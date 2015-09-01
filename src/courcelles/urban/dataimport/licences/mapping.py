# -*- coding: utf-8 -*-

from courcelles.urban.dataimport.licences.mappers import ArchitectMapper
from courcelles.urban.dataimport.licences.mappers import CompleteFolderDateMapper
from courcelles.urban.dataimport.licences.mappers import CompleteFolderEventTypeMapper
from courcelles.urban.dataimport.licences.mappers import CompletionStateMapper
from courcelles.urban.dataimport.licences.mappers import ContactFactory
from courcelles.urban.dataimport.licences.mappers import ContactIdMapper
from courcelles.urban.dataimport.licences.mappers import ContactNameMapper
from courcelles.urban.dataimport.licences.mappers import ContactSreetMapper
from courcelles.urban.dataimport.licences.mappers import ContactTitleMapper
from courcelles.urban.dataimport.licences.mappers import DecisionDateMapper
from courcelles.urban.dataimport.licences.mappers import DecisionEventTypeMapper
from courcelles.urban.dataimport.licences.mappers import DecisionMapper
from courcelles.urban.dataimport.licences.mappers import DepositDateMapper
from courcelles.urban.dataimport.licences.mappers import DepositEventTypeMapper
from courcelles.urban.dataimport.licences.mappers import ErrorsMapper
from courcelles.urban.dataimport.licences.mappers import IncompleteFolderDateMapper
from courcelles.urban.dataimport.licences.mappers import IncompleteFolderEventTypeMapper
from courcelles.urban.dataimport.licences.mappers import LicenceFactory
from courcelles.urban.dataimport.licences.mappers import NotificationDateMapper
from courcelles.urban.dataimport.licences.mappers import ObservationsMapper
from courcelles.urban.dataimport.licences.mappers import ParcelFactory
from courcelles.urban.dataimport.licences.mappers import ParcelReferencesMapper
from courcelles.urban.dataimport.licences.mappers import PortalTypeMapper
from courcelles.urban.dataimport.licences.mappers import UrbanEventFactory
from courcelles.urban.dataimport.licences.mappers import WorklocationMapper

from imio.urban.dataimport.access.mapper import AccessSimpleMapper as SimpleMapper

OBJECTS_NESTING = [
    (
        'LICENCE', [
            ('CONTACT', []),
            ('PARCEL', []),
            ('DEPOSIT EVENT', []),
            ('INCOMPLETE FOLDER EVENT', []),
            ('COMPLETE FOLDER EVENT', []),
            ('DECISION EVENT', []),
        ],
    ),
]

FIELDS_MAPPINGS = {
    'LICENCE':
    {
        'factory': [LicenceFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'genre',
                    'to': 'licenceSubject',
                },
                {
                    'from': 'N°',
                    'to': 'id',
                },
                {
                    'from': 'N°',
                    'to': 'reference',
                },
                {
                    'from': 'autreref',
                    'to': 'referenceDGATLP',
                },
            ),

            PortalTypeMapper: {
                'from': 'type',
                'to': ('portal_type', 'folderCategory',)
            },

            WorklocationMapper: {
                'from': ('lieu', 'ruelieu'),
                'to': 'workLocations',
            },

#            PcaMapper: {
#                'from': ('DatePPA',),
#                'to': ('isInPCA', 'pca',),
#            },

#            ParcellingsMapper: {
#                'from': ('AncCommune', 'NumLot', 'DateLot', 'DateLotUrbanisme'),
#                'to': ('isInSubdivision', 'parcellings',),
#            },

#            ParcellingRemarksMapper: {
#                'from': ('PPAObservations',),
#                'to': ('locationTechnicalRemarks',),
#            },

            ObservationsMapper: {
                'from': ('caractéristiques', 'REMARQUES'),
                'to': 'description',
            },

            ArchitectMapper: {
                'allowed_containers': ['BuildLicence'],
                'from': 'architecte',
                'to': 'architects',
            },

            CompletionStateMapper: {
                'from': ('datepermis', 'daterefus'),
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
                    'from': 'codeposte',
                    'to': 'zipcode',
                },
                {
                    'from': 'domicile',
                    'to': 'city',
                },
            ),
            ContactTitleMapper: {
                'from': 'Titre',
                'to': 'personTitle',
            },

            ContactNameMapper: {
                'from': 'Nom',
                'to': ('name1', 'name2'),
            },

            ContactSreetMapper: {
                'from': 'ruedomicile',
                'to': ('street', 'number'),
            },

            ContactIdMapper: {
                'from': 'Nom',
                'to': 'id',
            },
        },
    },

    'PARCEL':
    {
        'factory': [ParcelFactory, {'portal_type': 'PortionOut'}],

        'mappers': {
            ParcelReferencesMapper: {
                'from': ('lieu', 'section', 'numérocadastral'),
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

    'INCOMPLETE FOLDER EVENT':
    {
        'factory': [UrbanEventFactory],

        'allowed_containers': ['BuildLicence', 'ParcelOutLicence'],

        'mappers': {
            IncompleteFolderEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            IncompleteFolderDateMapper: {
                'from': 'datedossierincom',
                'to': 'eventDate',
            },
        },
    },

    'COMPLETE FOLDER EVENT':
    {
        'factory': [UrbanEventFactory],

        'allowed_containers': ['BuildLicence', 'ParcelOutLicence'],

        'mappers': {
            CompleteFolderEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            CompleteFolderDateMapper: {
                'from': 'dateaccuseréception',
                'to': 'eventDate',
            },
        },
    },

    'DECISION EVENT':
    {
        'factory': [UrbanEventFactory],

        'mappers': {
            DecisionEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            DecisionDateMapper: {
                'from': ('datepermis', 'daterefus'),
                'to': 'decisionDate',
            },

            NotificationDateMapper: {
                'from': 'dateenvoipermis',
                'to': 'eventDate',
            },

            DecisionMapper: {
                'from': ('datepermis', 'daterefus'),
                'to': 'decision',
            },
        },
    },
}
