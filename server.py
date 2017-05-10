#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
from flask import Flask, request, jsonify
from sentiment import Sentiment
from flask_cors import CORS

logger = logging.getLogger('marlowe.usent.server')

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def index():
    text = request.form.get('text')
    if text is not None:
        sentiment = Sentiment()
        text = str(request.form.get('text').encode("utf8")).strip()
        objectivity = float(sentiment.get_objectivity(text)) / 100
        data = {'objectivity': round(objectivity, 2)}
    else:
        data = {'objectivity': 1.0}
    return jsonify(data)


if __name__ == '__main__':
    debug = os.environ.get('DEBUG')
    if debug is not None:
        debug = True
    else:
        debug = False
    app.run(debug=debug, host='0.0.0.0')
