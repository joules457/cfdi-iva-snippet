"""
Constants

"""
import re

XML_PATTERN = re.compile('.+\\.(xml)$', re.I)
ALL_FILE_PATTERN = re.compile('.*', re.I)
EMPTY_STRING_PATTERN = re.compile('^$', re.I)

BS_PARSER = 'html.parser'
