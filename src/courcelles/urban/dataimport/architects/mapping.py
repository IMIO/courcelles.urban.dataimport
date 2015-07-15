# -*- coding: utf-8 -*-

from courcelles.urban.dataimport.architects.mappers import ArchitectFactory
from courcelles.urban.dataimport.architects.mappers import IdMapper
from courcelles.urban.dataimport.architects.mappers import PhoneMapper

from imio.urban.dataimport.mapper import SimpleMapper


OBJECTS_NESTING = [
    ('ARCHITECT', [],),
]

FIELDS_MAPPINGS = {
    'ARCHITECT':
    {
        'factory': [ArchitectFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'nom',
                    'to': 'name1',
                },
                {
                    'from': 'prénom',
                    'to': 'name2',
                },
                {
                    'from': 'société',
                    'to': 'society',
                },
                {
                    'from': 'adresse',
                    'to': 'street',
                },
                {
                    'from': 'numéro',
                    'to': 'number',
                },
                {
                    'from': 'cp',
                    'to': 'zipcode',
                },
                {
                    'from': 'ville',
                    'to': 'city',
                },
                {
                    'from': 'mail',
                    'to': 'email',
                },
                {
                    'from': 'fax',
                    'to': 'fax',
                },
            ),

            IdMapper: {
                'from': 'nom',
                'to': 'id',
            },

            PhoneMapper: {
                'from': ('téléphone', 'gsm'),
                'to': 'phone',
            },
        },
    },
}
