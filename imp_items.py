"""
Module: stock_data_downloader

This module provides functions to download stock data from various sources.

Functions:
    format_date: Format a date string.
"""

import os
from datetime import datetime , timedelta

def format_date(input_date):
    """
    Return the date in the format "26APR2024".

    Args:
        input_date (str): The input date string.

    Returns:
        str: The formatted date string.
    """
    # Parse the input date string
    parsed_date = datetime.strptime(input_date, '%Y-%m-%d')

    # Format the date in the desired format
    formatted_date = parsed_date.strftime('%d%b%Y').upper()

    return formatted_date

def find_csv_files(folder):
    """
    Find CSV files in a folder and its subdirectories.

    Args:
    folder (str): Path to the folder to search.

    Returns:
    list: A list of paths to CSV files found.
    """
    csv_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".csv"):
                csv_files.append(os.path.join(root, file))
    return csv_files

today_date = datetime.today()
yesterday_date = today_date - timedelta(days = 1)
# Format the date using the format_date function
formatted_today_date = format_date(today_date.strftime('%Y-%m-%d'))
formatted_yestrday_date = format_date(yesterday_date.strftime('%Y-%m-%d'))
# List of website URLs
website_urls = [
    f'https://nsearchives.nseindia.com/content/historical/EQUITIES/{today_date.strftime("%Y")}/{today_date.strftime("%b").upper()}/cm{formatted_today_date}bhav.csv.zip',
    'https://www.topstockresearch.com/rt/Screener/Technical/PivotPoint/StandardPivotPoint/ListSupportOrResistance',
    f'https://nsearchives.nseindia.com/content/historical/EQUITIES/{yesterday_date.strftime("%Y")}/{yesterday_date.strftime("%b").upper()}/cm{formatted_yestrday_date}bhav.csv.zip'
]

# Path to the "Documents" folder
documents_folder = os.path.join(os.path.expanduser("~"), 'Documents')
base_path = os.path.join(documents_folder, 'stock_ai')
# List of paths
paths = [base_path,os.path.join(base_path,'data'),os.path.join(base_path,'results'),os.path.join(base_path,'data','company_wise_data')]

print(website_urls)
print(paths)
