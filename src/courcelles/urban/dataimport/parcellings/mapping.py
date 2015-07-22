# -*- coding: utf-8 -*-

from courcelles.urban.dataimport.parcellings.mappers import IdMapper
from courcelles.urban.dataimport.parcellings.mappers import ParcellingFactory
from courcelles.urban.dataimport.parcellings.mappers import ParcelFactory
from courcelles.urban.dataimport.parcellings.mappers import ParcelRefMapper

from imio.urban.dataimport.mapper import SimpleMapper


OBJECTS_NESTING = [
    (
        'PARCELLING', [
            ('PARCEL', []),
        ],
    ),
]

FIELDS_MAPPINGS = {
    'PARCELLING':
    {
        'factory': [ParcellingFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'n° permis',
                    'to': 'label',
                },
                {
                    'from': 'Nom',
                    'to': 'subdividerName',
                },
                {
                    'from': 'date permis',
                    'to': 'authorizationDate',
                },
                {
                    'from': 'nombre lots',
                    'to': 'numberOfParcels',
                },
                {
                    'from': 'remarques',
                    'to': 'changesDescription',
                },
            ),

            IdMapper: {
                'from': 'n° permis',
                'to': 'id',
            },
        },
    },

    'PARCEL':
    {
        'factory': [ParcelFactory],

        'mappers': {
            ParcelRefMapper: {
                'from': ('Division', 'section', 'numéro cadastral',),
                'to': ('radical', 'exposant', 'puissance', 'bis'),
            },
        },
    },
}
