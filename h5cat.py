#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import print_function
import argparse
import h5py
from numpy import array

arguments = argparse.ArgumentParser(add_help=False)
arggroup = arguments.add_argument_group('HDF5 cat options')
arggroup.add_argument('-g', '--group', metavar='GROUP',
    help='Preview only path given by GROUP')
arggroup.add_argument('-v', '--verbose', action='store_true', default=False,
    help='Include array printout.')


def main():
    parser = argparse.ArgumentParser(
        description='Preview the contents of an HDF5 file',
        parents=[arguments]
    )
    parser.add_argument('fin', nargs='+', help='The input HDF5 files.')

    args = parser.parse_args()
    for fin in args.fin:
        print('>>>', fin)
        f = h5py.File(fin, 'r')
        if args.group is not None:
            groups = [args.group]
        else:
            groups = []
            f.visit(groups.append)
        for g in groups:
            print('\n   ', g)
            if type(f[g]) == h5py.Dataset:
                a = f[g]
                print('      shape: ', a.shape, '\n      type: ', a.dtype)
                if args.verbose:
                    a = array(f[g])
                    print(a)


if __name__ == '__main__':
    main()
