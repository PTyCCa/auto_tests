import os

import right
import wrong1
import wrong2
import wrong3


def get_validator():
    name = os.environ['FUNCTION_VERSION']
    return {
        "right": right,
        "wrong1": wrong1,
        "wrong2": wrong2,
        "wrong3": wrong3,
    }[name].make_validator

def make_validator():
    checks = []

    def add_check(check):
        checks.append(check)

    def is_valid(data):
        return all(predicate(data) for predicate in checks)

    return add_check, is_valid

def make_validator():
    checks = []

    def add_check(check):
        checks.append(check)

    def is_valid(data):
        return True

    return add_check, is_valid

def make_validator():
    checks = []

    def add_check(check):
        checks.append(check)

    def is_valid(data):
        return False

    return add_check, is_valid


def make_validator():
    checks = []

    def add_check(check):
        checks[:] = [check]

    def is_valid(data):
        return all(predicate(data) for predicate in checks)

    return add_check, is_valid