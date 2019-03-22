# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:45:06 2019

@author: leslie
"""

#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
import LRUCache 

app = Flask(__name__)

cacheCapacity = 2

cache = LRUCache.LRUCache(cacheCapacity)            
#cache.put(1,400)
#cache.put(2,800)


@app.route('/cache.service/api/v1.0/get/<int:key>', methods=['GET'])
def get_value(key):
    value = cache.get(key)
    if value is None:
        abort(404)
    return jsonify({'key':key, 'value': value})

@app.route('/cache.service/api/v1.0/put/<int:key>', methods=['PUT'])
def put_value(key):
    if 'value' in request.json and type(request.json['value']) != int:
        abort(400)
    value = request.json.get('value')
    #print("we got",key,value)
    ret = cache.put(key,value)
    if ret is None:
        return make_response(jsonify({}),202)
    else:
        return make_response(jsonify({'key':ret[0], 'value': ret[1]}),202)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)