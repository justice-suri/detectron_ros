
from distutils.core import setup
from distutils.core import Extension
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['detectron_ros'],
    package_dir={'': 'src'},
)

setup(**setup_args)
