#!/usr/bin/python3
'''
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
'''


if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    encoded_data = urllib.parse.urlencode(data).encode('ascii')
    request = urllib.request.Request(url, data=encoded_data, method='POST')

    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
