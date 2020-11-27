from pyfuzzysystem import *

puntuality = FuzzyVariable('puntuality')\
    .add('bad',  Z(3, 6))\
    .add('good', S(4, 8))

eficiency = FuzzyVariable('eficiency')\
    .add('poor',     L(3, 5))\
    .add('standar',  Gamma(4, 6))\
    .add('excelent', Gamma(8, 9))

relations = FuzzyVariable('social-relations')\
    .add('low',    Z(1, 5))\
    .add('normal', Gaussian(6, 3))\
    .add('high',   S(8, 10))

salary = FuzzyVariable('salary')\
    .add('type1',  Z(50,75))\
    .add('type2',  Gaussian(70,25))\
    .add('type3',  Gaussian(90,25))\
    .add('type4',  Gaussian(110,25))\
    .add('type5',  Gaussian(130,25))\
    .add('type6',  S(145,200))

salary.graph()

def populate_system(sys_class):
    system = sys_class(centroid)
    system += (puntuality['bad']  & eficiency['poor']     & relations['low'])    >> +salary['type1']
    system += (puntuality['bad']  & eficiency['poor']     & relations['normal']) >> +salary['type2']
    system += (puntuality['bad']  & eficiency['poor']     & relations['high'])   >> +salary['type1']
    system += (puntuality['bad']  & eficiency['standar'])                        >> +salary['type3']
    system += (puntuality['bad']  & eficiency['excelent'] & relations['low'])    >> +salary['type4']
    system += (puntuality['bad']  & eficiency['excelent'] & relations['normal']) >> +salary['type5']
    system += (puntuality['bad']  & eficiency['excelent'] & relations['high'])   >> +salary['type4']
    system += (puntuality['good'] & eficiency['poor']     & relations['low'])    >> +salary['type2']
    system += (puntuality['good'] & eficiency['poor']     & relations['normal']) >> +salary['type3']
    system += (puntuality['good'] & eficiency['poor']     & relations['high'])   >> +salary['type3']
    system += (puntuality['good'] & eficiency['standar']  & relations['low'])    >> +salary['type3']
    system += (puntuality['good'] & eficiency['standar']  & relations['normal']) >> +salary['type5']
    system += (puntuality['good'] & eficiency['standar']  & relations['high'])   >> +salary['type4']
    system += (puntuality['good'] & eficiency['excelent'] & relations['low'])    >> +salary['type5']
    system += (puntuality['good'] & eficiency['excelent'] & relations['normal']) >> +salary['type6']
    system += (puntuality['good'] & eficiency['excelent'] & relations['high'])   >> +salary['type6']
    return system

def main(args):
    d = {
        'puntuality':       args.puntuality,
        'eficiency':        args.eficiency,
        'social-relations': args.relations,
    }
    for x in d.values():
        assert 0 <= x <= 10
    print('Mamdani: ', populate_system(MamdaniSystem).infer(d)['salary'])
    print('Larsen:  ', populate_system(LarsenSystem).infer(d)['salary'])

def show(args):
    print(populate_system(MamdaniSystem))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='pyfuzzysystem-example, ALL INPUTS ARE IN RANGE [0,10]')
    subparsers = parser.add_subparsers()

    run = subparsers.add_parser('run')
    run.add_argument('-p', '--puntuality', type=int, required=True, help='Value of puntuality')
    run.add_argument('-e', '--eficiency',  type=int, required=True, help='Value of puntuality')
    run.add_argument('-r', '--relations',  type=int, required=True, help='Value of puntuality')
    run.set_defaults(command=main)

    rules = subparsers.add_parser('rules')
    rules.set_defaults(command=show)

    args = parser.parse_args()
    try: 
        assert hasattr(args, 'command')
        args.command(args)
    except AssertionError: 
        parser.print_help()
        