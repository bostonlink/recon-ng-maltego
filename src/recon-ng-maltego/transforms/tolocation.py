#!/usr/bin/env python

from canari.maltego.entities import IPv4Address, Domain, Location
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
    label='To Location [recon-ng]',
    description='Returns IP address and/or domain name locations from the recon-ng workspace',
    uuids=[ 'recon-ng-maltego.v2.DomainToLocation',
            'recon-ng-maltego.v2.IPToLocation' ],
    inputs=[ ( 'Recon-ng', Domain ),
             ( 'Recon-ng', IPv4Address ) ],
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

    for loc in host_list:
        if loc[0] == request.value or loc[1] == request.value:
            e = Location(loc[2] + ', ' + loc[3],
                          latitude=float(loc[4]),
                          longitude=float(loc[5]))
            e += Field("workspace", workspace, displayname='Workspace')
            response += e

    return response
