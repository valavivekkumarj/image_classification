from setuptools import find_packages

with open("C:\Cat_Dog_classification\\requirements.txt") as f:
    requirements = f.read.splitlines()

setup(
    name="Cat-Dog",
    version="0.0.1",
    author="suzal",
    packages=find_packages(),
    install_requires=[requirements],
)
