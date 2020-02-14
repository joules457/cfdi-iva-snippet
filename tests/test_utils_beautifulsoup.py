"""
Test cfdi/utils/directory

"""
import os
import pytest
from bs4 import BeautifulSoup
from tests.resources import scenarios
from cfdi.utils import beautifulsoup as bs_utils


@pytest.fixture(scope='session')
def dir_path():
    return os.path.dirname(
        os.path.realpath(__file__)
    )


def test_load_file_to_bso(dir_path):
    for scenario in scenarios.BEAUTIFULSOUP_FILES:
        abs_filename = os.path.join(
            dir_path, scenario['payload']['filename']
        )
        result = bs_utils.load_file_to_bso(
            abs_filename,
            scenario['payload']['parser']
        )
        if scenario['error']:
            assert result['status'] == 1
            assert result['bso'] is None
            assert isinstance(result['error'], Exception)
        else:
            assert result['status'] == 0
            assert isinstance(result['bso'], BeautifulSoup)
        print(result)
    # assert False
