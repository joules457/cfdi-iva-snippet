"""
Export Utils

"""
import os
import csv


def csv_file(dict_list: list, filename: str):
    """write a CSV File with given filename and data.

    Parameters
    ----------
    dict_list : list
        List of dicts.
    filename : str
        FIlename.

    Returns
    -------
    dict
        Result {status, csv_filename}.

    """
    result = {
        'status': 0,
        'csv_filename': None
    }
    try:
        fieldnames = dict_list[0].keys() if dict_list else []
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=fieldnames,
                quoting=csv.QUOTE_MINIMAL
            )
            writer.writeheader()
            for row in dict_list:
                writer.writerow(row)
        result['csv_filename'] = filename
    except Exception as err:
        result['status'] = 1
        result['error'] = err
    return result
