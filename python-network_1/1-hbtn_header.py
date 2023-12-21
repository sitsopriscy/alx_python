#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL,
and displays the body of the response.

If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code.

Usage:
    ./1-hbtn_header.py <URL>
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        print(response.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")
