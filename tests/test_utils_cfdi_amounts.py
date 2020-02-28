"""
Test cfdi/utils/cfdi_amounts

"""
import os
import pytest
from tests.resources import scenarios
from cfdi.utils import cfdi_amounts as cfdia


@pytest.fixture(scope='session')
def dir_path():
    return os.path.dirname(
        os.path.realpath(__file__)
    )


def test_get_directory_cfdi_amounts(dir_path):
    for scenario in scenarios.CFDI_AMOUNTS:
        abs_dir_path = os.path.join(
            dir_path, scenario['payload']['dir_path']
        )
        result = cfdia.get_directory_cfdi_amounts(
            abs_dir_path
        )
        print(result)
        if scenario['error']:
            assert result['status'] == 1
            assert result['info'] is None
            assert result['iva_cfdi_amount'] is None
            assert result['total_cfdi_amount'] is None
            assert result['subtotal_cfdi_amount'] is None
            assert isinstance(result['error'], Exception)
        else:
            assert result['status'] == 0
            assert isinstance(result['info'], list)
            assert isinstance(result['iva_cfdi_amount'], float)
            assert isinstance(result['total_cfdi_amount'], float)
            assert isinstance(result['subtotal_cfdi_amount'], float)
            assert result['iva_cfdi_amount'] == \
                scenario['iva_cfdi_amount']
            assert result['total_cfdi_amount'] == \
                scenario['total_cfdi_amount']
            assert result['subtotal_cfdi_amount'] == \
                scenario['subtotal_cfdi_amount']
