import falcon
import logging


class DefaultHandler(object):

    def __init__(self, mappings):
        self.mappings = mappings

    def on_post(self, req, resp):
        body = req.stream.read()
        logging.info('Route triggered -->> %s' % req.path)
        for expectations in self.mappings:
            for expectation, expressions in expectations.items():
                if expectation == 'contains':
                    for exp in expressions:
                        if body.__contains__(exp.encode('utf-8')):
                            response = expectations['response']
                            resp.body = response
                            resp.append_header("Content-Type", "text/xml; charset=utf-8")
