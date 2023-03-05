import argparse


"""
Parser command in script.
Commands for script.
py main.py -a create -m Teacher -n 'Boris Jonson'
py main.py -a create -m Group -n 'AD-101' 
"""


def arg_parser():
    parser = argparse.ArgumentParser(description='A console utility for CRUD operations with a db.')

    parser.add_argument('-a', '--action', type=str, required=True)
    parser.add_argument('-m', '--model', type=str, required=True)
    parser.add_argument('-n', '--name', type=str)
    parser.add_argument('-i', '--id', type=int)

    args = vars(parser.parse_args())  # object -> dict
    command_pars = args.get('action').lower()
    column_pars = args.get('model').lower()
    value_pars = args.get('name')
    id_pars = args.get('id')

    return {"command": command_pars,
            "column": column_pars,
            "value": value_pars,
            "id": id_pars}
