''' Adelaide's code practicing pandas'''
#goal is to read in and extract information, journal dates, secret codes
#template available, add one or two lines to each method
#pylint will not like except statements, he removed all of them
#to read in locations part, read.csv()

import re
import pandas as pd

def load_artifact_data(excel_filepath):
    '''
    Reads artifact data from a specific sheet ('Main Chamber') in an Excel file,
    skipping the first 3 rows.

    Args:
        excel_filepath (str): The path to the artifacts Excel file.

    Returns:
        pandas.DataFrame: DataFrame containing the artifact data.
    '''
    df=pd.read_excel(excel_filepath, sheet_name = 'Main Chamber', skiprows=3)
    return df
    # Hint: Use pd.read_excel, specify sheet_name and skiprows
    # return the resulting DataFrame

def load_location_notes(tsv_filepath):
    '''
    Reads location data from a Tab-Separated Value (TSV) file.

    Args:
        tsv_filepath (str): The path to the locations TSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the location data.
    '''
    df=pd.read_csv(tsv_filepath, sep='\t')
    return df
    # Hint: Use pd.read_csv, specify the separator for tabs ('\t')
    # Replace 'pass' with your code
    # return the resulting DataFrame

def extract_journal_dates(journal_text):
    '''
    Extracts all dates in MM/DD/YYYY format from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of date strings found in the text.
    '''
    df = re.findall(r"(?:0[1-9]|1[0-2])/(?:0[1-9]|[12]\d|3[01])/\d{4}", journal_text)
    return df
    # Hint: Use re.findall with a raw string pattern for MM/DD/YYYY format.
    # Pattern idea: r"\d{2}/\d{2}/\d{4}"
    #for the second try i used r"(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/\d{4}"
    # Replace 'pass' with your code
    # return the list of found dates

def extract_secret_codes(journal_text):
    '''
    Extracts all secret codes in AZMAR-XXX format (XXX are digits) from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of secret code strings found in the text.
    '''
    df = re.findall(r"AZMAR-\d{3}", journal_text)
    return df
    # Hint: Use re.findall with a raw string pattern for AZMAR- followed by 3 digits.
    # Pattern idea: r"AZMAR-\d{3}"
    # Replace 'pass' with your code
    # return the list of found codes


# --- Optional: Main execution block for your own testing ---
if __name__ == '__main__':
    # Define file paths (adjust if your files are located elsewhere)
    EXCEL_FILE = 'artifacts.xlsx'
    TSV_FILE = 'locations.tsv'
    JOURNAL_FILE = 'journal.txt'

    print(f"--- Loading Artifact Data from {EXCEL_FILE} ---")
    try:
        artifacts_df = load_artifact_data(EXCEL_FILE)
        print("Successfully loaded DataFrame. First 5 rows:")
        print(artifacts_df.head())
        print("\nDataFrame Info:")
        artifacts_df.info()
    except FileNotFoundError:
        print(f"Error: File not found at {EXCEL_FILE}")

    print(f"\n--- Loading Location Notes from {TSV_FILE} ---")
    try:
        locations_df = load_location_notes(TSV_FILE)
        print("Successfully loaded DataFrame. First 5 rows:")
        print(locations_df.head())
        print("\nDataFrame Info:")
        locations_df.info()
    except FileNotFoundError:
        print(f"Error: File not found at {TSV_FILE}")

    print(f"\n--- Processing Journal from {JOURNAL_FILE} ---")
    try:
        with open(JOURNAL_FILE, 'r', encoding='utf-8') as f:
            journal_content = f.read()

        print("\nExtracting Dates...")
        dates = extract_journal_dates(journal_content)
        print(f"Found dates: {dates}")

        print("\nExtracting Secret Codes...")
        codes = extract_secret_codes(journal_content)
        print(f"Found codes: {codes}")

    except FileNotFoundError:
        print(f"Error: File not found at {JOURNAL_FILE}")
