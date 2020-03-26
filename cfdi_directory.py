#!/usr/bin/env python
"""
CFDI Info

"""
import os
import sys
import argparse
from tabulate import tabulate
from cfdi.utils import export as export_utils
from cfdi.utils import cfdi_amounts as cfdia


def get_directory_path():
    """Get directory path.

    Parameters
    ----------

    Returns
    -------
    str
        Directory path.

    """
    return os.path.dirname(
        os.path.realpath(__file__)
    )


EXPORT_FILENAME = os.path.join(
    get_directory_path(), 'cfdi_directory.csv'
)


parser = argparse.ArgumentParser(
    description="""
    This script determines the IVA total amount for given directory
    """
)
parser.add_argument(
    '-dir',
    '--directory',
    type=str,
    help='CFDI\'s directory: /home/2020/january/received/cfdi',
    required=True
)
parser.add_argument(
    '-v',
    '--verbose',
    action='store_true',
    help='Print Verbose Info',
    required=False
)
parser.add_argument(
    '-e',
    '--export',
    action='store_true',
    help='Export scan result to cfdi_directory.csv file',
    required=False
)


# Shell args!!!
script_args = vars(parser.parse_args())


def main(my_args):
    my_status = True
    # data_table = []
    total_table = []
    try:
        print('CFDI Directory: ', my_args['directory'])
        cfdi_amounts = cfdia.get_directory_cfdi_amounts(
            my_args['directory']
        )
        if cfdi_amounts['status'] == 1:
            raise cfdi_amounts['error']
        if my_args['export']:
            export_utils.csv_file(
                cfdi_amounts['info'],
                EXPORT_FILENAME
            )
        if my_args['verbose']:
            print(
                tabulate(cfdi_amounts['info'], headers='keys')
            )
        total_table.append({
            'total': 'Subtotal',
            'amount': cfdi_amounts['subtotal_cfdi_amount']
        })
        total_table.append({
            'total': 'Discount',
            'amount': cfdi_amounts['discount_cfdi_amount']
        })
        total_table.append({
            'total': 'IVA',
            'amount': cfdi_amounts['iva_cfdi_amount']
        })
        total_table.append({
            'total': 'Total',
            'amount': cfdi_amounts['total_cfdi_amount']
        })

        print(
            tabulate(total_table)
        )
    except Exception as err:
        print('ERR: ', err)
        my_status = False
    return my_status


if __name__ == "__main__":
    my_status = 0 if main(script_args) is True else 1
    sys.exit(my_status)
