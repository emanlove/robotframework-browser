from enum import Enum
from typing import Any

AssertionOperator = Enum("AssertionOperator", "NO_ASSERTION == != contains < > <= >=")


def verify_assertion(value: Any, operator: AssertionOperator, expected, message=""):
    if operator.name == "==" and value != expected:
        raise AssertionError(f"{message} `{value}` should be `{expected}`")
    if operator.name == "!=" and value == expected:
        raise AssertionError(f"{message} `{value}` should not be `{expected}`")
    if operator.name == "<" and value >= expected:
        raise AssertionError(f"{message} `{value}` should be less than `{expected}`")
    if operator.name == ">" and value <= expected:
        raise AssertionError(f"{message} `{value}` should be greater than `{expected}`")
    if operator.name == "<=" and value > expected:
        raise AssertionError(
            f"{message} `{value}` should be less than or equal `{expected}`"
        )
    if operator.name == ">=" and value < expected:
        raise AssertionError(
            f"{message} `{value}` should be greater than or equal `{expected}`"
        )
    if operator.name == "contains" and expected not in value:
        raise AssertionError(f"{message} `{value}` did not contain `{expected}`")
    elif operator.name not in AssertionOperator.__members__:
        raise AssertionError(
            f"{message} `{operator.name}` is not a valid assertion operator"
        )