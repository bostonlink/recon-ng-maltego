#!/usr/bin/env python

from canari.maltego.entities import Domain
from canari.maltego.message import Field
from common.reconng import db_connect, get_hosts
from common.rng_launch import hosts_gather, hosts_enum, hosts_geo
from canari.framework import configure
from common.entities import Workspace

# from canari.maltego.message import Label

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
    label='Launch Hosts Recon [recon-ng]',
    description='Launches recon-ng and gathers hosts and ouputs all hostnames as a Domain entity',
    uuids=[ 'recon-ng-maltego.v2.GatherHosts' ],
    inputs=[ ( 'Launch Recon-ng', Workspace ) ],
    remote=False,
    debug=True
)


def dotransform(request, response, config):

    hosts_gather(request.value)
    hosts_enum(request.value)
    hosts_geo(request.value)

    dbcon = db_connect(request.value)
    host_list = get_hosts(dbcon)

    for host in host_list:
        e = Domain(host[0])
        e += Field("workspace", request.value, displayname='Workspace')
        response += e

    return response
