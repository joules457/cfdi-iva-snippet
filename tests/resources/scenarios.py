"""
Scenarios

"""
from cfdi.utils import constants as ccfdi

DIRECTORY_FILES = [
    {
        'payload': {
            'path': 'resources/files',
            'include_pattern': None,
            'exclude_pattern': None
        },
        'result': ['cfdi.xml', 'mock1.txt', 'mock2.xml', 'mock3.xml'],
        'error': False,
    },
    {
        'payload': {
            'path': 'resources/files',
            'include_pattern': ccfdi.XML_PATTERN,
            'exclude_pattern': None
        },
        'result': ['cfdi.xml', 'mock2.xml', 'mock3.xml'],
        'error': False,
    },
    {
        'payload': {
            'path': 'nonexistent/path',
            'include_pattern': None,
            'exclude_pattern': None
        },
        'error': True,
    }
]

BEAUTIFULSOUP_FILES = [
    {
        'payload': {
            'filename': 'resources/files/cfdi.xml',
            'parser': 'html.parser',
        },
        'error': False,
    },
    {
        'payload': {
            'filename': 'resources/files/cfdi.xml',
            'parser': 'html.parser',
        },
        'error': False,
    },
    {
        'payload': {
            'filename': 'nonexistent/file/algo.xml',
            'parser': 'html.parser',
        },
        'error': True,
    },
]

IVA_AMOUNT = [
    {
        'payload': {
            'dir_path': 'resources/files',
        },
        'total_iva_amount': 211.73,
        'error': False,
    },
    {
        'payload': {
            'dir_path': 'nonexistent/path',
            'include_pattern': None,
            'exclude_pattern': None
        },
        'total_iva_amount': None,
        'error': True,
    }
]

CFDI_AMOUNTS = [
    {
        'payload': {
            'dir_path': 'resources/files',
        },
        'iva_cfdi_amount': 211.73,
        'total_cfdi_amount': 750,
        'subtotal_cfdi_amount': 646.54,
        'error': False,
    },
    {
        'payload': {
            'dir_path': 'nonexistent/path',
            'include_pattern': None,
            'exclude_pattern': None
        },
        'iva_cfdi_amount': None,
        'total_cfdi_amount': None,
        'subtotal_cfdi_amount': None,
        'error': True,
    }
]

CSV_FILE = [
    {
        'payload': {
            'filename': '',
            'dict_list': []
        },
        'contents': '',
        'error': True
    },
    {
        'payload': {
            'filename': 'test.csv',
            'dict_list': []
        },
        'contents': '''
''',
        'error': False
    },
    {
        'payload': {
            'filename': 'test.csv',
            'dict_list': [
                {'field1': 'value', 'field2': 2},
                {'field1': 'value2', 'field2': 25.3},
            ]
        },
        'contents': '''field1,field2
value,2
value2,25.3
''',
        'error': False
    },
]
