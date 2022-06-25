import configparser

def get_url(file):
    # Create an instance
    config = configparser.ConfigParser()
    # Open the file
    config.read(file)
    # Get url from google sheets section
    sheet_url = config.get('gsheets', 'sheet_url')
    return sheet_url