"""
utils.py
Small helper utilities used by the assistant.
"""

import operator
from typing import Callable

def get_operator_fn(op: str) -> Callable:
    return {
        '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        '*': operator.mul,
        'times': operator.mul,
        'divided': operator.truediv,
        '/': operator.truediv,
    }[op]

def eval_binary_expr(op1: str, oper: str, op2: str):
    op1, op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)
