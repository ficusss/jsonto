from setuptools import setup, find_packages

with open("requirements.txt", "r") as requirements:
    setup(
        name="jsonto",
        version="0.0.1",
        description="Package for converting json to another format and vice versa",
        long_description="Package for converting json to another format and vice versa",
        author="ficusss",
        maintainer="ficusss",
        packages=find_packages(),
        python_requires='>=3.6',
        install_requires=reqirements.readlines(),
    )
