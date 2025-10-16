from technical_questions.supporting_code.model_objects import (
    AnnotatedStepFactory,
    DealerCustomerConsolidationRef,
    step
)

# Candidate Name:


# 1. Given an input of 3 records as a DataFrame,
# perform a bulk lookup and return a panda series with
# 3 rows by capturing the results of the lookups.

import pandas as pd


class BulkCrossRefLookup(AnnotatedStepFactory):
    def __init__(self):
        self.dcc = DealerCustomerConsolidationRef()

    @step.transform_column.to_temp(target="temp_dealer_customer_consolidation")
    def temp_dealer_customer_consolidation(self, source: pd.DataFrame) -> pd.Series:
        # The source DataFrame will contain 2 columns customerID and sourceSystemCode
        # and will have 3 rows of data as shown in example below
        """
            |customerID | sourceSystemCode|
            |9998880001 | HCM             |
            |9998880003 | HCM             |
            |9998880005 | HCM             |
        """

        # Validate if customerID & sourceSystemCode exists in source DataFrame
        # Type code below:

        # Convert the source DataFrame to a list of dicts,
        # and assign it to a variable called helper_input_list
        # Type code below:

        # The lookup method below returns an iterator
        # object which contains decision objects.
        # Each decision object corresponds to one row in the source df.
        # A decision object can contain 1-n ValueChoice objects.
        # A ValueChoice object with the value set to None means
        # the lookup returned nothing for that row.
        decision_iterator = self.dcc.do_lookup(record_list=helper_input_list)

        """
        [
            Decisions(
                    [
                        ValueChoice(
                            subject="test_dcc",
                            value=None,
                        ),
                    ]
                ),
            Decisions(
                    [
                        ValueChoice(
                            subject="test_dcc",
                            value={
                                "customerID":"9998880003",
                                "sourceSystemCode": "HCM",
                                "dealerCustomerNumber": "SS0002",
                                "dealerCode": "SS02",
                            },
                        ),
                    ]
                ),  
            Decisions(
                    [
                        ValueChoice(
                            subject="test_dcc",
                            value={
                                "customerID":"9998880005",
                                "sourceSystemCode": "HCM",
                                "dealerCustomerNumber": "SS0002",
                                "dealerCode": "SS02",
                            },
                        ),
                        ValueChoice(
                            subject="test_dcc",
                            value={
                                "customerID":"9998880005",
                                "sourceSystemCode": "HCM",
                                "dealerCustomerNumber": "SS0003",
                                "dealerCode": "SS03",
                            },
                        )
                    ]
                ),
        ]
        """

        # Using the decision_iterator response from the lookup method above,
        # iterate over the responses and capture the results.
        # The Decisions objects contain nested objects
        # (see example in doc string above).
        # Decisions -> value_choice -> value
        # Type code below:

        # Build a panda series that contains the return values for these lookups.
        # Each row of the panda series should only contain the lookup results
        # of the corresponding row in the source DataFrame.
        # If a row from the source DataFrame resulted in no lookup value being returned
        # (value=None), that row in the panda series should be an empty list.
        # The length of the panda series being returned should match the length of
        # the source DataFrame.
        # Return the pandas series
        # Type code below:


# 2. Given the mapping function below map_std_mfr_cd with dictionary as an input parameter,
# what unit test scenarios would you test?

def map_std_mfr_cd(temp: dict):
    if temp.get("standard_manufacturer_code") and len(temp.get("standard_manufacturer_code")) > 4:
        std_man_code = temp.get("standard_manufacturer_code")
    else:
        std_man_code = "NA"
    return std_man_code


# Write out your unit tests below


if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
