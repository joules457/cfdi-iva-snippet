# cfdi-iva-snippet
Script for process all CFDI xml files on a given path, computing total amount of "IVA"

## Installation

Just Run
```shell
pip install -r requirements.txt

```

## Usage

For total amount just run
```Shell
# As python script
python total_iva_amount.py -d /home/cfdi/2020/01 --verbose

```

For CFDI Directory info
```Shell
# As python script
python cfdi_directory.py -d /home/cfdi/2020/01 -v  -e

```

### Run tests

Just run
```Shell
# Using pytest
pytest tests --verbose

```
