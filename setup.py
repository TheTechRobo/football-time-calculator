"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here/'README.md').read_text(encoding='utf-8')

setup(
    name='footballTimeCalculator',  # Required

    version='1.0.0',  # Required

    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',

    url='https://github.com/thetechrobo/football-time-calculator',  # Optional

    # This should be your name or the name of the organization which owns the
    # project.
    author='TheTechRobo',  # Optional

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Alpha',

        # Pick your license as you wish
        'License :: OSI Approved :: GNU GPLv3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],

    packages=find_packages(),

    python_requires='3',

    project_urls={  # Optional
        'Issue tracker': 'https://github.com/thetechrobo//football-time-calculator/issues',
        'Say Thanks!': 'https://saythanks.io/to/thetechrobo%40outlook.com',
        'Source': 'https://github.com/thetechobo/football-time-calculator/',
    },
)
