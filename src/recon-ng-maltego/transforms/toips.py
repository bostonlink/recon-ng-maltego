#!/usr/bin/env python

from canari.maltego.entities import IPv4Address, Domain
from common.entities import Workspace
from common.reconng import db_connect, get_hosts
from canari.framework import configure
from canari.maltego.message import Field, MatchingRule

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
    label='To IP Addresses [recon-ng]',
    description='Returns IP addresses from the recon-ng workspace',
    uuids=[ 'recon-ng-maltego.v2.DomainToIPs',
            'recon-ng-maltego.v2.WorkspaceToIps' ],
    inputs=[ ( 'Recon-ng', Domain ),
             ( 'Recon-ng', Workspace ) ],
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

    for ip in host_list:
        if ip[0] == request.value:
            e = IPv4Address(ip[1])
            e += Field("workspace", workspace, displayname='Workspace')
            e += Field("domainname", request.value, displayname='Domain Name')
            response += e
        else:
            e = IPv4Address(ip[1])
            e += Field("workspace", workspace, displayname='Workspace')
            response += e

    return response
