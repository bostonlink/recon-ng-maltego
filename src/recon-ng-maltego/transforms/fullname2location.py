#!/usr/bin/env python
from canari.maltego.entities import Person, Location
from canari.framework import configure
from canari.maltego.message import Field

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
    description='Returns Location of person',
    uuids=[ 'recon-ng-maltego.v2.FullnameToLocation' ],
    inputs=[ ( 'Recon-ng', Person ) ],
    remote=False,
    debug=True
)

def dotransform(request, response, config):

    if 'workspace' in request.fields:
        workspace = request.fields['workspace']
    else:
        workspace = request.value

    e = Location(request.fields["location"].decode('ascii'))
    e += Field("workspace", workspace, displayname='Workspace')
    response += e

    return response
