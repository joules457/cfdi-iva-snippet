"""
Test cfdi/utils/total_iva_amount

"""
import os
import pytest
from tests.resources import scenarios
from cfdi.utils import total_iva_amount as tia


@pytest.fixture(scope='session')
def dir_path():
    return os.path.dirname(
        os.path.realpath(__file__)
    )


def test_get_directory_total_iva_amount(dir_path):
    for scenario in scenarios.IVA_AMOUNT:
        abs_dir_path = os.path.join(
            dir_path, scenario['payload']['dir_path']
        )
        result = tia.get_directory_total_iva_amount(
            abs_dir_path
        )
        if scenario['error']:
            assert result['status'] == 1
            assert result['info'] is None
            assert result['total_iva_amount'] is None
            assert isinstance(result['error'], Exception)
        else:
            assert result['status'] == 0
            assert isinstance(result['info'], list)
            assert isinstance(result['total_iva_amount'], float)
            assert result['total_iva_amount'] == scenario['total_iva_amount']
    # assert False
