import pytest
from Browser.assertion_engine import verify_assertion, AssertionOperator


def test_equals():
    _validate_operator(AssertionOperator["=="], "actual", "actual", "unexpected")


def _validate_operator(operator: AssertionOperator, actual, expected, invalid):
    verify_assertion(actual, operator, expected)
    with pytest.raises(AssertionError):
        verify_assertion(actual, operator, invalid)


def test_not_equals():
    _validate_operator(AssertionOperator["!="], "actual", "expected", "actual")


def test_contains():
    _validate_operator(AssertionOperator["contains"], "actual", "ctua", "nope")


def test_greater():
    _validate_operator(AssertionOperator["<"], 1, 2, 0)


def test_less():
    _validate_operator(AssertionOperator[">"], 2, 1, 3)


def test_greater_or_equal():
    _validate_operator(AssertionOperator["<="], 1, 1, 0)


def test_less_or_equal():
    _validate_operator(AssertionOperator[">="], 2, 2, 3)