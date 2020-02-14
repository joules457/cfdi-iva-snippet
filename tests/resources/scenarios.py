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
        'result': ['mock1.txt', 'mock3.xml', 'mock2.xml'],
        'error': False,
    },
    {
        'payload': {
            'path': 'resources/files',
            'include_pattern': ccfdi.XML_PATTERN,
            'exclude_pattern': None
        },
        'result': ['mock3.xml', 'mock2.xml'],
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
