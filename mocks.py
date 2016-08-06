from wsgiref import simple_server

import falcon

import sid

from loader import load_expectations

import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
root.addHandler(ch)


MAPPING = load_expectations()
print(MAPPING)

api = application = falcon.API()

for key in MAPPING:
    logging.info('Key in MAPPINGS -->> %s' % key)
    api.add_route('%s' % key, sid.Resource(MAPPING[key]))


if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, application)
    httpd.serve_forever()
