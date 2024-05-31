#!/usr/bin/python3
'''
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
'''


if __name__ == '__main__':
    import requests
    import sys

    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]

    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print(None)
