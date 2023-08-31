#!/usr/bin/env python3
import os

import aws_cdk as cdk

from lib.multi_region_s3_crr_source.stack import MultiRegionS3CrrSourceStack
from lib.multi_region_s3_crr_source.construct import MultiRegionS3CrrProps

from lib.multi_region_s3_crr_target.stack import MultiRegionS3CrrTargetStack


tags = {
    "Region" : "us-west-2",
    "Owner" : "smarkin@aligntech.com",
    "Environment" : "dev",
    "Requestor" : "rnd/sw/peg/cloudops",
    "Role": "ITIO/CloudOps",
    "Type": "workshop"
}

app = cdk.App()


target_stack = MultiRegionS3CrrTargetStack(app, "MultiRegionCcrTargetStack",
    env=cdk.Environment(region='us-west-1')
    )

source_props = MultiRegionS3CrrProps(
    target_bucket=target_stack.bucket,
    target_kms_id_ssm_parameter_name=target_stack.ssm_paramter_name,
    target_region=target_stack.region
)

source_stack = MultiRegionS3CrrSourceStack(app, "MultiRegionCcrSourceStack",
    props=source_props,
    env=cdk.Environment(region='us-west-2')
)

# add default tags on the stack
for key, value in tags.items():
    for stack in [target_stack, source_stack]:
        cdk.Tags.of(stack).add(
            key, value
        )

source_stack.add_dependency(target_stack)
app.synth()
