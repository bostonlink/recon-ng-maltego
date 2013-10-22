#!/usr/bin/env python

from canari.maltego.entities import IPv4Address
from canari.maltego.message import Field, Label
from common.reconng import db_connect, get_pushpin
from canari.framework import configure
from common.entities import Workspace, ShodanPin

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
    label='To Pushpin Shodan [recon-ng]',
    description='Returns Shodan results as an IPv4Address entity',
    uuids=[ 'recon-ng-maltego.v2.PushpinShodanWorkspace',
            'recon-ng-maltego.v2.PushpinShodanPicasaPin' ],
    inputs=[ ( 'Recon-ng', Workspace ),
             ( 'Recon-ng', ShodanPin ) ],
    remote=False,
    debug=True
)


def dotransform(request, response, config):

    if 'workspace' in request.fields:
        workspace = request.fields['workspace']
    else:
        workspace = request.value

    dbcon = db_connect(workspace)
    pushpin_list = get_pushpin(dbcon)

    for shost in pushpin_list:
        if 'Shodan' == shost[0]:
            ipsplit = shost[1].split(":")
            e = IPv4Address(ipsplit[0])
            e += Field("workspace", workspace, displayname='Workspace')
            e += Field("port", ipsplit[1], displayname='Port')
            e += Field("hostname", shost[6], displayname='Hostname')
            e += Label('Shodan Query', shost[4])
            e += Label('Hostname', shost[6])
            e += Label('Published Date', shost[9])
            response += e

    return response
