"""
Total CFDI Amounts

"""
import os
import decimal
from cfdi.utils import constants as ccfdi
from cfdi.utils import directory as dir_utils
from cfdi.utils import beautifulsoup as bs_utils
from cfdi.utils.total_iva_amount import get_cfdi_iva_amount


decimal.getcontext().prec = 8


def get_directory_cfdi_amounts(my_dir: str):
    result = {
        'status': 0,
        'info': [],
        'iva_cfdi_amount': 0,
        'total_cfdi_amount': 0,
        'subtotal_cfdi_amount': 0,
    }
    try:
        cfdi_files = dir_utils.get_directory_files(
            my_dir,
            ccfdi.XML_PATTERN
        )
        if cfdi_files['status'] == 1:
            raise cfdi_files['error']
        # print(cfdi_files)
        total_amount = 0
        subtotal_amount = 0
        iva_amount = 0
        cfdi_info = []
        for cfdi in cfdi_files['files']:
            cfdi_bs = bs_utils.load_file_to_bso(
                os.path.join(my_dir, cfdi),
                ccfdi.BS_PARSER
            )
            if cfdi_bs['status'] == 1:
                raise cfdi_bs['error']
            voucher = cfdi_bs['bso'].find('cfdi:comprobante')
            if voucher is None:
                continue
            vtotal = decimal.Decimal(
                voucher.get('total')
            )
            vsubtotal = decimal.Decimal(
                voucher.get('subtotal')
            )
            viva = get_cfdi_iva_amount(cfdi_bs['bso'])
            total_amount += vtotal
            subtotal_amount += vsubtotal
            iva_amount += viva
            issuer = cfdi_bs['bso'].find('cfdi:emisor')
            issuer_name = issuer.get('nombre')
            issuer_rfc = issuer.get('rfc')
            cfdi_info.append({
                'issuer_name': issuer_name,
                'issuer_rfc': issuer_rfc,
                'iva': float(viva),
                'total': float(vtotal),
                'subtotal': float(vsubtotal),
            })
        result['info'] = cfdi_info
        result['iva_cfdi_amount'] = float(iva_amount)
        result['total_cfdi_amount'] = float(total_amount)
        result['subtotal_cfdi_amount'] = float(subtotal_amount)
    except Exception as err:
        result['status'] = 1
        result['info'] = None
        result['iva_cfdi_amount'] = None
        result['total_cfdi_amount'] = None
        result['subtotal_cfdi_amount'] = None
        result['error'] = err
    return result
