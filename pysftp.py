# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:35:25 2018
@author: sawid
"""
#How to push files to a server
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:34:59 2018
@author: sawid
"""

import Crypto
import paramiko as pm
import pysftp
cnopts = pysftp.CnOpts()
#cnopts.hostkeys = None
def connect(filename):
    with pm.SSHClient() as client:
        client.set_missing_host_key_policy(pm.AutoAddPolicy())
        client.connect(
            'servername',
            port=number,
            username='usrname',
            password='pass'
        )
        with client.open_sftp() as sftp:
            dir=sftp.listdir()
            print(dir)
            #sftp.put(str(local_path)+str(file), str(file))
            #print(filename, local_path)
            #sftp.get(str(filename),str(local_path)+str(filename))
            #sftp.remove(str(filename))
            sftp.close()
    return filename 



connect('file.csv')      