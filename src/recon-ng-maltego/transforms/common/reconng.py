#!/usr/bin/env python

import os
import os.path
import sqlite3
import json
from canari.easygui import choicebox
from canari.config import config
from canari.maltego.message import MaltegoException

__author__ = 'David Bressler (@bostonlink), GuidePoint Security, LLC.'
__copyright__ = 'Copyright 2013, Recon-ng-maltego Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'David Bressler (@bostonlink), GuidePoint Security, LLC.'
__email__ = 'david.bressler@guidepointsecurity.com'
__status__ = 'Development'
#workspace_path = os.path.join(config['recon-ng/reconng_path'],'workspaces')


def pick_workspace():
    """displays a list of recon-ng workspaces within the maltego gui to choose
    fromand returns the workspace selected"""

    workspace_path = os.path.join(config['recon-ng/reconng_path'],
                                  'workspaces')

    for p, d, f in os.walk(workspace_path):
        if len(d) > 0:
            msg = "Pick a recon-ng workspace"
            title = "Recon-ng Workspaces"
            return choicebox(msg, title, choices=d)
        else:
            MaltegoException("No valid workspaces selcted or detected")


def db_connect(workspace):
    """connect to the recon-ng workspace database and return the connection
    object"""

    workspace_p = os.path.join(config['recon-ng/reconng_path'],
                               'workspaces')

    db = os.path.join(workspace_p, workspace + '/data.db')
    return sqlite3.connect(db)


def get_config(workspace):
    """returns config dic containing:
    proxy_server
    verbose
    rec_file
    socket_timeout
    company
    domain
    longitude
    user-agent
    latitude
    radius
    proxy
    workspace
    debug"""

    workspace_p = os.path.join(config['recon-ng/reconng_path'],
                               'workspaces')

    workspace_conf_path = os.path.join(workspace_p, workspace + '/config.dat')
    f = open(workspace_conf_path, 'r')
    workspace_conf = json.loads(f.read())
    f.close()
    return workspace_conf


def get_hosts(dbcon):
    """connects to db and returns a list of rows from the host table"""

    with dbcon:
        cur = dbcon.cursor()
        cur.execute("SELECT * FROM hosts")
        return cur.fetchall()


def get_contacts(dbcon):
    """connects to db and returns a list of rows from the contacts table"""

    with dbcon:
        cur = dbcon.cursor()
        cur.execute("SELECT * FROM contacts")
        return cur.fetchall()


def get_creds(dbcon):
    """connects to db and returns a list of rows from the creds table"""

    with dbcon:
        cur = dbcon.cursor()
        cur.execute("SELECT * FROM creds")
        return cur.fetchall()


def get_pushpin(dbcon):
    """connects to db and returns a list of rows from the pushpin table"""

    with dbcon:
        cur = dbcon.cursor()
        cur.execute("SELECT * FROM pushpin")
        return cur.fetchall()

#workspace = pick_workspace()
#get_config(workspace)
