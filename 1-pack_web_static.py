#!/usr/bin/python3
"""create a .tgz archive from contents of the web_static"""
from fabric.api import local, task
from datetime import datetime


@task
def do_pack():
    """pack web_static folder"""
    try:
        cur_date = datetime.now().strftime('%Y%m%d%H%M%S')
        arch = f'web_static_{cur_date}.tgz'
        local('mkdir -p versions')
        local(f'tar -cvzf versions/{arch} web_static')
        return f'versions/{arch}'
    except Exception:
        return None
