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
        logging.info('Avaliable expectations -->> %s' % self.mappings['expectations'])
        for expectation, expression in self.mappings['expectations'].iteritems():
            print(expectation, expression)
        # print(self.mappings['response']['file'])
        # exp_method = mocks.MAPPING['mvd_simple']['']
        # if body.__contains__('123123'):
        #     print('contains!')
        # resp.body = '123'
