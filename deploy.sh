#!/bin/bash
set -e

cp ./etc/supervisor/moviejie_api.conf /etc/supervisor/conf.d/moviejie_api.conf
supervisord -c /etc/supervisor/supervisord.conf
supervisorctl start moviejie_api
nginx -s reload
