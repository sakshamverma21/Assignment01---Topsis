from setuptools import setup, find_packages

setup(
    name="topsis-saksham-102303892",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis_saksham_102303892.topsis:topsis"
        ]
    },
    author="Saksham Verma",
    description="Python package implementing TOPSIS for MCDM problems",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/topsis-saksham-102303892/",
    license="MIT"
)
