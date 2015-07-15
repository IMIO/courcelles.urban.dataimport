# -*- coding: utf-8 -*-

from courcelles.urban.dataimport.notaries.mappers import AddressMapper
from courcelles.urban.dataimport.notaries.mappers import IdMapper
from courcelles.urban.dataimport.notaries.mappers import NotaryFactory

from imio.urban.dataimport.access.mapper import AccessSimpleMapper as SimpleMapper


OBJECTS_NESTING = [
    ('NOTARY', [],),
]

FIELDS_MAPPINGS = {
    'NOTARY':
    {
        'factory': [NotaryFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'NOM',
                    'to': 'name1',
                },
                {
                    'from': 'codepost',
                    'to': 'zipcode',
                },
                {
                    'from': 'localite',
                    'to': 'city',
                },
                {
                    'from': 'adressemail',
                    'to': 'email',
                },
                {
                    'from': 'tel',
                    'to': 'phone',
                },
                {
                    'from': 'fax',
                    'to': 'fax',
                },
            ),

            IdMapper: {
                'from': 'NOM',
                'to': 'id',
            },

            AddressMapper: {
                'from': 'rue',
                'to': ('street', 'number')
            },
        },
    },
}
