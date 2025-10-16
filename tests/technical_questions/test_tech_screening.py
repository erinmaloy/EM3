from unittest import TestCase
import pandas as pd

from technical_questions.tech_screening import BulkCrossRefLookup


class TestBulkCrossRefLookup(TestCase):
    def setUp(self):
        # Create an instance of the BulkCrossRefLookup class
        self.lookup_instance = BulkCrossRefLookup()

    def test_return_type(self):
        # Test the bulk_crossref_lookup function

        # Create test data for method input
        source_df = pd.DataFrame(TestData.input_data())

        # Call the lookup method
        result_series = self.lookup_instance.temp_dealer_customer_consolidation(
            source=source_df
        )

        # Checking the return data type is correct for the method
        self.assertIsInstance(result_series, pd.Series, "The result should be a pandas Series")

    def test_length_of_return_data(self):
        # Test the bulk_crossref_lookup function

        # Create test data for method input
        source_df = pd.DataFrame(TestData.input_data())

        # Call the lookup method
        result_series = self.lookup_instance.temp_dealer_customer_consolidation(
            source=source_df
        )

        # Checking the length of the result series is correct
        self.assertEqual(len(result_series), len(source_df), f"The result should have {len(source_df)} rows")

    def test_results_at_index_0(self):
        # Test the bulk_crossref_lookup function

        # Create test data for method input
        source_df = pd.DataFrame(TestData.input_data())

        # Call the lookup method
        result_series = self.lookup_instance.temp_dealer_customer_consolidation(
            source=source_df
        )

        # Checking the results in the first row of data within the pandas series
        self.assertEqual([[]], result_series[0],
                         "The first row should contain a nested list, with the inner list being empty")

    def test_results_at_index_1(self):
        # Test the bulk_crossref_lookup function

        # Create test data for method input
        source_df = pd.DataFrame(TestData.input_data())

        # Call the lookup method
        result_series = self.lookup_instance.temp_dealer_customer_consolidation(
            source=source_df
        )

        # Checking the data type is correct for the second row of data within the pandas series
        self.assertIsInstance(result_series[1], list, "The second row should be a list")

        # Checking the length of the second row of data within the pandas series
        self.assertEqual(1, len(result_series[1]), "The second row should be a list, containing 1 element.")

        # Checking the data type is correct for the first element of the second row of data within the pandas series
        self.assertIsInstance(result_series[1][0], dict,
                              "The second row should contain a list with a nested dictionary")

        # Checking the content of the first element of the second row of data within the pandas series
        expected_dict_at_index_one = {
            "customerID": "9998880003",
            "sourceSystemCode": "HCM",
            "dealerCustomerNumber": "SS0002",
            "dealerCode": "SS02",
        }
        self.assertEqual(expected_dict_at_index_one, result_series[1][0],
                         "The second row should contain a list with a nested dictionary")

    def test_results_at_index_2(self):
        # Test the bulk_crossref_lookup function

        # Create test data for method input
        source_df = pd.DataFrame(TestData.input_data())

        # Call the lookup method
        result_series = self.lookup_instance.temp_dealer_customer_consolidation(
            source=source_df
        )

        # Checking the data type is correct for the third row of data within the pandas series
        self.assertIsInstance(result_series[2], list, "The third row should be a list")

        # Checking the length of the third row of data within the pandas series
        self.assertEqual(2, len(result_series[2]), "The third row should be a list, containing 2 element.")

        # Checking the data type is correct for the first element of the third row of data within the pandas series
        self.assertIsInstance(result_series[2][0], dict,
                              "The third row should contain a list of two elements, "
                              "the inner list containing a dictionary at index 0")

        # Checking the content of the first element of the third row of data within the pandas series
        third_row_expected_dict_at_index_zero = {
            "customerID": "9998880005",
            "sourceSystemCode": "HCM",
            "dealerCustomerNumber": "SS0002",
            "dealerCode": "SS02",
        }
        self.assertEqual(third_row_expected_dict_at_index_zero, result_series[2][0],
                         "The third row should contain a list with a nested dictionary")

        # Checking the data type is correct for the second element of the third row of data within the pandas series
        self.assertIsInstance(result_series[2][1], dict,
                              "The third row should contain a list of two elements, "
                              "the inner list containing a dictionary at index 1")

        # Checking the content of the second element of the third row of data within the pandas series
        third_row_expected_dict_at_index_one = {
            "customerID": "9998880005",
            "sourceSystemCode": "HCM",
            "dealerCustomerNumber": "SS0003",
            "dealerCode": "SS03",
        }
        self.assertEqual(third_row_expected_dict_at_index_one, result_series[2][1],
                         "The third row should contain a list with a nested dictionary")


class TestData:
    @staticmethod
    def input_data():
        return [
            {
                "customerID": "9998880001",
                "sourceSystemCode": "HCM"
            },
            {
                "customerID": "9998880003",
                "sourceSystemCode": "HCM"
            },
            {
                "customerID": "9998880005",
                "sourceSystemCode": "HCM"
            }
        ]