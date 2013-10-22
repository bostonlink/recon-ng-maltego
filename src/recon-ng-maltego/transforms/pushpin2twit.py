#!/usr/bin/env python

from canari.maltego.entities import Twitter, Location, Twit
from canari.maltego.message import Field
from common.reconng import db_connect, get_pushpin
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
    label='To Pushpin Twit [recon-ng]',
    description='Returns found tweets per twitter user as an affiliation twit entity',
    uuids=[ 'recon-ng-maltego.v2.PushpinTwit' ],
    inputs=[ ( 'Recon-ng', Twitter ) ],
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
        if request.value == tuser[1] and 'Twitter' == tuser[0]:
            e = Twit(tuser[6],
                     author=tuser[1],
                     img_link=tuser[5],
                     author_uri=tuser[4],
                     pubdate=tuser[9])
            e += Field("workspace", workspace, displayname='Workspace')
            response += e

    return response
