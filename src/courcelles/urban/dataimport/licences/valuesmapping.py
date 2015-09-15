# -*- coding: utf-8 -*-

from imio.urban.dataimport.mapping import table

VALUES_MAPS = {

'type_map': table({
'header'      : ['portal_type',  'foldercategory'],
''            : ['BuildLicence', 'upp'],
'PerOrd'      : ['BuildLicence', 'upp'],
'CU2'         : ['BuildLicence', 'upp'],
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

'division_map': {
    'courcelles': '52015',
    'gouy-lez-piéton': '52031',
    'souvret': '52064',
    'trazegnies': '52066',
},

'externaldecisions_map': {
    'favorable': 'favorable',
    'favorable conditionel': 'favorable-conditionnel',
    'défavorable': 'defavorable',
    'défavorable révisable': 'defavorable-revisable',
    'favorable par défaut': 'favorable-defaut',
},

}
