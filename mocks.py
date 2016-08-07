
#gunicorn -k gevent -w 6 mocks
#gunicorn -k "egg:meinheld#gunicorn_worker" -w 6 mocks
# curl -v -XPOST 0.0.0.0:8000/SID0003030 -d @mvd_full.req
# curl -v -XPOST localhost:8000/bigfile -d @bigfile.req
#curl -v -XPOST localhost:8000/bigfile -d @bigfile_fake.req

from wsgiref import simple_server

import falcon
import default_handler

from loader import load_data

import logging
import sys

root = logging.getLogger()
# root.setLevel(logging.DEBUG)
# #
# ch = logging.StreamHandler(sys.stdout)
# ch.setLevel(logging.DEBUG)
# ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
# root.addHandler(ch)


MAPPING = load_data()

api = application = falcon.API()

for url, expectations in MAPPING.items():
    print(url)
    logging.info('Route added -->> %s' % url)
    api.add_route('%s' % url, default_handler.DefaultHandler(expectations))


if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, application)
    httpd.serve_forever()
