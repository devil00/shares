import unittest
import csv
import random
import calendar
from share_analysis import ShareAnalysis


class TestShareAnalysis(unittest.TestCase):
    """
    Class to test the share analysis result.
    """
    def setUp(self):
        self.test_file = "test_shares_data.csv"
        self.test_data = self._generate_share_test_data()
        self.share_analysis = ShareAnalysis(self.test_file)

    def _generate_share_test_data(self):
        """
        Generate a csv file which will contain share price data for every
        company.
        """
        start_year = random.randint(1990, 2001)
        end_year = random.randint(2002, 2014)
        no_companies = random.randint(1, 10)
        # Prepare header for csv file.
        share_headers = ['Year', 'Month']
        test_data = {}
        for i in xrange(1, no_companies+1):
            company = "Company_{}".format(i)
            share_headers.append(company)
            test_data[company] = {'price': 0, 'year': 0, 'month': 0}
        with open(self.test_file, "wb") as data_file:
            share_writer = csv.writer(data_file, quotechar='|',
                                      quoting=csv.QUOTE_MINIMAL)
            share_writer.writerow(share_headers)
            for year in range(start_year, end_year+1):
                for month in [calendar.month_abbr[i] for i in range(1, 13)]:
                    data_row = [year, month]
                    for company in share_headers[2:]:
                        share_value = random.randint(100, 1000)
                        # Make sure to store max share price for every company
                        if share_value > test_data[company]['price']:
                            test_data[company].update(
                                {'price': share_value, 'year': year,
                                 'month': month})
                            data_row.append(share_value)
                    share_writer.writerow(data_row)

            return test_data

        def test_share_file_extension(self):
            """
            Test whether share file is csv file or not. If csv then it should
            be available .
            """
            self.assertEqual(self.share_analysis._is_valid_share_file(), True)

        def test_data_validity(self):
            """
            Test if result obtained matches exactly with data available from
            csv file.
            """
            result = self.share_analysis.execute()
            result = result.split("\n")[3:]
            for com_info in result:
                if com_info:
                    company, year, month, price = com_info.split("\t")
                    self.assertEqual(str(year),
                                     str(self.test_data[company]['year']))
                    self.assertEqual(str(month),
                                     str(self.test_data[company]['month']))
                    self.assertEqual(str(price),
                                     str(self.test_data[company]['price']))

    def test_all_companies_listing(self):
        """
        Test if company mentioned in the result is actually exist in the source
        data or csv file.
        """
        result = self.share_analysis.execute()
        for key in self.test_data:
            self.assertTrue(key in result)


if __name__ == "__main__":
    unittest.main()
