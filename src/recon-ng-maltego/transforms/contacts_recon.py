#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.message import Field, Label
from canari.easygui import multenterbox
from common.reconng import db_connect, get_contacts
from common.rng_launch import contacts_gather, contacts_enum, contacts_mangle
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
    label='Launch Contacts Recon [recon-ng]',
    description='Launches recon-ng and gathers recon on contacts and ouputs all to a person',
    uuids=[ 'recon-ng-maltego.v2.ContactsRecon' ],
    inputs=[ ( 'Launch Recon-ng', Workspace ) ],
    remote=False,
    debug=True
)


def dotransform(request, response, config):
    workspace = request.value
    contacts_gather(workspace)
    contacts_enum(workspace)
    msg = "Contact Mangle to Create Email addresses enter <fn>.<ln>, etc"
    title = "Mangle Contacts to Emails"
    fieldNames = ["Pattern"]
    fieldValues = []
    fieldValues = multenterbox(msg, title, fieldNames)

    while 1:
        if fieldValues is None:
            break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg += ('"%s" is a required field.\n\n' % fieldNames[i])
        if errmsg == "":
            break  # no problems found
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)

    contacts_mangle(workspace, fieldValues[0])

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
            e += Field("location", str(fullname[4]) + ', ' + str(fullname[5]), displayname='Location')
            e += Label("Title", fullname[3])
            e += Label("Location", str(fullname[4]) + ', ' + str(fullname[5]))
            response += e

    return response
