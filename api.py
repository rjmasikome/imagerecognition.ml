from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import urllib
import sys
import subprocess
import mimetypes

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('url')

def parse_score(s):
    return float(s.split("=")[1].strip()[:-1])

def is_url_image(url):
    mimetype,encoding = mimetypes.guess_type(url)
    return (mimetype and mimetype.startswith('image'))

class ImgRec(Resource):
    def get(self):
        args = parser.parse_args()
        imgUrl = args['url']
        obj = {}

        if type(imgUrl) is not str:
            abort(404, description="url query is not defined", status=404)

        if is_url_image(imgUrl) is not True:
            abort(404, description="Image not found on the url", status=404)

        try:
            urllib.request.urlretrieve(imgUrl, "image")
            obj['url'] = imgUrl
        except urllib.error.HTTPError as err:
            abort(err.code, description=str(err), status=err.code)

        s2_out = subprocess.check_output([sys.executable, "classify.py", "--image_file=image"])
        res = [x for x in str(s2_out, 'utf-8').split('\n') if len(x) > 1]
        obj['res'] = []

        for val in res:
            each = val.split("(")
            eachObj = {
                'class': [x.strip() for x in each[0].split(',')],
                'score': parse_score(each[1])
            }
            obj['res'].append(eachObj)
        return obj

api.add_resource(ImgRec, '/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
