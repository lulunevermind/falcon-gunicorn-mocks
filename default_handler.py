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
                #from here we parsing expectation line like {"contains": ["<dob:usrF>simple</dob:usrF>"],
                #  "request": "mvd_simple.req", "response": "mvd_simple.resp",
                #"response-header": {"Content-Type": "text/xml; charset=utf-8", "Accept": "ALL"}}
                response_headers = expectations.get("response-header", default=[])
                if expectation == 'contains':
                    for exp in expressions:
                        if body.__contains__(exp.encode('utf-8')):
                            response = expectations['response']
                            resp.body = response
                            logging.info('Match for %s succeded!' % exp.encode('utf-8'))
                            logging.info('Setting headers: %s' % response_headers)
                            for k, v in response_headers.items():
                                resp.append_header(k, v)
