from flask import json
from flask import Response
from flask import request
from flask_cors import CORS
from flask_api import FlaskAPI
import os

app = FlaskAPI(__name__)
CORS(app) # Required if the client is browser, else returns cross origin requests errors

# GET Function to get data from a file
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

# POST Function to upload images to the server
@app.route("/uploadFiles/", methods=['POST'])
def upload_file():
    
    response_dict = {}
    error_files = ''
    new_filename = ''

    try:
        new_filename = request.form['filename']
        recieved_files = request.files.getlist('files_list')
        for each_file in recieved_files:
            each_file_name = each_file.filename
            
            try:
                each_file.save(os.path.join('.', new_filename + each_file_name.replace(" ", "")))
            
            except RuntimeError as err:
                print('Error in saving file %s: %s', each_file.filename, err)
                error_files = error_files + ',' + each_file.filename
        
        response_dict['status'] = True
        response_dict['error_list'] = error_files
        js_dump = json.dumps(response_dict)
        
        resp = Response(js_dump, status=200, mimetype='application/json')

    except RuntimeError:
        response_dict = {'error': 'error on server side', 'filename':request.form['filename']}
        js_dump = json.dumps(response_dict)
        
        resp = Response(js_dump, status=200, mimetype='application/json')
    
    return resp        


if __name__=='__main__':
    app.run(port=5000, threaded=True, debug=True)