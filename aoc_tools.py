from dotenv import load_dotenv
from copy import copy
import requests
import os

load_dotenv()

RAW_URL_STR = "https://adventofcode.com/2024/day/$DAY_NUMBER/input"
SESSION_COOKIE = os.getenv("SESSION_COOKIE")

def retrieve_input(day:int, year:int=2024) -> str:
    """
    Retrieve input from the adventofcode website

    Args:
        day (int): day of december 1-25
        year (int, optional): year. Defaults to 2024.

    Returns:
        str: raw input
    """
    if day == 0:
        print("Change the Class name in the template Day class, please")
        exit()

    # Specify active login for retrieving outside of the browser
    headers = {
        "Cookie": f"session={SESSION_COOKIE}"
    }
    placeholders = {
        "$DAY_NUMBER": str(day),
        "$YEAR": str(year)
    }

    # Generate final url string
    input_url_str = copy(RAW_URL_STR)
    for p,v in placeholders.items():
        input_url_str = input_url_str.replace(p,v)
    
    response = requests.get(
        input_url_str,
        headers=headers
    )
    if response.status_code == 200:
        # Retrieve as a string
        text = response.text
        return(text)
    else:
        
        print(response.text)