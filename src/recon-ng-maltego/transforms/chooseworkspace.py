#!/usr/bin/env python

from common.reconng import pick_workspace, get_config
from canari.framework import configure
from common.entities import Workspace, Reconng
from canari.maltego.message import Label

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
    label='To Workspace [recon-ng]',
    description='Returns the selected workspace in a workspace entity',
    uuids=[ 'recon-ng-maltego.v2.ToWorkspace' ],
    inputs=[ ( 'Recon-ng', Reconng ) ],
    remote=False,
    debug=True
)

def dotransform(request, response, config):
    workspace = pick_workspace()
    workspace_config = get_config(workspace)

    e = Workspace(workspace,
                  cname=workspace_config["company"]["value"],
                  domain=workspace_config["domain"]["value"])

    #e += Label("Company Name", workspace_config["company"]["value"])
    #e += Label("Domain Name", domain=workspace_config["domain"]["value"])

    response += e
    return response
