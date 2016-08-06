import falcon
import logging


class Resource(object):

    def __init__(self, mappings):
        self.mappings = mappings

    def on_get(self, req, resp):
        resp.body = '{"message": "Hello world!"}'
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        body = req.stream.read()
        logging.info('Route triggered -->> %s' % req.path)
        logging.info('Avaliable expectations -->> %s' % self.mappings['expectations'])
        for expectation, expressions in self.mappings['expectations'].iteritems():
            logging.info('Expectations: %s, Expressions: %s' % (expectation, expressions))
            if expectation == 'contains':
                for exp in expressions:
                    logging.info('Looking for %s in request' % exp)
                    if body.__contains__(exp):
                        response = self.mappings['response']['file']
                        resp.body = response
                        logging.info('Response finded -->> %s' % response)
                    else:
                        logging.info('No response found with expectations!')