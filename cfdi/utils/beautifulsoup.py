"""
Beautiful soup utils

"""
from bs4 import BeautifulSoup


def load_file_to_bso(filename: str, parser: str = None):
    """Load File to BeautifulSoup object.

    Parameters
    ----------
    filename : str
        Filename to be loaded as BeautifulSoup.
    parser : str
        Parser used by BeautifulSoup to load file.

    Returns
    -------
    dict
        Result object {status, bso}.

    """
    result = {
        'status': 0,
        'bso': None
    }
    try:
        with open(filename, 'r') as fh:
            result['bso'] = BeautifulSoup(
                 fh.read(),
                 parser
            )
    except Exception as err:
        result['status'] = 1
        result['error'] = err
    return result
