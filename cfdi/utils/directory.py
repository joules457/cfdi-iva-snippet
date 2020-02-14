"""
Directory Utils

"""
import re
import os
from cfdi.utils import constants as ccfdi


def get_directory_files(
        path: str,
        include_pattern: re.Pattern = None,
        exclude_pattern: re.Pattern = None
):
    """List files from given path directory,
    take an include and exclude patterns.

    Parameters
    ----------
    include_pattern : re.Pattern
        Include files  re.compile pattern.
    exclude_pattern : re.Pattern
        Exclude files re.compile pattern.

    Returns
    -------
    dict
        List of files that match given pattern.
        {status, files}

    """
    result = {
        'status': 0,
        'files': [],
    }
    try:
        my_include_pattern = include_pattern \
            if include_pattern \
            else ccfdi.ALL_FILE_PATTERN
        my_exclude_pattern = exclude_pattern \
            if exclude_pattern \
            else ccfdi.EMPTY_STRING_PATTERN
        files = [
            f for f in os.listdir(path)
            if os.path.isfile(os.path.join(path, f))
        ]
        for file in files:
            if my_include_pattern.match(file) and \
                    not my_exclude_pattern.match(file):
                result['files'].append(file)
    except Exception as err:
        result['status'] = 1
        result['files'] = None
        result['error'] = err
    return result
