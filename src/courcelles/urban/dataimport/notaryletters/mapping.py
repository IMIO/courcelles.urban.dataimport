# -*- coding: utf-8 -*-

from courcelles.urban.dataimport.notaryletters.mappers import CompletionStateMapper
from courcelles.urban.dataimport.notaryletters.mappers import ContactFactory
from courcelles.urban.dataimport.notaryletters.mappers import ContactIdMapper
from courcelles.urban.dataimport.notaryletters.mappers import DepositDateMapper
from courcelles.urban.dataimport.notaryletters.mappers import DepositEventTypeMapper
from courcelles.urban.dataimport.notaryletters.mappers import ErrorsMapper
from courcelles.urban.dataimport.notaryletters.mappers import NotaryletterFactory
from courcelles.urban.dataimport.notaryletters.mappers import ObservationsMapper
from courcelles.urban.dataimport.notaryletters.mappers import ParcelFactory
from courcelles.urban.dataimport.notaryletters.mappers import ParcelReferencesMapper
from courcelles.urban.dataimport.notaryletters.mappers import UrbanEventFactory
from courcelles.urban.dataimport.notaryletters.mappers import WorksEndEventDateMapper
from courcelles.urban.dataimport.notaryletters.mappers import WorksEndEventTypeMapper
from courcelles.urban.dataimport.notaryletters.mappers import WorklocationMapper

from imio.urban.dataimport.access.mapper import AccessSimpleMapper as SimpleMapper

OBJECTS_NESTING = [
    (
        'LICENCE', [
            ('CONTACT', []),
            ('PARCEL', []),
#            ('DEPOSIT EVENT', []),
#            ('WORKS END EVENT', []),
        ],
    ),
]

FIELDS_MAPPINGS = {
    'LICENCE':
    {
        'factory': [NotaryletterFactory, {'portal_type': 'NotaryLetter'}],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'N°',
                    'to': 'id',
                },
                {
                    'from': 'N°',
                    'to': 'reference',
                },
            ),

            WorklocationMapper: {
                'from': ('localitebien', 'ruebien'),
                'to': 'workLocations',
            },

            ObservationsMapper: {
                'from': ('caractéristiques', 'REMARQUES'),
                'to': 'description',
            },

            CompletionStateMapper: {
                'from': 'dateenvoi',
                'to': (),  # <- no field to fill, its the workflow state that has to be changed
            },

            ErrorsMapper: {
                'from': (),
                'to': 'description',  # log all the errors in the description field
            }
        },
    },

    'CONTACT':
    {
        'factory': [ContactFactory],

        'mappers': {

            SimpleMapper: (
                {
                    'from': 'nompro',
                    'to': 'name1',
                },
            ),

            ContactIdMapper: {
                'from': 'nompro',
                'to': 'id',
            },
        },
    },

    'PARCEL':
    {
        'factory': [ParcelFactory, {'portal_type': 'PortionOut'}],

        'mappers': {
            ParcelReferencesMapper: {
                'from': ('localitebien', 'section', 'cadastre'),
                'to': (),
            },
        },
    },

    'DEPOSIT EVENT':
    {
        'factory': [UrbanEventFactory],

        'mappers': {
            DepositEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            DepositDateMapper: {
                'from': 'daterecepisse',
                'to': 'eventDate',
            }
        },
    },

    'WORKS END EVENT':
    {
        'factory': [UrbanEventFactory],

        'allowed_containers': ['BuildLicence'],

        'mappers': {
            WorksEndEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            WorksEndEventDateMapper: {
                'from': 'fintravaux',
                'to': 'eventDate',
            },
        },
    },
}
