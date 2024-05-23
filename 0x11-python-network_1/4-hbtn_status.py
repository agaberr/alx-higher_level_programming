#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
'''


if __name__ == '__main__':
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')

    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
