#!/usr/bin/env python

from canari.maltego.entities import Image, Location
from canari.maltego.message import Field, Label
from common.reconng import db_connect, get_pushpin
from canari.framework import configure
from common.entities import Workspace, PicasaPin

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
    label='To Pushpin Picasa [recon-ng]',
    description='Returns Picasa images as an Image entity',
    uuids=[ 'recon-ng-maltego.v2.PushpinPicasaWorkspace',
            'recon-ng-maltego.v2.PushpinPicasaPicasaPin' ],
    inputs=[ ( 'Recon-ng', Workspace ),
             ( 'Recon-ng', PicasaPin ) ],
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

    for puser in pushpin_list:
        if 'Picasa' == puser[0]:
            e = Image(puser[6],
                      url=puser[4])
            e += Field("workspace", workspace, displayname='Workspace')
            e += Label('Picasa Profile User', puser[2])
            e += Label('Picasa Profile URL', puser[3])
            e += Label('Published Date', puser[9])
            response += e

    return response
