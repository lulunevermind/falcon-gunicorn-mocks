import os
import json

STORAGE_DIR = 'reqResps'
EXPECTATIONS_DIR = 'expectations'
PARSED_DIRS = [EXPECTATIONS_DIR, STORAGE_DIR]


def load_expectations():
    MAPPING = {}
    for root, dirs, files in os.walk(EXPECTATIONS_DIR, topdown=False):
        for name in files:
            with open(os.path.join(root, name), 'r') as expectations:
                exp = json.load(expectations)
                print(exp)
                name = name.strip('.json')
                print('%s expectations...' % name)
                request_filename = exp['request']['file']
                response_filename = exp['response']['file']
                print(request_filename)
                exp['request']['file'] = open(os.path.join(STORAGE_DIR, request_filename)).read()
                exp['response']['file'] = open(os.path.join(STORAGE_DIR, response_filename)).read()
                if not MAPPING.get(exp['url']):
                    MAPPING[exp['url']] = exp
    print(MAPPING)
    return MAPPING

if __name__ == '__main__':
    mapping = load_expectations()
