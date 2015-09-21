# -*- coding: utf-8 -*-

from imio.urban.dataimport.mapping import table

VALUES_MAPS = {

    'type_map': table({
        'header': ['portal_type', 'foldercategory'],
        '': ['BuildLicence', 'upp'],
        'PerOrd': ['BuildLicence', 'upp'],
        'CU2': ['BuildLicence', 'upp'],
        'aut com': ['BuildLicence', 'upp'],
        'Aut com': ['BuildLicence', 'upp'],
        'art 127': ['BuildLicence', 'art127'],
        'Declarat': ['Declaration', 'dup'],
        'Déclaration': ['Declaration', 'dup'],
        'Puniq': [None, None],
        'socio': [None, None],
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

    'parcellings_map': {
        '10091/1L38 - 1': '1',
        '2': '2',
        '10/52015/1L98 - 3': '3',
        '10.091/1L59 - 4': '4',
        '10091/1L66 - 5': '4',
        '10.091/1L36 - 7': '5',
        '10/52015/1L84 - 8': '6',
        '10/52015/1L82 - 9': '7',
        '10': '8',
        '10/52015/1L78 - 13': '10',
        '10/52015/1L58 - 14': '11',
        '10/52015/1L93 - 15': '13',
        '10/52015/1L88 - 16': '14',
        '10091/67L - 17': '15',
        '10091/1L26 - 18': '16',
        '10091/1L25 - 19': '17',
        '10/52015/1L89 - 20': '18',
        '10091/1L19 - 21': '19',
        '10091/1L41': '20',
        '10091/1L16 - 22': '22',
        '10091/1L24 - 23': '23',
        '10091/53L - 24': '24',
        '10091/1L29 - 25': '25',
        '10091/1L29 - 26': '26',
        '10091/1L62 - 27': '27',
        '10091/65L - 28': '28',
        '29': '29',
        '10091/39H - 29': '29',
        '10091/1L11 - 30': '30',
        '10091/68L - 31': '31',
        '10/52015/1L96 - 32': '32',
        '10091/47L - 33': '33',
        '10091/75L - 34': '34',
        '10091/1L74 - 36': '35',
        '10091/1L63 - 37': '36',
        '10/52015/1L95 - 38': '37',
        '10091/55L - 411': '38',
        '39': '39',
        '10091/46L - 41': '40',
        '10091/1L22 - 42': '41',
        '43': '42',
        '44': '43',
        '10091/71 - 45': '44',
        '10091/1L57 - 46': '45',
        '10091/51L - 47': '46',
        '10091/1L27 - 48': '47',
        '10091/1L17 - 49': '48',
        '10091/1L42 - 50': '49',
        '10091/1L21 - 51': '50',
        '10091/1L5 - 52': '51',
        '10/52015/1L80 - 53': '52',
        '10091/50L - 54': '53',
        '10091/40L - 55': '54',
        '10091/32L - 56': '55',
        '10091/1L45 - 57': '56',
        '10091/72L - 58': '57',
        '10091/48L - 59': '58',
        '10091/1L6 - 61': '60',
        '10/52015/1L91 - 62': '61',
        '10091/1L61 - 63': '62',
        '10091/1L7 - 64': '63',
        '10091/43L - 65': '64',
        '10091/70L66': '65',
        '10/52015/1L94 - 67': '66',
        '10/52015/1L90 - 68': '67',
        '10091/30L - 69': '68',
        '10/52015/76L - 70': '69',
        '10/52015/6L - 71': '70',
        '10091/60L - 72': '71',
        '10091/1L56 - 73': '72',
        '10091/1L15 - 74': '73',
        '10091/1L12 - 75': '74',
        '10091/37L - 76': '75',
        '10091/1L13 - 77': '76',
        '10091/73L - 78': '77',
        '10091/1L54 - 79': '78',
        '10091/1L14 - 80': '79',
        '10404/2L - 81': '80',
        '10404/16L - 82': '81',
        '10404/4L': '',
        '10404/1L5 - 83': '82',
        '84': '83',
        '10404/7L - 85': '84',
        '10404/9L - 86': '85',
        '10404/10L - 87': '86',
        '10/52066/1L11 - 88': '87',
        '10/52066/1L12 - 89': '88',
        '10/52066/13L - 90': '89',
        '10/52066/1L14 - 91': '90',
        '10/52066/15L - 92': '91',
        '10/52066/1L16 - 93': '92',
        '10/52066/1L17 - 94': '93',
        '10/52066/1L19 - 95': '94',
        '10/52066/1L21 - 96': '95',
        '10380/1L2 - 97': '96',
        '10/52064/1L11 - 98': '97',
        '10380/1L9 - 99': '98',
        '10380/1L6 - 100': '99',
        '10380/1L3 - 102': '100',
        '10/52064/1L13 - 103': '101',
        '10380/5L - 104': '102',
        '10/52064/1L16 - 105': '103',
        '10380/1L8 - 106': '104',
        '10380/1L7 - 107': '105',
        '10/52064/1L12 - 108': '106',
        '10/52031/1L14 - 109': '107',
        '10/52031/1L8 - 110': '108',
        '10/52031/1L9 - 111': '109',
        '10164/1L5 - 112': '110',
        '10/52031/1L10 - 113': '111',
        '10/52031/1L12 - 114': '112',
        '10164/1L24 - 116': '113',
        '10091/1L106 - 117': '114',
        '10/52031/1L18 - 118': '115',
        '10404/1L24 - 119': '116',
        '10/52064/1L17 - 120': '117',
        '': '118',
        '10404/1L26 - 123': '119',
        '124': '119',
        '10380/1L18 - 125': '120',
        '10091/1L11 - 126': '122',
        '10404/1L27 - 127': '123',
        '10091/1L123 - 129': '124',
        '10091/1L20 - 130': '125',
        '10091/1L109 - 131': '126',
        '10380/1L19 - 132': '127',
        '10091/1L116 - 133': '128',
        '10164/1L22 - 134': '129',
        '135': '130',
        '10164/1L21 - 137': '131',
        '10164/1L25 - 138': '132',
        '10164/1L26 - 139': '133',
        '10/52031/1L17 - 140': '134',
        '10091/1L22 - 141': '135',
        '10/52015/1L101 - 142': '136',
        '10404/1L22 - 143': '137',
        '10/52015/1L102 - 145': '138',
        '10091/1L119 - 146': '139',
        'MC du 12/1/79 - 147': '140',
        '10164/1L21 - 149': '141',
        '10/52015/1L97 - 150': '142',
        '10/52015/1L99 - 151': '143',
        '10/52031/1L15 - 152': '144',
        '10164/1L2 - 154': '145',
        '10091/1L127 - 155': '146',
        '10164/1L23 - 156': '147',
        '10/52015/1L124 - 157': '148',
        '10404/1L25 - 159': '149',
        '10/52031/1L20 - 160': '150',
        '10091/1L118 - 161': '151',
        '10091/108L - 162': '152',
        '10091/105L - 153': '153',
        '10/52064/1L14 - 164': '154',
        '10/52064/1L15 - 167': '155',
        '10091/1L103 - 168': '156',
        '10/52031/1L13 - 169': '157',
        '10404/1L29 - 172': '158',
        '10380/1L20 - 173': '159',
        '10380/1L21 -174': '160',
        '10091/1L114 - 175': '161',
        '10404/1L28 - 176': '162',
        '10091/1L115 - 177': '163',
        '10164/1L28 - 178': '164',
        '10/52031/1L16 - 179': '165',
        '10404/1L20 - 180': '166',
        '10/52015/1L108 - 181': '167',
        '10091/1L21 - 182': '168',
        '10091/1L112 - 183': '169',
        '10091/1L113 - 184': '171',
        '10/52066/1L23 - 186': '172',
        '10404/1L30 - 187': '173',
        '10091.1L128 - 188': '174',
        '10164/1L29 - 189': '175bis',
        '10164/1L29 / 190': '175',
        '10091/1L130 - 191': '176',
        '10164/1L30 - 192': '177',
        '10164/1L31 - 194': '178',
        '10091/1L131 - 195': '179',
        '10091/1L133 - 197': '180',
        '10380/1L23 - 198': '181',
        '10091/1L132 - 199': '182',
        '10380/1L22 - 200': '183',
        '10091/1L134 - 201': '184',
        '10091/1L135 - 202': '185',
        '10380/1L25 - 203': '186',
        '10164/1L24 - 204': '187',
        '10091/1L136 - 205': '188',
        '10091/1L137 - 207': '189',
        '10091/1L138 - 208': '190',
        '10404/1L31 - 209': '191',
        '10091/1L140 - 210': '192',
        '10091/1L139 - 211': '193',
        '10091/1L141 - 212': '194',
        '10091/1L142 - 213': '195',
        '10404/1L33 - 214': '196',
        '10380/1L27 - 215': '197',
        '10091/1L143 - 216': '198',
        '10091/1L144 - 217': '199',
        '10091/1L145 - 218': '200',
        '10091/1L147 - 219': '201',
        '10091/1L146 - 220': '202',
        '10091/1L149 - 221': '203',
        '10/52015/1L181 - 223': '204',
        '10091/1L148 - 224': '205',
        '10164/1L33 - 225': '206',
        '10404/1L34 - 226': '207',
        '10091/1L151 - 227': '208',
        '10/52015/1L152 - 229': '209',
        '10/52015/1L155 - 231': '210',
        '10/52015/1L154 - 232': '211',
        '10/52066/1L36 - 233': '212',
        '88/52015/066/1L35 - 234': '213',
        '10/52015/1L158 - 235': '214',
        '10/52031/1L36 - 236': '215',
        '10/52015/1L157 - 237': '216',
        '10/52015/1L159 - 238': '217',
        '10/52031/1L37 - 239': '218',
        '10/52015/1L156 - 240': '219',
        '10/52015/1L153 - 242': '220',
        '10/52064/1L28 - 243': '221',
        '10/52015/1L161 - 244': '222',
        '10/52015/1L162 - 245': '223',
        '10/52015/1L163 - 246': '224',
        '10/52066/1L38 - 247': '225',
        '10/52015/1L164 - 248': '226',
        '10/52066/1L39 - 249': '227',
        '10380/1L24 - 250': '228',
        '10/52015/1L165 - 251': '229',
        '10/52015/1L166 - 252': '230',
        'PCA - 253': '231',
        '10/52031/1L39- 255': '232',
        '10/52015/1L160 - 257': '233',
        '10.404/1L29 - 258': '234',
        '10/52066/1L41 - 259': '235',
        '10/52015/1L167 - 260': '236',
        '10/52031/1L40 - 261': '237',
        '10/52015/1L168 - 262': '238',
        '10/52015/1L169 - 263': '239',
        '10/52015/1L170 - 264': '240',
        '10/52061/1L49 - 265': '241',
        '10/52066/1L43 - 266': '242',
        '10/52031/1L41 - 267': '243',
        '10/52066/1L44 - 268': '244',
        '93/52066/1L37 - 269': '245',
        '10/52015/1L173 - 270': '246',
        '10/52066/1L45 - 415': '247',
        '10/52015/1L174 - 271': '248',
        '10/52031/1L42 - 272': '249',
        '10/52015/1L175 - 273': '250',
        '10/52031/1L43 - 274': '251',
        '10/52015/1L176 - 275': '252',
        '10/52064/1L29 - 276': '253',
        '10/52064/1L30 - 277': '254',
        '10/52031/1L45 - 278': '255',
        '10/52031/1L44 - 279': '256',
        '10/52015/1L177 - 280': '257',
        '10/52066/1L47 - 281': '258',
        '10/52015/1L178 - 282': '259',
        '10/52015/1L179 - 283': '260',
        '10/52066/1L46 - 284': '261',
        '10/52031/1L46 - 285': '262',
        '10/52064/1L31 - 286': '263',
        '10/52031/1L47 - 287': '264',
        '10/52015/1L183 - 288': '265',
        '10/52031/1L48 - 289': '266',
        '10/52031/1L49 - 290': '267',
        'F0312/52015/LOT/97.8/M - 291': '268',
        '10.52031/1L51 - 292': '269',
        '10/52031/1L50 - 293': '270',
        '10/52015/1L84 - 294': '271',
        '10/52066/1L50 - 295': '272',
        '10/52015/1L186 - 296': '273',
        '10/52015/1L185 - 297': '274',
        'F0312/52015/LOT/91.1 - 298': '275',
        'F0312/52015/LOT/97.2 - 299': '276',
        'F0312/52015/LOT/98.1 - 300': '277',
        'F0312/52015/LOT/97.5 - 301': '278',
        'F0312/52015/LAP/98.1/H - 302': '279',
        'F0312/52015/LAP/98.4/H - 303': '280',
        'F0312/52015/LOT/98.4 - 304': '281',
        'F0413/52015/LAP/1999.8 - 305': '282',
        'F0413/52015/LAP/99.7 - 306': '283',
        'F0413/52015/LAP/2000.5 - 307': '283',
        'F0413/52015/LAP/2000.11 - 308': '283',
        'F0413/52015/LAP/1999.9 - 309': '284',
        'F0413/52015/LAP/2000.3 - 310': '285',
        'F0413/52015/LAP/2000.4 - 311': '286',
        'F0413/52015/LAP/2000.8 - 312': '287',
        'F0413/52015/Lap/2000.7 - 313': '288',
        'F0413/52015/LAP/2000.9 - 314': '289',
        'F0413/52015/LAP/2001.8 - 315': '290',
        'F0413/52015/LAP/2002.2 - 316': '291',
        'F0413/52015/LAP/2001.5 - 317': '292',
        'F0413/52015/LAP/2001.1 - 318': '293',
        'F0413/52015/LAP/2001.4 - 319': '294',
        'F0413/52015/LAP/2001.7 - 320': '295',
        'F0413/52015/LAP/2001.6 - 321': '296',
        'F0413/52015/LAP/2001.11 - 322': '297',
        'F0413/52015/LAP/2001.1 - 323': '298',
        'F0413/52015/LAP/2001.13 - 324': '299',
        'F0413/52015/LAP/2001.12 - 325': '300',
        '10/52066/1L19 - 326': '301',
        'F0413/52015/LAP/2002.3 - 327': '302',
        '328': '303',
        'F0413/52015/LAP/2002.5 - 329': '304',
        'F0413/52015/LAP/2002.6 - 330': '305',
        'F0413/52015/LAP/2002.7 - 331': '306',
        'F0413/52015/LAP/2002.9/M - 332': '307',
        'F0413/52015/LAP/2002.8 - 333': '308',
        'F0413/52015/LAP/2002.11 - 334': '309',
        '335': '310',
        'F0413/52015/LAP/2002.10 - 336': '311',
        'F0413/52015/LAP/2002.12 - 337': '312',
        'F0413/52015/LAP/2002.13/M - 338': '313',
        'F0413/52015/LAP/2002.3 - 339': '314',
        'F0413/52015/LAP2/2003.5 - 340': '315',
        'F0413/52015/LAP/2003.3 - 341': '316',
        'F0413/52015/LOT/98.4 - 342': '317',
        'F0413/52015/LAP2/2003.11 - 343': '318',
        'F0413/52015/LAP/2001.2 - 344': '319',
        'F0413/52015/LAP2/2003.6 - 345': '320',
        'F0413/52015/LAP2/2003.7 - 346': '321',
        'F0413/52015/LAP2/2003.9 - 347': '322',
        'F0413/52015/LAP2/2003.8 - 348': '323',
        '349': '324',
        'F0413/52015/LAP/2003.12 - 350': '325',
        'F0413/52015/LAP2/2003.10 - 351': '326',
        'F0413/52015/LCP2/2004.3/TER - 352': '327',
        'F0413/52015/LCP2/2004.4/TER - 353': '328',
        'F0413/52015/LAP2/2004.3/bis354': '329',
        'F0411/52015/LAP3/2006.6 - 355': '330',
        'F0413/52015/LAP2/2004.4 - 356': '331',
        'F0413/52015/LAP2/2004.5/M - 357': '332',
        '358': '333',
        'F0411/52015/LAP2/2004.7 - 360': '334',
        'F0411/52015/LAP2/2004.7 - 359': '335',
        'F0411/52015/LAP3/2005/1 - 361': '336',
        '362': '337',
        'F0411/52015/LAP3/2005.2/M - 363': '338',
        '364': '339',
        'F0411/52015/LAP3/2006.1/M - 365': '340',
        'F0411/52015/LAP3/2006.2/M - 366': '341',
        'F0411/52015/LAP3/2006.3 - 367': '342',
        '368': '343',
        'F0411/52015/LAP3/2006.4/M - 369': '344',
        '370': '345',
        '371': '346',
        '372': '347',
        'F0411/52015/LAP3/2006.7 - 373': '348',
        'F0411/52015/LAP3/2006.8/M - 374': '349',
        'F0413/52015/LAP/2001.4 - 375': '350',
        'F0411/52015/LAP3/2006.10/M - 378': '351',
        'F0411/52015/LAP3/2006.11 - 379': '352',
        'F0411/52015/LAP3/2007.4/M - 380': '353',
        'F0411/52015/LAP3/2007.1 - 395': '354',
        'F0411/52015/LAP3/2007.3 - 396': '355',
        'F0411/52015/LAP3/2007.3 - 397': '356',
        'F0415/52015/LAP3/2007.5 - 398': '357',
        'F0411/52015/LAP3/2006.11 - 399': '358',
        'F0410/52015/LCP3/2007.1/M - 400': '359',
        'F0411/52015/LAP3/2007.7/M - 401': '360',
        'F0411/52015/LAP3/2008.2 - 402': '361',
        'F0411/52015/LAP3/2008.1/M - 403': '362',
        'F0411/52015/LAP3/2008.4 - 404': '363',
        'F0411/52015/LAP3/2008.3/M - 405': '364',
        '406': '365',
        '10/52015/1L40 - 407': '366',
        'F0411/52015/LAP3/2008.7 - 408': '367',
        'F0411/52015/LAP3/2009.7/M/bis - 409': '368',
        'F0411/52015/LAP3/2009.1/M - 410': '369',
        'F0411/52015/LAP3/2009.4 - 416': '370',
        'F0411/52015/LAP3/2008.4 - 417': '371',
        'F0411/52015/LAP3/2009.5 - 418': '372',
        'F0411/52015/LAP3/2009.2/bis - 419': '373',
        '420': '374',
        'F0411/52015/LAP3/2010.1/M - 421': '375',
        'F0411/52015/LAP3/2011.1 - 422': '376',
        'F0411/52015/LAP3/2010.2 - 423': '377',
        '424': '378',
        '425': '379',
        '': '380',
    }

}
