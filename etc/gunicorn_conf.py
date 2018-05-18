# Gunicorn configuration file.
# http://docs.gunicorn.org/en/0.16.0/configure.html


import multiprocessing

bind = '127.0.0.1:5001'
backlog = 2048  # The maximum number of pending connections

workers = multiprocessing.cpu_count() * 2 + 1
worker_connections = 10240  # The maximum number of simultaneous clients. This setting only affects the Eventlet and Gevent worker types.
max_requests = 10240  # The maximum number of requests a worker will process before restarting.
keepalive = 2  # The number of seconds to wait for requests on a Keep-Alive connection

secure_scheme_headers = {
    'X-SCHEME': 'https',
}
x_forwarded_for_header = 'X-Forwarded-For'

loglevel = 'info'
accesslog = '/var/log/moviejie-api/gunicorn_stdout.log'
errorlog = '/var/log/moviejie-api/gunicorn_stdout.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%({X-Real-IP}i)s"'

reload = True  # Restart workers when code changes
