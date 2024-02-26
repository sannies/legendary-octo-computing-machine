from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from aws_cdk.aws_stepfunctions import StateMachine, Parallel, DistributedMap, Pass, Result
from aws_cdk.aws_lambda import Function, Runtime, Code
from aws_cdk.aws_stepfunctions_tasks import LambdaInvoke
from constructs import Construct


class LegendaryOctoComputingMachineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        f = Function(self, id="Lambda", runtime=Runtime.PYTHON_3_12, handler="index.handler",
                      code=Code.from_asset('lambda'))
        li_f = LambdaInvoke(self, id="LambdaInvoke", lambda_function=f)
        init = Pass(self, id="Pass", result=Result.from_object({"p": ["Hello", "World"]}))
        p = Parallel(self, id="Parallel")
        d = DistributedMap(self, id="DistributedMap", items_path="$.p")
        d.item_processor(li_f)
        p.branch(d)
        StateMachine(self, id="repro", definition=init.next(p))
