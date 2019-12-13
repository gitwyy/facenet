"""Setup script for object_detection."""

from setuptools import find_packages
from setuptools import setup


REQUIRED_PACKAGES = ['scipy>=1.0.0', 'scikit-learn>=0.22', 'h5py>=0.28.1', 'opencv-python>=4.1.2.30',
                     'matplotlib>=3.0.3', 'Pillow>=6.2.1', 'requests>=2.22.0', 'psutil>=5.6.7']

setup(
    name='facenet',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    # package_dir={'': 'src'},
    package_data={'facenet': ['align/*.npy'], },
    packages=[p for p in find_packages() if p.startswith('facenet')],
    description='facenet model by tensorflow',
)
