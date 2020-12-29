#!/bin/bash
source /home/www/project_pikket/env/bin/activate
exec gunicorn -c "/home/www/project_pikket/gunicorn_config.py" pikket.wsgi
