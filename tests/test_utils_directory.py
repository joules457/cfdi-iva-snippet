"""
Test cfdi/utils/directory

"""
import os
import json
import pytest
from tests.resources import scenarios
from cfdi.utils import directory as dir_utils


@pytest.fixture(scope='session')
def dir_path():
    return os.path.dirname(
        os.path.realpath(__file__)
    )


def test_get_directory_files(dir_path):
    for scenario in scenarios.DIRECTORY_FILES:
        abs_path = os.path.join(dir_path, scenario['payload']['path'])
        result = dir_utils.get_directory_files(
            abs_path,
            scenario['payload']['include_pattern']
        )
        if scenario['error']:
            assert result['status'] == 1
            assert result['files'] is None
            assert isinstance(result['error'], Exception)
        else:
            assert result['status'] == 0
            assert isinstance(result['files'], list)
            assert json.dumps(result['files'].sort()) == \
                json.dumps(scenario['result'].sort())
        # print(result)
