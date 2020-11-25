from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="identity-number-validator",
    version="0.0.5",
    author="David Armendariz",
    author_email="davidarmendariz1998@gmail.com",
    description=
    "A package for validating identity numbers from different countries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DavidArmendariz/identity-number-validator-python",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords="identity, cedula, ecuador")
