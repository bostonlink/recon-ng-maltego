#!/usr/bin/env python

from canari.maltego.entities import Domain, IPv4Address
from common.entities import Workspace
from canari.maltego.message import Field
from common.reconng import db_connect, get_hosts
from canari.framework import configure

__author__ = 'David Bressler (@bostonlink), GuidePoint Security, LLC.'
__copyright__ = 'Copyright 2013, Recon-ng-maltego Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'David Bressler (@bostonlink), GuidePoint Security, LLC.'
__email__ = 'david.bressler@guidepointsecurity.com'
__status__ = 'Development'

__all__ = [
    'dotransform',
]

@configure(
    label='To Hostnames [recon-ng]',
    description='Returns all domain names within a selected workspace',
    uuids=[ 'recon-ng-maltego.v2.WorkspaceToHostnames',
            'recon-ng-maltego.v2.IPToHostnames' ],
    inputs=[ ( 'Recon-ng', Workspace ),
             ( 'Recon-ng', IPv4Address) ],
    remote=False,
    debug=True
)

def dotransform(request, response, config):

    if 'workspace' in request.fields:
        workspace = request.fields['workspace']
    else:
        workspace = request.value

    dbcon = db_connect(workspace)
    host_list = get_hosts(dbcon)

    for host in host_list:
        e = Domain(host[0])
        e += Field("workspace", workspace, displayname='Workspace')
        response += e

    return response
