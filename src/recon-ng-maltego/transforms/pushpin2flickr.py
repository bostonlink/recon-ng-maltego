#!/usr/bin/env python

from canari.maltego.entities import Image
from canari.maltego.message import Field, Label
from common.reconng import db_connect, get_pushpin
from canari.framework import configure
from common.entities import Workspace, FlickrPin

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
    label='To Pushpin Flickr [recon-ng]',
    description='Returns Picasa images as an Image entity',
    uuids=[ 'recon-ng-maltego.v2.PushpinFlickrWorkspace',
            'recon-ng-maltego.v2.PushpinFlickrFlickrPin' ],
    inputs=[ ( 'Recon-ng', Workspace ),
             ( 'Recon-ng', FlickrPin ) ],
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

    for fuser in pushpin_list:
        if 'Flickr' == fuser[0]:
            e = Image(fuser[6],
                      url=fuser[4])
            e += Field("workspace", workspace, displayname='Workspace')
            e += Label('Flickr Username', fuser[1])
            e += Label('Flickr Profile User', fuser[2])
            e += Label('Picasa Profile URL', fuser[3])
            e += Label('Published Date', fuser[9])
            response += e

    return response
