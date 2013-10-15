#!/usr/bin/env python
from canari.maltego.entities import Person, EmailAddress
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
    label='To Email Address [recon-ng]',
    description='Returns email addresses from names',
    uuids=[ 'recon-ng-maltego.v2.FullnameToEmails' ],
    inputs=[ ( 'Recon-ng', Person ) ],
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

    for email in contact_list:
        if email[0] == request.fields["fname"] and email[1] == request.fields["lname"]:
            e = EmailAddress(email[2])
            e += Field("workspace", workspace, displayname='Workspace')
            e += Field("fullname", email[0] + ' ' + email[1], displayname='Fullname')
            response += e
        else:
            pass

    return response
