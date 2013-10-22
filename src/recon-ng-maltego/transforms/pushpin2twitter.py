#!/usr/bin/env python

from canari.maltego.entities import Twitter, Location
from canari.maltego.message import Field
from common.reconng import db_connect, get_pushpin
from canari.framework import configure
from common.entities import Workspace, TwitterPin

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
    label='To Pushpin Twitter [recon-ng]',
    description='Returns found twitter users as an affiliation twitter entity',
    uuids=[ 'recon-ng-maltego.v2.PushpinTwitterWorkspace',
            'recon-ng-maltego.v2.PushpinTwitterLocation',
            'recon-ng-maltego.v2.PushpinTwitterTwitterPin' ],
    inputs=[ ( 'Recon-ng', Workspace ),
             ( 'Recon-ng', Location ),
             ( 'Recon-ng', TwitterPin ) ],
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

    for tuser in pushpin_list:
        if 'Twitter' == tuser[0]:
            e = Twitter(tuser[1],
                        screenname=tuser[2],
                        profile_url=tuser[3])
            e += Field("workspace", workspace, displayname='Workspace')
            response += e

    return response
