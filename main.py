import pandas as pd
import sys
import os
import logging


def setup_logging():
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create a file handler and set the level to ERROR
    file_handler = logging.FileHandler('error.log', mode='w')
    file_handler.setLevel(logging.ERROR)

    # Create a formatter and set it for the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)


def main():
    # Check if the file path exists
    if len(sys.argv) != 2:
        logging.info("File path missing")
        sys.exit(1)

    # Check if the input file exists
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        logging.error("Input file does not exist: %s", input_file)
        sys.exit(1)

    try:
        # Load the Excel file
        xls_file = pd.ExcelFile(input_file)

        # Read the first sheet into a DataFrame
        df = pd.read_excel(xls_file)

        # Get the row count of the DataFrame
        row_count = len(df)

        print(row_count)

    except Exception as e:
        logging.error("An error occurred: %s", str(e))


if __name__ == "__main__":
    setup_logging()
    main()
