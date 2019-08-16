#!/bin/bash

export FLASK_ENV=production
waitress-serve --port 5000 --host 127.0.0.1 app:app
