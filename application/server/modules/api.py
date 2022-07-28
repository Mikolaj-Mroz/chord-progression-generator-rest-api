from flask import jsonify, send_file
from application.server import app, api
from flask_restful import Resource, reqparse
from application.server.modules.generator import Scale
import json

parser = reqparse.RequestParser()
progressions = {'progressions': {}}

# update existing progressions
with open('application\server\static\data.json') as fp:
    progressions = json.load(fp)


# Returns list of already generated Progressions
class Progressions(Resource):
    def get(self):
        return jsonify(progressions)

# Generates a new progression
class Generate(Resource):
    def post(self):
        parser.add_argument('key', type=str)
        parser.add_argument('mode', type=str)
        args = parser.parse_args()
        key = args['key']
        mode = args['mode']
        generator = Scale(key, mode)
        generator.generate()
        progressions['progressions'][generator.midiname] = generator.progression
        with open('application\server\static\data.json', 'w') as fp:
            json.dump(progressions, fp)
        return jsonify({
                        'message': 'success',
                        'chord id': generator.midiname
                        })

class ReturnFile(Resource):
    def get(self, filename):
        return send_file('static/' + filename + '.mid')


api.add_resource(Progressions, '/')
api.add_resource(Generate, '/generate')
api.add_resource(ReturnFile, '/<string:filename>')
