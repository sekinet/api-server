# -*- coding: utf-8 -*-
from flask import Flask, jsonify, make_response
import time

DELAY_TIME=1

api = Flask(__name__)

@api.route('/virtual-network/rintaro', methods=['GET'])
def get_virtual_network():
    result = {
        "vmi":"UP", 
        "version":2
        }

    time.sleep(DELAY_TIME)
    return make_response(jsonify(result))

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)
