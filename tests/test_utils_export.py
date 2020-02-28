"""
Test cfdi/utils/export

"""
import os
import pytest
from tests.resources import scenarios
from cfdi.utils import export as export_utils


@pytest.fixture(scope='session')
def dir_path():
    return os.path.dirname(
        os.path.realpath(__file__)
    )


def test_get_directory_files(dir_path):
    for scenario in scenarios.CSV_FILE:
        payload = scenario['payload']
        abs_filename = os.path.join(dir_path, payload['filename'])
        result = export_utils.csv_file(
            payload['dict_list'],
            abs_filename
        )
        if scenario['error']:
            assert result['status'] == 1
            assert result['csv_filename'] is None
            assert isinstance(result['error'], Exception)
        else:
            assert result['status'] == 0
            assert isinstance(result['csv_filename'], str)
            assert os.path.exists(result['csv_filename'])
            with open(result['csv_filename']) as f:
                contents = f.read()
                f.close()
                assert contents == scenario['contents']
