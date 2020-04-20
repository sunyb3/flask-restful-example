# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api
from resources import profiles, companies, books

api_v1 = Blueprint('api_v1', __name__)

api = Api(api_v1)

api.add_resource(profiles.ProfileListResource, '/profiles')
api.add_resource(profiles.ProfileResource, '/profiles/<string:id>')
api.add_resource(companies.CompaniesResource, '/company')
api.add_resource(books.BookResource, '/book')