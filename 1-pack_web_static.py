#!/usr/bin/python3
""" 
a Fabric script that generates a .tgz archive from
the contents of the web_static folder of your 
AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import *
from datetime import datetime
import os

def do_pack():
    
    local('sudo mkdir -p versions')

    time = datetime.now()
    time_str = time.strftime('%Y%m%d%H%M%S')

    local(f'sudo tar -cvzf versions/web_static_{time_str}.tgz web_static')

    file_path = f"versions/web_static_{time_str}.tgz"
    file_size = os.path.getsize(file_path)
    print(f"web_static packed: {file_path} -> {file_size}Bytes")
