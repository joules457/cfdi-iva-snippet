"""
IVA Amount

"""
import os
import decimal
from cfdi.utils import constants as ccfdi
from cfdi.utils import directory as dir_utils
from cfdi.utils import beautifulsoup as bs_utils

decimal.getcontext().prec = 8


def get_directory_total_iva_amount(my_dir: str):
    """GEt Total IVA amount for given directory.

    Parameters
    ----------
    my_dir : str
        CFDIs directory.

    Returns
    -------
    dict
        REsult dict {status, info, total_iva_amount}.

    """
    result = {
        'status': 0,
        'info': [],
        'total_iva_amount': 0,
    }
    try:
        cfdi_files = dir_utils.get_directory_files(
            my_dir,
            ccfdi.XML_PATTERN
        )
        if cfdi_files['status'] == 1:
            raise cfdi_files['error']
        total_amount = 0
        cfdi_info = []
        for cfdi in cfdi_files['files']:
            cfdi_bs = bs_utils.load_file_to_bso(
                os.path.join(my_dir, cfdi),
                ccfdi.BS_PARSER
            )
            if cfdi_bs['status'] == 1:
                raise cfdi_bs['error']
            issuer = cfdi_bs['bso'].find('cfdi:emisor')
            iva_amount = get_cfdi_iva_amount(cfdi_bs['bso'])

            if iva_amount > 0:
                total_amount += decimal.Decimal(iva_amount)
                issuer_name = issuer.get('nombre')
                issuer_rfc = issuer.get('rfc')
                cfdi_info.append({
                    'issuer_name': issuer_name,
                    'issuer_rfc': issuer_rfc,
                    'iva_amount': float(iva_amount),
                })
            result['info'] = cfdi_info
            result['total_iva_amount'] = float(total_amount)

    except Exception as err:
        result['status'] = 1
        result['info'] = None
        result['total_iva_amount'] = None
        result['error'] = err

    return result


def get_cfdi_iva_amount(cfdi_bso):
    """GEt CFDI IVA AMOUNT by CFDI BeautifulSoup Object.

    Parameters
    ----------
    cfdi_bso : BeautifulSoup
        CFDI BeautifulSoup Object.

    Returns
    -------
    Decimal
        CFDI IVA amount.

    """
    total_amount = 0
    taxes = []
    for tmp in cfdi_bso.find_all('cfdi:impuestos'):
        taxes = tmp.find_all(
            'cfdi:traslado',
            attrs={'impuesto': '002'}
        )
    for tax in taxes:
        amount = tax.get('importe')
        if amount is not None:
            total_amount += decimal.Decimal(amount)
    return total_amount
