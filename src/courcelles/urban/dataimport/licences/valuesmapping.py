# -*- coding: utf-8 -*-

from imio.urban.dataimport.mapping import table

VALUES_MAPS = {

'type_map': table({
'header'      : ['portal_type',  'foldercategory'],
''            : ['BuildLicence', 'uap'],
'PerOrd'      : ['BuildLicence', 'uap'],
'CU2'         : ['BuildLicence', 'uap'],
'aut com'     : ['BuildLicence', 'upp'],
'Aut com'     : ['BuildLicence', 'upp'],
'art 127'     : ['BuildLicence', 'art127'],
'Declarat'    : ['Declaration',  'dup'],
'Déclaration' : ['Declaration',  'dup'],
'Puniq'       : [None,           None],
'socio'       : [None,           None],
}),

'titre_map': {
    'monsieur': 'mister',
    'm': 'mister',
    'm.': 'mister',
    'messieurs': 'misters',
    'mrs.': 'misters',
    'mrs': 'misters',
    'madame': 'madam',
    'mme': 'madam',
    'mme.': 'madam',
    'mmes': 'ladies',
    'mesdames': 'ladies',
    'mlle': 'miss',
    'melle': 'miss',
    'mademoiselle': 'miss',
    'monsieur et madame': 'madam_and_mister',
    'madame et monsieur': 'madam_and_mister',
    'm et mme': 'madam_and_mister',
    'mr et mme': 'madam_and_mister',
    'm. et mme': 'madam_and_mister',
    'm et mme.': 'madam_and_mister',
    'm. et mme.': 'madam_and_mister',
},

'eventtype_id_map': table({
'header'             : ['decision_event',                       'folder_complete',     'deposit_event'],
'BuildLicence'       : ['delivrance-du-permis-octroi-ou-refus', 'accuse-de-reception', 'depot-de-la-demande'],
'ParcelOutLicence'   : ['delivrance-du-permis-octroi-ou-refus', 'accuse-de-reception', 'depot-de-la-demande'],
'Declaration'        : ['deliberation-college',                 '',                    'depot-de-la-demande'],
}),

}
