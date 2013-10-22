#!/usr/bin/env python

from canari.maltego.entities import Location
from canari.maltego.message import Field
from common.reconng import db_connect, get_pushpin
from common.rng_launch import run_pushpin
from canari.framework import configure
from canari.easygui import multenterbox
from common.entities import Workspace, TwitterPin, ShodanPin, PicasaPin, FlickrPin

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
    label='Launch Pushpin Recon [recon-ng]',
    description='Launches recon-ng and runs pushpin modules',
    uuids=[ 'recon-ng-maltego.v2.PushpinReconWorkspace',
            'recon-ng-maltego.v2.PushpinReconLocation' ],
    inputs=[ ( 'Launch Recon-ng', Workspace ),
             ( 'Launch Recon-ng', Location ) ],
    remote=False,
    debug=True
)


def dotransform(request, response, config):

    if 'workspace' in request.fields:
        workspace = request.fields['workspace']
        latitude = request.fields['latitude']
        longitude = request.fields['longitude']
    else:
        workspace = request.value
        msg = "Enter Latitude and Longitude"
        title = "Coordinates to Query for Pushpin"
        fieldNames = ["Latitude", "Longitude"]
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

        latitude = fieldValues[0]
        longitude = fieldValues[1]

    run_pushpin(workspace, latitude, longitude)

    dbcon = db_connect(request.value)
    pushpin_list = get_pushpin(dbcon)

    for pin in pushpin_list:
        if 'Twitter' == pin[0]:
            e = TwitterPin(pin[0])
            e += Field("workspace", workspace, displayname='Workspace')
            response += e
        elif 'Shodan' == pin[0]:
            e = ShodanPin(pin[0])
            e += Field("workspace", workspace, displayname='Workspace')
            response += e
        elif 'Picasa' == pin[0]:
            e = PicasaPin(pin[0])
            e += Field("workspace", workspace, displayname='Workspace')
            response += e
        elif 'Flickr' == pin[0]:
            e = FlickrPin(pin[0])
            e += Field("workspace", workspace, displayname='Workspace')
            response += e

    return response
