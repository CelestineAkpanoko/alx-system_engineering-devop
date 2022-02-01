#!/usr/bin/python3
'''A script that retrieves data from an API and exports it to a CSV file.
'''
import re
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            emp_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
            todos_res = requests.get('{}/todos'.format(API_URL)).json()
            emp_name = emp_res.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            with open('{}.csv'.format(id), 'w') as file:
                for todo in todos:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            emp_name,
                            todo.get('completed'),
                            todo.get('title')
                        )
                    )