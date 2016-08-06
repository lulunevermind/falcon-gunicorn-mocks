import os
import json
import logging

STORAGE_DIR = 'reqResps'
EXPECTATIONS_DIR = 'expectations'
PARSED_DIRS = [EXPECTATIONS_DIR, STORAGE_DIR]


def load_data():
    MAPPING = {}
    for root, dirs, files in os.walk(EXPECTATIONS_DIR, topdown=False):
        for name in files:
            with open(os.path.join(root, name), 'r') as expectations:
                exp_by_url = json.load(expectations)
                logging.info('Expectation file found -->> %s' % exp_by_url)
                for k, expectations in exp_by_url.items():
                    print(k, expectations)
                    if k == 'url':
                        continue
                    for expectation in expectations:
                        print(expectation)
                        request_filename = expectation['request']
                        response_filename = expectation['response']
                        expectation['request'] = open(os.path.join(STORAGE_DIR, request_filename)).read()
                        expectation['response'] = open(os.path.join(STORAGE_DIR, response_filename)).read()
                        url = exp_by_url['url']
                        if not MAPPING.get(url):
                            MAPPING[url] = [expectation]
                        else:
                            MAPPING[url] += [expectation]
    # logging.info('FULL MAPPING -->> %s' % MAPPING)
    return MAPPING

if __name__ == '__main__':
    mapping = load_data()
