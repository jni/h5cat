from setuptools import setup

descr = """h5cat: Quick preview of hdf5 files

Quickly check the contents of multiple hdf5 files. Usage:

`h5cat -h`

`h5cat path/to/hdffiles/*.h5`

Note: h5cat is no longer maintained. For similar functionality, see
h5glance at https://pypi.org/project/h5glance/#description
"""

DISTNAME            = 'h5cat'
DESCRIPTION         = 'Quick preview of hdf5 files'
LONG_DESCRIPTION    = descr
MAINTAINER          = 'Juan Nunez-Iglesias'
MAINTAINER_EMAIL    = 'juan.nunez-iglesias@monash.edu'
URL                 = 'https://github.com/jni/h5cat'
LICENSE             = 'BSD 3-clause'
DOWNLOAD_URL        = 'https://github.com/jni/h5cat'
VERSION             = '0.1'
INST_DEPENDENCIES   = []


if __name__ == '__main__':

    setup(name=DISTNAME,
        version=VERSION,
        url=URL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        license=LICENSE,
        py_modules=['h5cat'],
        package_data={},
        install_requires=INST_DEPENDENCIES,
        entry_points = {
            'console_scripts': ['h5cat=h5cat:main']
        }
    )
