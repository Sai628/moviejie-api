#!/bin/bash
set -e

cp ./etc/supervisor/moviejie_api.conf /etc/supervisor/conf.d/moviejie_api.conf
supervisord -c /etc/supervisor/supervisord.conf
nginx -s reload
