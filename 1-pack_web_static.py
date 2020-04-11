#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the 
contents of the web_static folder of your AirBnB Clone repo, usingthe function do_pack
"""
from datetime import datetime
from fabric.api import *

def do_pack():
    """
    generate a pack of .tgz files
    """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(file))
    return file
    
    
