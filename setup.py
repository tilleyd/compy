from setuptools import setup, find_packages

requirements = [
    "numpy",
    "matplotlib",
]

setup(
    name="compy",
    version="1.0",
    description="Personal package containing commonly used functions",
    author="Duncan Tilley",
    url="https://github.com/tilleyd/compy",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
)
