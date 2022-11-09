#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/deploiement-flask/")

from app import app
app.secret_key = 'something super SUPER secret'
