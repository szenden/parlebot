'''Controller and routes for file downloads'''
import os
import sys
from flask import request, jsonify
from app import app, mongo
import logger
import datetime
from app.helpers.kamervragen import scrap_link

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))

@app.route('/download', methods=['GET', 'POST', 'DELETE'])
def download():
    if request.method == 'GET':
        query = request.args
        data = mongo.db.downloads.find_one(query)
        return jsonify(data), 200

    data = request.get_json()
    if request.method == 'POST':
        if data.get('url', None) is not None and data.get('query', None) is not None: 
            # data.set('insertDate',datetime.datetime.now())          
            _id = mongo.db.downloadQuery.insert_one(data)
            #Todo: download class
            data = scrap_link(data.get('url'), data.get('query'), mongo, _id.inserted_id)
            #_id.inserted_id
            return jsonify({'ok': True, 'message': 'Downloads created successfully!', 'objectId': _id.inserted_id,'content': data}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'DELETE':
        if data.get('fileId', None) is not None:
            db_response = mongo.db.downloads.delete_one({'fileId': data['fileId']})
            if db_response.deleted_count == 1:
                response = {'ok': True, 'message': 'record deleted'}
            else:
                response = {'ok': True, 'message': 'no record found'}
            return jsonify(response), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400
