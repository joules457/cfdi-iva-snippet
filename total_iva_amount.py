#!/usr/bin/env python
"""
Total IVA amount

"""
import sys
import argparse
from cfdi.utils import directory as dir_utils
from cfdi.utils import beautifulsoup as bs_utils


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


# Shell args!!!
script_args = vars(parser.parse_args())


def main(my_args):
    my_status = True
    try:
        pass
    except Exception as err:
        print('ERR: ', err)
        my_status = False
    return my_status


if __name__ == "__main__":
    print('TTT', script_args)
    my_status = 0 if main(script_args) is True else 1
    print('Exiting with status code', my_status)
    sys.exit(my_status)
