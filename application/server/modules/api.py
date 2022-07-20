from email import parser
from flask import redirect, request, send_file, url_for, jsonify, abort
from application.server import app, api
from flask_restful import Resource, reqparse
from application.server.modules.generator import Scale

parser = reqparse.RequestParser()
chords = {}

class Chords(Resource):
    def get(self):
        return jsonify(chords)

class Generate(Resource):
    def post(self):
        parser.add_argument('key', type=str, location='form')
        parser.add_argument('mode', type=str, location='form')
        args = parser.parse_args()
        key = args['key']
        mode = args['mode']
        generator = Scale(key, mode)
        generator.generate()
        chords[generator.midiname] = generator.progression
        return jsonify(True)



api.add_resource(Chords, '/')
api.add_resource(Generate, '/midifile/generate')
