# Gunicorn configuration file.
# http://docs.gunicorn.org/en/0.16.0/configure.html


import multiprocessing

bind = '127.0.0.1:5001'
backlog = 2048

workers = multiprocessing.cpu_count() * 2 + 1
worker_connections = 1024
max_requests = 10240
keepalive = 2

loglevel = 'info'
accesslog = '/var/log/moviejie-api/gunicorn_stdout.log'
errorlog = '/var/log/moviejie-api/gunicorn_stdout.log'

secure_scheme_headers = {
    'X-SCHEME': 'https',
}
x_forwarded_for_header = 'X-FORWARDED-FOR'

reload = True  # Restart workers when code changes