# -*- coding: utf-8 -*-

from courcelles.urban.dataimport.notaryletters.mappers import CompletionStateMapper
from courcelles.urban.dataimport.notaryletters.mappers import ContactFactory
from courcelles.urban.dataimport.notaryletters.mappers import ContactIdMapper
from courcelles.urban.dataimport.notaryletters.mappers import DeliveryEventDateMapper
from courcelles.urban.dataimport.notaryletters.mappers import DeliveryEventTypeMapper
from courcelles.urban.dataimport.notaryletters.mappers import DepositDateMapper
from courcelles.urban.dataimport.notaryletters.mappers import DepositEventTypeMapper
from courcelles.urban.dataimport.notaryletters.mappers import ErrorsMapper
from courcelles.urban.dataimport.notaryletters.mappers import NotaryMapper
from courcelles.urban.dataimport.notaryletters.mappers import NotaryletterFactory
from courcelles.urban.dataimport.notaryletters.mappers import ObservationsMapper
from courcelles.urban.dataimport.notaryletters.mappers import PortaltypeMapper
from courcelles.urban.dataimport.notaryletters.mappers import ParcelFactory
from courcelles.urban.dataimport.notaryletters.mappers import ParcelReferencesMapper
from courcelles.urban.dataimport.notaryletters.mappers import ReferenceMapper
from courcelles.urban.dataimport.notaryletters.mappers import UrbanEventFactory
from courcelles.urban.dataimport.notaryletters.mappers import WorklocationMapper

from imio.urban.dataimport.access.mapper import AccessSimpleMapper as SimpleMapper

OBJECTS_NESTING = [
    (
        'LICENCE', [
            ('CONTACT', []),
            ('PARCEL', []),
            ('DEPOSIT EVENT', []),
            ('DELIVERY EVENT', []),
        ],
    ),
]

FIELDS_MAPPINGS = {
    'LICENCE':
    {
        'factory': [NotaryletterFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'N°',
                    'to': 'id',
                },
            ),

            PortaltypeMapper: {
                'from': 'CU1',
                'to': 'portal_type'
            },

            ReferenceMapper: {
                'from': 'N°',
                'to': 'reference',
            },

            NotaryMapper: {
                'from': 'NOM',  # 'from': 'notaire',
                'to': 'notaryContact',
            },

            WorklocationMapper: {
                'from': ('localitebien', 'ruebien'),
                'to': 'workLocations',
            },

            ObservationsMapper: {
                'from': ('caractéristiques', 'remarqueurbanisme'),
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
                'from': 'daterecu',
                'to': 'eventDate',
            }
        },
    },

    'DELIVERY EVENT':
    {
        'factory': [UrbanEventFactory],

        'mappers': {
            DeliveryEventTypeMapper: {
                'from': ('CU1'),
                'to': 'eventtype',
            },

            DeliveryEventDateMapper: {
                'from': 'dateenvoi',
                'to': 'eventDate',
            },
        },
    },
}
