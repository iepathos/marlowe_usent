#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
from flask import Flask, request, jsonify
from sentiment import Sentiment
logger = logging.getLogger('marlowe.objectivity.server')

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    sentiment = Sentiment()
    text = str(request.form.get('text'))
    objectivity = float(sentiment.get_objectivity(text)) / 100
    data = {'objectivity': round(objectivity, 2)}
    return jsonify(data)


if __name__ == '__main__':
    debug = os.environ.get('DEBUG')
    if debug is not None:
        debug = True
    else:
        debug = False
    app.run(debug=debug, host='0.0.0.0')
