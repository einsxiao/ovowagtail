#!/bin/sh
rm -r build
django-admin compilemessages
python setup.py build
python setup.py install
