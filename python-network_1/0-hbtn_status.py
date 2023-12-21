""" A script that fetches a URL  
    URL: https://alu-intranet.hbtn.io/status
    Usage:
    ./0-hbtn_status.py | cat -e
"""
import requests

def get_url_status(url):
    """
    Fetches the status of the given URL using the requests package.

    Args:
        url (str): The URL to fetch.

    Returns:
        requests.models.Response: The response object.

    Raises:
        requests.exceptions.RequestException: If the request encounters an error.
    """
    
    
    return response

if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'

    try:
        response = get_url_status(url)
        print("Body response:")
        print(f"\t- type: {type(response.text)}")
        print(f"\t- content: {response.text}")
        print(f"({len(response.text)} chars long)")
    except requests.exceptions.RequestException as e:
        print(f"[stderr]: {e}")
