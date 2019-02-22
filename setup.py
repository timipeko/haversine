
from setuptools import setup

setup(
    name='haversineWrapper',
    version='0.1.0',
    description='Calculate the distance between 2 locations using Google Geolocation API.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    author='Timotej Kovacic',
    author_email='timotej.peter.kovacic@gmail.com',
    url='https://github.com/mapado/haversine',
    packages=['wrapper'],
    license=['GPL'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: FSF :: GPLv3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Mathematics'
    ],
)