#!/bin/bash
pip3 uninstall kyoho
python3 ./setup.py develop

tail -f /dev/null # or sleep infinity
