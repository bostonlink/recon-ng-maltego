#!/usr/bin/env python
from canari.maltego.entities import Person, Phrase
from common.reconng import db_connect, get_contacts
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
    label='To Title [recon-ng]',
    description='Returns Title of person',
    uuids=[ 'recon-ng-maltego.v2.FullnameToTitle' ],
    inputs=[ ( 'Recon-ng', Person ) ],
    remote=False,
    debug=True
)

def dotransform(request, response, config):

    if 'workspace' in request.fields:
        workspace = request.fields['workspace']
    else:
        workspace = request.value

    e = Phrase(request.fields["title"].decode('ascii'))
    e += Field("workspace", workspace, displayname='Workspace')
    e += Field("fullname", request.value, displayname='Fullname', matchingrule='loose')
    response += e

    return response
