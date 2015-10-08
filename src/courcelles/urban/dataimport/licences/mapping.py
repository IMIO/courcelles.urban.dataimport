# -*- coding: utf-8 -*-

from courcelles.urban.dataimport.licences.mappers import ArchitectMapper
from courcelles.urban.dataimport.licences.mappers import CollegeReportDateMapper
from courcelles.urban.dataimport.licences.mappers import CollegeReportEventTypeMapper
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
from courcelles.urban.dataimport.licences.mappers import DeclarationDecisionEventTypeMapper
from courcelles.urban.dataimport.licences.mappers import DecisionMapper
from courcelles.urban.dataimport.licences.mappers import DelayMapper
from courcelles.urban.dataimport.licences.mappers import DepositDateMapper
from courcelles.urban.dataimport.licences.mappers import DepositEventTypeMapper
from courcelles.urban.dataimport.licences.mappers import ErrorsMapper
from courcelles.urban.dataimport.licences.mappers import FolderCategoryMapper
from courcelles.urban.dataimport.licences.mappers import FolderZoneMapper
from courcelles.urban.dataimport.licences.mappers import FoldermanagerMapper
from courcelles.urban.dataimport.licences.mappers import IncompleteFolderDateMapper
from courcelles.urban.dataimport.licences.mappers import IncompleteFolderEventTypeMapper
from courcelles.urban.dataimport.licences.mappers import InquiryArticlesMapper
from courcelles.urban.dataimport.licences.mappers import InquiryEndMapper
from courcelles.urban.dataimport.licences.mappers import InquiryStartMapper
from courcelles.urban.dataimport.licences.mappers import LicenceFactory
from courcelles.urban.dataimport.licences.mappers import NotificationDateMapper
from courcelles.urban.dataimport.licences.mappers import NotificationEventTypeMapper
from courcelles.urban.dataimport.licences.mappers import ObservationsMapper
from courcelles.urban.dataimport.licences.mappers import OpinionsMapper
from courcelles.urban.dataimport.licences.mappers import ParcelFactory
from courcelles.urban.dataimport.licences.mappers import ParcellingsMapper
from courcelles.urban.dataimport.licences.mappers import ParcelReferencesMapper
from courcelles.urban.dataimport.licences.mappers import PcaMapper
from courcelles.urban.dataimport.licences.mappers import PortalTypeMapper
from courcelles.urban.dataimport.licences.mappers import ReclamationsMapper
from courcelles.urban.dataimport.licences.mappers import PrimoDateMapper
from courcelles.urban.dataimport.licences.mappers import PrimoEventTypeMapper
from courcelles.urban.dataimport.licences.mappers import RemovalDateMapper
from courcelles.urban.dataimport.licences.mappers import RemovalEventTypeMapper
from courcelles.urban.dataimport.licences.mappers import SecondRWEventDateMapper
from courcelles.urban.dataimport.licences.mappers import SecondRWDecisionDateMapper
from courcelles.urban.dataimport.licences.mappers import SecondRWDecisionMapper
from courcelles.urban.dataimport.licences.mappers import SecondRWEventTypeMapper
from courcelles.urban.dataimport.licences.mappers import UrbanEventFactory
from courcelles.urban.dataimport.licences.mappers import UsageMapper
from courcelles.urban.dataimport.licences.mappers import WorksStartEventDateMapper
from courcelles.urban.dataimport.licences.mappers import WorksStartEventTypeMapper
from courcelles.urban.dataimport.licences.mappers import WorksEndEventDateMapper
from courcelles.urban.dataimport.licences.mappers import WorksEndEventTypeMapper
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
            ('PRIMO RW EVENT', []),
            ('COLLEGE REPORT EVENT', []),
            ('SECOND RW EVENT', []),
            ('DECISION EVENT', []),
            ('DECLARATION DECISION EVENT', []),
            ('NOTIFICATION EVENT', []),
            ('REMOVAL EVENT', []),
            ('WORKS START EVENT', []),
            ('WORKS END EVENT', []),
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
                'to': 'portal_type'
            },

            FolderCategoryMapper: {
                'from': ('type', 'zonepca', 'datelot', 'reflot', 'dateaviscol'),
                'to': 'folderCategory',
            },

            FoldermanagerMapper: {
                'from': 'agent traitant',
                'to': 'foldermanagers',
            },

            WorklocationMapper: {
                'from': ('lieu', 'ruelieu'),
                'to': 'workLocations',
            },

            DelayMapper: {
                'from': 'délai',
                'to': 'annoncedDelay',
            },

            FolderZoneMapper: {
                'from': 'zoneplansecteur',
                'to': ('folderZone', 'folderZoneDetails')
            },

            PcaMapper: {
                'from': ('dateppa', 'refppa', 'zonepca'),
                'to': ('isInPCA', 'pca', 'pcaDetails', 'pcaZone'),
            },

            ParcellingsMapper: {
                'from': ('reflot', 'n°lot', 'datelot'),
                'to': ('isInSubdivision', 'parcellings', 'subdivisionDetails'),
            },

            ObservationsMapper: {
                'from': ('caractéristiques', 'REMARQUES'),
                'to': 'description',
            },

            ArchitectMapper: {
                'allowed_containers': ['BuildLicence'],
                'from': 'architecte',
                'to': 'architects',
            },

            UsageMapper: {
                'allowed_containers': ['BuildLicence'],
                'from': 'modele',
                'to': 'usage',
            },

            InquiryStartMapper: {
                'from': 'débutenquete',
                'to': 'investigationStart',
            },

            InquiryEndMapper: {
                'from': 'finenquete',
                'to': 'investigationEnd',
            },

            InquiryArticlesMapper: {
                'from': 'caractéristiques',
                'to': ('investigationArticles', 'investigationReasons'),
            },

            ReclamationsMapper: {
                'from': 'nombreréclamation',
                'to': 'investigationWriteReclamationNumber',
            },

            OpinionsMapper: {
                'from': (
                    'transAGRICULTURE',
                    'transSRI',
                    'transCCAT',
                    'transRAVel',
                    'transELECTRABEL',
                    'transIGRETEC',
                    'transCHACUNLOGIS',
                    'transSERVICEVOYER',
                    'transMET',
                    'transMONUMENTSITES',
                    'transNATUREFORET',
                    'transSNCB'
                ),
                'to': 'solicitOpinionsTo',
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

    'PRIMO RW EVENT':
    {
        'factory': [UrbanEventFactory],

        'allowed_containers': ['BuildLicence', 'ParcelOutLicence'],

        'mappers': {
            PrimoEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            PrimoDateMapper: {
                'from': 'dateenvoiprédossier',
                'to': 'eventDate',
            },
        },
    },

    'COLLEGE REPORT EVENT':
    {
        'factory': [UrbanEventFactory],

        'allowed_containers': ['BuildLicence', 'ParcelOutLicence'],

        'mappers': {
            CollegeReportEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            CollegeReportDateMapper: {
                'from': 'dateaviscol',
                'to': 'eventDate',
            },
        },
    },

    'SECOND RW EVENT':
    {
        'factory': [UrbanEventFactory],

        'allowed_containers': ['BuildLicence', 'ParcelOutLicence'],

        'mappers': {
            SecondRWEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            SecondRWEventDateMapper: {
                'from': 'dateenvoiaviscol',
                'to': 'eventDate',
            },

            SecondRWDecisionMapper: {
                'from': 'typeavis',
                'to': 'externalDecision',
            },

            SecondRWDecisionDateMapper: {
                'from': 'dateavisfoncdelegue',
                'to': 'decisionDate',
            },
        },
    },

    'DECISION EVENT':
    {
        'factory': [UrbanEventFactory],

        'allowed_containers': ['BuildLicence', 'ParcelOutLicence'],

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

    'DECLARATION DECISION EVENT':
    {
        'factory': [UrbanEventFactory],

        'allowed_containers': ['Declaration'],

        'mappers': {
            DeclarationDecisionEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            DecisionDateMapper: {
                'from': ('datepermis', 'daterefus'),
                'to': 'eventDate',
            },

            DecisionMapper: {
                'from': ('datepermis', 'daterefus'),
                'to': 'decision',
            },
        },
    },

    'NOTIFICATION EVENT':
    {
        'factory': [UrbanEventFactory],

        'allowed_containers': ['Declaration'],

        'mappers': {
            NotificationEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            NotificationDateMapper: {
                'from': 'dateenvoipermis',
                'to': 'eventDate',
            },
        },
    },

    'REMOVAL EVENT':
    {
        'factory': [UrbanEventFactory],

        'allowed_containers': ['BuildLicence', 'ParcelOutLicence'],

        'mappers': {
            RemovalEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            RemovalDateMapper: {
                'from': ('datepermis', 'daterefus'),
                'to': 'eventDate',
            },
        },
    },

    'WORKS START EVENT':
    {
        'factory': [UrbanEventFactory],

        'allowed_containers': ['BuildLicence'],

        'mappers': {
            WorksStartEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            WorksStartEventDateMapper: {
                'from': 'débuttravaux',
                'to': 'eventDate',
            },
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
