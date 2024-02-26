import aws_cdk as core
import aws_cdk.assertions as assertions

from legendary_octo_computing_machine.legendary_octo_computing_machine_stack import LegendaryOctoComputingMachineStack

# example tests. To run these tests, uncomment this file along with the example
# resource in legendary_octo_computing_machine/legendary_octo_computing_machine_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LegendaryOctoComputingMachineStack(app, "legendary-octo-computing-machine")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
