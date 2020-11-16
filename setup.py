from setuptools import setup

setup(
    name='csv_xlsx_converter',
    version='0.1',
    py_modules=['csv_xlsx_converter'],
    entry_points={
        'console_scripts': [
            'csv2xlsx = csv_xlsx_converter:csv2xlsx',
            'xlsx2csv = csv_xlsx_converter:xlsx2csv'
        ]
    },
)
