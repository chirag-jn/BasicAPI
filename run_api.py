from flask import json
from flask import Response
from flask_cors import CORS
from flask_api import FlaskAPI

app = FlaskAPI(__name__)
CORS(app)

@app.route("/get/<filename>", methods=['GET'])
def get_response(filename):

    labels_dict = {}
    response_dict = {}
    
    try:
        with open(filename, 'r') as labels:
            labels_dict = json.load(labels)
        
        response_dict['status'] = True
        response_dict['labels_mapping'] = labels_dict
        js_dump = json.dumps(response_dict)
        resp = Response(js_dump, status=200, mimetype='application/json')

    except FileNotFoundError:
        response_dict = {'error': 'file not found'}
        js_dump = json.dumps(response_dict)
        resp = Response(js_dump, status=500, mimetype='application/json')

    except RuntimeError:
        response_dict = {'error': 'error occured on server'}
        js_dump = json.dumps(response_dict)
        resp = Response(js_dump, status=500, mimetype='application/json')

    return resp

if __name__=='__main__':
    app.run(port=5000, threaded=True, debug=True)