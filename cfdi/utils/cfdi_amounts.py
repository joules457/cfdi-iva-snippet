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
        'subtotal_cfdi_amount': 0,
        'discount_cfdi_amount': 0,
        'iva_cfdi_amount': 0,
        'total_cfdi_amount': 0,
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
        discount_amount = 0
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
            tfd = cfdi_bs['bso'].find('tfd:timbrefiscaldigital')
            if voucher is None:
                continue
            vtotal = decimal.Decimal(
                voucher.get('total')
            )
            vdiscount = decimal.Decimal(
                voucher.get('descuento', 0)
            )
            vsubtotal = decimal.Decimal(
                voucher.get('subtotal')
            )
            vdate = voucher.get('fecha')
            vuuid = tfd.get('uuid')
            viva = get_cfdi_iva_amount(cfdi_bs['bso'])
            total_amount += vtotal
            subtotal_amount += vsubtotal
            discount_amount += vdiscount
            iva_amount += viva
            issuer = cfdi_bs['bso'].find('cfdi:emisor')
            issuer_name = issuer.get('nombre')
            issuer_rfc = issuer.get('rfc')
            cfdi_info.append({
                'date': vdate,
                'uuid': vuuid,
                'issuer_name': issuer_name,
                'issuer_rfc': issuer_rfc,
                'subtotal': float(vsubtotal),
                'discount': float(vdiscount),
                'iva': float(viva),
                'total': float(vtotal),
            })
        result['info'] = sorted(cfdi_info, key=lambda x: x['date'])
        result['subtotal_cfdi_amount'] = float(subtotal_amount)
        result['discount_cfdi_amount'] = float(discount_amount)
        result['iva_cfdi_amount'] = float(iva_amount)
        result['total_cfdi_amount'] = float(total_amount)
    except Exception as err:
        result['status'] = 1
        result['info'] = None
        result['subtotal_cfdi_amount'] = None
        result['discount_cfdi_amount'] = None
        result['iva_cfdi_amount'] = None
        result['total_cfdi_amount'] = None
        result['error'] = err
    return result
