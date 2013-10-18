#!/usr/bin/env python

from common.rng_launch import create_workspace, set_domain, set_company, set_radius
from canari.framework import configure
from canari.easygui import multenterbox
from common.entities import Workspace, Reconng

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
    label='Create Workspace [recon-ng]',
    description='Creates the specified workspace as a workspace entity',
    uuids=[ 'recon-ng-maltego.v2.CreateWorkspace' ],
    inputs=[ ( 'Launch Recon-ng', Reconng ) ],
    remote=False,
    debug=True
)


def dotransform(request, response, config):
    msg = "Workspace Configuration"
    title = "Workspace Confguration"
    fieldNames = ["Workspace Name", "Company Name", "Domain", "Radius"]
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

    create_workspace(fieldValues[0])
    set_domain(fieldValues[0], fieldValues[2])
    set_company(fieldValues[0], fieldValues[1])
    set_radius(fieldValues[0], fieldValues[3])

    e = Workspace(fieldValues[0],
                  cname=fieldValues[1],
                  domain=fieldValues[2])

    response += e
    return response
