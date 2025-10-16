# Empty class, just to make imports happy, no logic is needed here.
from unittest import mock


class AnnotatedStepFactory:
    pass


# This is a fake class to mimic what would happen if we called the API
# for our lookup. We are not actually calling the API in this test.
class DealerCustomerConsolidationRef:

    @staticmethod
    def _check_keys(record):
        if record.get('customerID') == '9998880001' and record.get('sourceSystemCode') == 'HCM':
            return [ValueChoice("test_dcc", None)]
        elif record.get('customerID') == '9998880003' and record.get('sourceSystemCode') == 'HCM':
            return [ValueChoice("test_dcc",
                                {
                                    "customerID": "9998880003",
                                    "sourceSystemCode": "HCM",
                                    "dealerCustomerNumber": "SS0002",
                                    "dealerCode": "SS02",
                                }
                                )
                    ]
        elif record.get('customerID') == '9998880005' and record.get('sourceSystemCode') == 'HCM':
            return [
                ValueChoice("test_dcc",
                            {
                                "customerID": "9998880005",
                                "sourceSystemCode": "HCM",
                                "dealerCustomerNumber": "SS0002",
                                "dealerCode": "SS02",
                            }
                            ),
                ValueChoice("test_dcc",
                            {
                                "customerID": "9998880005",
                                "sourceSystemCode": "HCM",
                                "dealerCustomerNumber": "SS0003",
                                "dealerCode": "SS03",
                            }
                            )
            ]
        else:
            return [ValueChoice("test_dcc", None)]

    def do_lookup(self, record_list):
        for record in record_list:
            yield Decisions(self._check_keys(record))


"""
Supporting model objects to mimic the response we'd get back from our cross ref helper
"""


class Decisions:
    def __init__(self, value_choices):
        self.value_choices = value_choices


class ValueChoice:
    def __init__(self, subject, value):
        self.subject = subject
        self.value = value


class InnerSteps:
    def __init__(self):
        self.to_temp = self.func

    @classmethod
    def func(cls, *args, **kwargs):
        def wrapper(fn):
            def wrapped(*args, **kwargs):
                return fn(*args, **kwargs)
            return wrapped
        return wrapper


class Steps:
    def __init__(self):
        self.transform_column = InnerSteps()

step = Steps()

#https://www.geeksforgeeks.org/decorators-in-python/