# h5cat: preview the contents of HDF5 files in the command line.

h5cat is a Python script to quickly preview the contents of an HDF5 file.
It is designed to be used in situations where 
[hdfview](http://www.hdfgroup.org/hdf-java-html/hdfview/) is overkill.
It is distributed under the open-source 
[MIT license](http://www.opensource.org/licenses/mit-license.php).

# NOTE: h5cat is no longer maintained

See the excellent `h5glance` for a more modern replacement:

https://pypi.org/project/h5glance/#description

## Requirements (tested versions)

* Python 2.7, 3.5+
* numpy (<2.0)
* h5py (<3.0)

All of the above are included in the Enthought Python Distribution, so I would
recommend you just install that if you can. argparse is required if you are
on Python 2.6 (but it is built in with 2.7).

## Installation

```
pip install h5cat
```

## Usage

### Agglomeration

Run `h5cat -h` for a helpful message.

Here are a couple of examples to get you started.

By default, `h5cat` gives you the shape and type of every dataset in an
HDF5 file.
```
$ h5cat single-channel-tr[0-3]-0-0.00.lzf.h5
>>> single-channel-tr1-0-0.00.lzf.h5

    stack
      shape:  (250, 250, 250) 
      type:  int32

    vi
      shape:  (3, 1) 
      type:  float64
>>> single-channel-tr2-0-0.00.lzf.h5

    stack
      shape:  (250, 250, 250) 
      type:  int32

    vi
      shape:  (3, 1) 
      type:  float64
>>> single-channel-tr3-0-0.00.lzf.h5

    stack
      shape:  (250, 250, 250) 
      type:  int32

    vi
      shape:  (3, 1) 
      type:  float64
```

If you want more details, use `-v` or `--verbose` to get a printout of the
array. For large arrays this will be `...`ed to show only the edges of the
array as can be fit on screen. Use `-g` or `--group` to display only a
specific group of the `.h5` file.
```
$ h5cat -v -g vi single-channel-tr3-0-0.00.lzf.h5
>>> single-channel-tr3-0-0.00.lzf.h5

    vi
      shape:  (3, 1) 
      type:  float64
[[ 0.        ]
 [ 0.06224902]
 [ 2.23062383]]
```
