#!/bin/sh
rm -r build
rm -r ~/ovoenv/lib/python3.5/site-packages/wagtail-2*
django-admin compilemessages
python setup.py build
python setup.py install
