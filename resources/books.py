from flask import current_app, abort
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from common import code, pretty_result

class BookResource(Resource):
    """
    示例Book资源类
    """

    def __init__(self):
        self.parser = RequestParser()

    def get(self):
        data = {
            'name': 'wanli',
            'age': 12,
            'address': 'wuhan'
        }
        return pretty_result(code.OK, data=data)