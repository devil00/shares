# -*- coding: utf-8 -*-

"""
Solution to the given problem.
Listing for each company, year and month in which the share price was highest.

@author: Mayur Swami
@date: 26/08/2014
"""

import csv
from collections import OrderedDict
from optparse import OptionParser


class ShareException(Exception):
    """
    A base class to raise all the exceptions related to
    `:class`:`ShareAnalysis`.
    """
    def __init__(self, message=""):
        self.message = message
        super(ShareException, self).__init__(message)

    def __str__(self):
        return repr(self.message)

class ShareAnalysis(object):
    """
    This class will get the share data from a csv file and provide the list of
    year and month for each company when share price was highest.
    """
    def __init__(self, file_path):
        """
        :param file_path: Name of file which contains share price data for
                          companies.
        :type file_path: str
        """
        self.file_path = file_path

    def _is_valid_share_file(self):
        """
        Returns True if share file is csv and available or else raise
        exception with appropriate message.
        """
        try:
            share_file = open(self.file_path, "rb", 1)
        except (IOError, TypeError):
            raise ShareException("Share data file does not exist.")

        if not self.file_path.endswith(".csv"):
            raise ShareException("Program only support share data in "
                                 "valid csv file.")
        share_file.close()
        return True

    def _capture_result(self, share_data):
        """
        Returns the maximum share price of each company along with year and
        month.
        :param share_data: a dict containing key as company_name and value as
                           another dict having share info.
        :type share_data: dict
        e.g., share_data = {'Company_1': {'price': 400, 'year': 2012
                           , 'month': 'Feb'},..}
        """
        # Do proper formatting to represent final result.
        # Max. Price is the maximum price of share for a given year and month.
        result = '\nCompany Name\tYear\tMonth\tMax. Price\n\n'
        for company_name, analysis_dict in share_data.items():
            result += "{}\t{}\t{}\t{}\n".format(
                company_name, analysis_dict['year'], analysis_dict['month'],
                analysis_dict['price'])
        return result

    def execute(self):
        """
        Call this method to get the maximum price of share for every company
        along with year and month.
        """
        if self._is_valid_share_file():
            with open(self.file_path, 'rb') as share_csv:
                share_file = csv.reader(share_csv)
                # Ordered dict will maintain the insertion order of company
                # in the same order of csv file.
                share_data = OrderedDict()
                company_names = next(share_file)[2:]
                for name in company_names:
                    # Initialized Ordered dict with default values.
                    share_data[name] = {'price': 0, 'year': 0, 'month': 0}
                for row in share_file:
                    year, month = row[:2]
                    for name, price in zip(company_names, map(int, row[2:])):
                        # Update the share price for a company if share value,
                        # being iterated is larger than the current value.
                        if share_data[name]['price'] < price:
                            share_data[name].update(
                                {'price': price, 'year': year, 'month': month})

        return self._capture_result(share_data)

def main():
    usage = "Usage: %prog [options] arg1"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file_path", dest="file_path",
                      help="Provide the path to csv file containing share"
                      " price data.")
    (options, args) = parser.parse_args()
    share_analysis = ShareAnalysis(options.file_path)
    print share_analysis.execute()

if __name__ == "__main__":
    main()
