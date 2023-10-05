#!/usr/bin/python3
"""create a .tgz archive from contents of the web_static"""
from fabric.api import local, task, put, run, env
from datetime import datetime
import os


@task
def do_pack():
    """pack web_static folder"""
    try:
        cur_date = datetime.now().strftime('%Y%m%d%H%M%S')
        arch = f'web_static_{cur_date}.tgz web_static'
        local('mkdir -p versions')
        local(f'tar -cvzf versions/{arch}')
        return 'versions/'
    except Exception:
        return None


@task
def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    env.hosts = ['54.89.27.151', '18.209.225.187']
    file_name = archive_path.split('/')[-1].split('.')[0]
    if not os.path.exists(archive_path):
        return False
    try:
        for host in env.hosts:
            env.host_string = host
            put(archive_path, '/tmp/')
            run(f'mkdir -p /data/web_static/releases/{file_name}')
            run(f'tar -xzf /tmp/{file_name}.tgz data/web_static/releases/ \
            {file_name} -C /data/web_static/releases/{file_name}/')
            run(f'rm /tmp/{file_name}.tgz')
            run(f'mv /data/web_static/releases/{file_name}/web_static/* \
            /data/web_static/releases/{file_name}/')
            run(f'rm -rf /data/web_static/releases/{file_name}/web_static')
            run('rm -rf /data/web_static/current')
            run(f'ln -s /data/web_static/releases/{file_name}/ \
            /data/web_static/current')
            print('New version deployed!')
    except Exception:
        return False
    return True
