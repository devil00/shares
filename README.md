shares
======

It contains the solutions for the below mentioned problem:
 List for each company , year and month for which stock price was highest.

============
Requirements
============
 - python >= 2.7
 - Linux OS

===========================
Instructions to test or run
===========================
1. Clone Repository:
   Unix/Mac: git clone git@github.com:mayur-mq/shares.git

2. Run the script
   python <script_name> -f <stock_csv_file_path>
   python share_analysis.py -f share_data.csv

   Output:

    Company Name	Year	Month	Max. Price

        Company_1	2005	Jan	1000
        Company_2	2001	May	959
        Company_3	2001	Jan	895
        Company_4	2001	Jan	128


3. Run Test Cases
   python unitest_share_analysis.py 
