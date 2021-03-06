from setuptools import dist, find_packages
dist.Distribution().fetch_build_eggs(['wheel', 'cmake_setuptools'])
ctypesgen_install = dist.Distribution().fetch_build_egg('ctypesgen')

dist.Distribution().fetch_build_eggs(['cmake_setuptools', 'scikit-build'])

from skbuild import setup    
import os

import subprocess
version = subprocess.check_output(["git", "describe", "--tags", "--long"]).strip().decode('utf-8').replace("-", ".")[1:]
version = version[:version.rfind("g")-1]

setup(name='pysurvive',
      description='',
      version=version,
      packages=['pysurvive'],
      package_dir={'pysurvive': 'bindings/python/pysurvive'},
      include_package_data=True,
      cmake_args=['-DPYTHON_GENERATED_DIR="'+ os.path.dirname(os.path.abspath(__file__))+'/bindings/python/pysurvive/"']
      )
