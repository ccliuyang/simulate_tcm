# -*- coding: utf-8 -*-

import datetime
import os
from gevent import pywsgi
from flask import Flask, g, request
from flask_restful import Api
import atexit
import yaml
import codecs

from . import log


app = Flask(__name__)
api = Api(app)


def on_exit():
    log.logger.info('stopping simulate_tcm server')
    log.logger.info('simulate_tcm server stopped')


def start(debug=True, port=500, autoreload=False):
    pass

