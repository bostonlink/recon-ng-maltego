#!/usr/bin/env python
from canari.maltego.entities import Person
from common.entities import Workspace
from common.reconng import db_connect, get_contacts
from canari.framework import configure
from canari.maltego.message import Field, Label

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
    label='To Fullname [recon-ng]',
    description='Returns Fullnames (first, last) from the recon-ng workspace',
    uuids=[ 'recon-ng-maltego.v2.WorkspaceToFullname' ],
    inputs=[ ( 'Recon-ng', Workspace ) ],
    remote=False,
    debug=True
)

def dotransform(request, response, config):

    if 'workspace' in request.fields:
        workspace = request.fields['workspace']
    else:
        workspace = request.value

    dbcon = db_connect(workspace)
    contact_list = get_contacts(dbcon)

    for fullname in contact_list:
        if fullname[0] is None or fullname[1] is None:
            pass
        else:
            e = Person(fullname[0] + ' ' + fullname[1])
            e += Field("workspace", workspace, displayname='Workspace')
            e += Field("fname", fullname[0], displayname='First Name')
            e += Field("lname", fullname[1], displayname='Last Name')
            e += Field("title", fullname[3], displayname='Title')
            e += Field("location", fullname[4] + ', ' + fullname[5], displayname='Location')
            e += Label("Title", fullname[3])
            e += Label("Location", fullname[4] + ', ' + fullname[5])
            response += e

    return response
