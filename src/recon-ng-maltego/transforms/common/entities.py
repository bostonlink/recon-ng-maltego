#!/usr/bin/env python

from canari.maltego.message import Entity, EntityField

__author__ = 'David Bressler (@bostonlink), GuidePoint Security, LLC.'
__copyright__ = 'Copyright 2013, Recon-ng-maltego Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'David Bressler (@bostonlink), GuidePoint Security, LLC.'
__email__ = 'david.bressler@guidepointsecurity.com'
__status__ = 'Development'

__all__ = [
    'ReconngmaltegoEntity',
    'Reconng',
    'Workspace'
]


class ReconngmaltegoEntity(Entity):
    _namespace_ = 'recon-ng-maltego'


"""
You can specify as many entity fields as you want by just adding an extra @EntityField() decorator to your entities. The
@EntityField() decorator takes the following parameters:
    - name: the name of the field without spaces or special characters except for dots ('.') (required)
    - propname: the name of the object's property used to get and set the value of the field (required, if name contains dots)
    - displayname: the name of the entity as it appears in Maltego (optional)
    - type: the data type of the field (optional, default: EntityFieldType.String)
    - required: whether or not the field's value must be set before sending back the message (optional, default: False)
    - choices: a list of acceptable field values for this field (optional)
    - matchingrule: whether or not the field should be loosely or strictly matched (optional, default: MatchingRule.Strict)
    - decorator: a function that is invoked each and everytime the field's value is set or changed.
    - is_value: a boolean value that determines whether the field is also the default value of the entity object.
TODO: define as many custom fields and entity types as you wish:)
"""


class Reconng(ReconngmaltegoEntity):
    pass


@EntityField(name='recon-ng-maltego.cname', propname='cname', displayname='Company Name')
@EntityField(name='recon-ng-maltego.domain', propname='domain', displayname='Domain')
class Workspace(ReconngmaltegoEntity):
    pass

@EntityField(name='recon-ng-maltego.workspace', propname='workspace', displayname='Workspace')
class TwitterPin(ReconngmaltegoEntity):
    pass

@EntityField(name='recon-ng-maltego.workspace', propname='workspace', displayname='Workspace')
class ShodanPin(ReconngmaltegoEntity):
    pass

@EntityField(name='recon-ng-maltego.workspace', propname='workspace', displayname='Workspace')
class PicasaPin(ReconngmaltegoEntity):
    pass

@EntityField(name='recon-ng-maltego.workspace', propname='workspace', displayname='Workspace')
class FlickrPin(ReconngmaltegoEntity):
    pass
