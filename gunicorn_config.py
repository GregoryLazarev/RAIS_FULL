command = '/home/www/project_pikket/env/bin/gunicorn'
pythonpath = '/home/www/project_pikket/pikket'
bind = '127.0.0.1:8000'
workers = 5
user = 'user'
limit_request_fields = 32000
limit_request_fields_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=pikket.settings'
