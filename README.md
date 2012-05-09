# h5cat: preview the contents of HDF5 files in the command line.

h5cat is a Python script to quickly preview the contents of an HDF5 file.
It is designed to be used in situations where 
[hdfview](http://www.hdfgroup.org/hdf-java-html/hdfview/) is overkill.
It is distributed under the open-source 
[MIT license](http://www.opensource.org/licenses/mit-license.php).

## Requirements (tested versions)

* Python 2.x (2.6, 2.7)
* numpy (1.5.1, 1.6.0)
* h5py (1.5.0)

All of the above are included in the Enthought Python Distribution, so I would
recommend you just install that if you can. argparse is required if you are
on Python 2.6 (but it is built in with 2.7).

## Installation

Well, there's nothing to install per se (distutils support coming at some point
in the far future). Download the source and add whatever path you downloaded it
to to your shell path.

## Usage

### Agglomeration

Run `h5cat -h` for a helpful message.

Here are a couple of examples to get you started:


