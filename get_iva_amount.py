"""
GEt total IVA amount

"""
import re
import os
import decimal
from cfdi.utils import directory as dir_utils
from cfdi.utils import beautifulsoup as bs_utils

decimal.getcontext().prec = 8

XML_PATTERN = re.compile('.+\\.(xml)$', re.I)

path_to_root, filename = os.path.split(os.path.realpath(__file__))
path_to_resources = os.path.join(
    path_to_root, 'cfdi/resources'
)

cfdi_files = dir_utils.list_directory_files(path_to_resources, XML_PATTERN)

total_amount = 0

for cfdi in cfdi_files:
    cfdi_bs = bs_utils.load_file(
        dir_utils.get_absolute_filename(cfdi, path_to_resources),
        'html.parser'
    )
    issuer = cfdi_bs.find('cfdi:emisor')
    taxes = cfdi_bs.find_all('cfdi:impuestos')
    print('???', taxes)
    # taxes = cfdi_bs.find_all('cfdi:traslado', attrs={'impuesto': '002'})
    for tax in taxes:
        issuer_name = issuer.get('nombre')
        amount = tax.get('importe')
        if amount is not None:
            total_amount += decimal.Decimal(amount)
            print(
                '-', issuer_name, amount
            )

print('total IVA amount:', total_amount)
