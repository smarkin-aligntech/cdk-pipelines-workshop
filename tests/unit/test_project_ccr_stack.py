import aws_cdk as core
import aws_cdk.assertions as assertions

from project_ccr.project_ccr_stack import ProjectCcrStack

# example tests. To run these tests, uncomment this file along with the example
# resource in project_ccr/project_ccr_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ProjectCcrStack(app, "project-ccr")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
