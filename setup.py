import re
import os
from setuptools import setup


version = '1.0.0'

description = ''
with open('README.md', 'rb') as file:
    description = file.read().decode('utf-8')

setup(name='mes2hb',
    version=version,
    description='Convert optical density data (red and infrared) from functional near infrared spectrope (fNIRS) to oxy, de-oxy haemoglobin concentrations using modified Beer-Lambert law.',
    long_description=description,
    url='http://kaunild.github.io',
    author='Kaunil Dhruv',
    author_email='dhruv.kaunil@gmail.com',
    license='BSD',
    packages=['mes2hb']
)
