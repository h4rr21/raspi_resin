#!/bin/sh

# Test scripts
python ping-script-facebook.py &
python ping-script-google.py &

# Run flask app
python hello.py