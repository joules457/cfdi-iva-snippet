#!/usr/bin/env python
"""
Total IVA amount

"""
import sys
import argparse
from tabulate import tabulate
from cfdi.utils import total_iva_amount as tia


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


# Shell args!!!
script_args = vars(parser.parse_args())


def main(my_args):
    my_status = True
    total_table = []
    try:
        print('CFDI Directory: ', my_args['directory'])
        total_amount = tia.get_directory_total_iva_amount(
            my_args['directory']
        )
        if total_amount['status'] == 1:
            raise total_amount['error']
        if my_args['verbose']:
            print(
                tabulate(total_amount['info'], headers='keys')
            )
        total_table.append({
            'total': 'IVA Amount',
            'amount': total_amount['total_iva_amount']
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
