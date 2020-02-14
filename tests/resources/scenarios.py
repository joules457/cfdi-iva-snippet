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
