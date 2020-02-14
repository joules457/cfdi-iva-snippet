#!/usr/bin/env python
"""
Total IVA amount

"""
import sys
import argparse
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
    try:
        print('CFDI Directory: ', my_args['directory'])
        total_amount = tia.get_directory_total_iva_amount(
            my_args['directory']
        )
        if total_amount['status'] == 1:
            raise total_amount['error']
        if my_args['verbose']:
            for item in total_amount['info']:
                print(
                    item['issuer_name'],
                    item['iva_amount'],
                )
        print(
            'Total IVA Amount: ',
            total_amount['total_iva_amount']
        )
    except Exception as err:
        print('ERR: ', err)
        my_status = False
    return my_status


if __name__ == "__main__":
    my_status = 0 if main(script_args) is True else 1
    # print('Exiting with status code', my_status)
    sys.exit(my_status)
