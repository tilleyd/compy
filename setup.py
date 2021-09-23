from setuptools import setup

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
    packages=["compy"],
    include_package_data=True,
    install_requires=requirements,
)
