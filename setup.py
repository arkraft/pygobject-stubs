import os
import glob
from setuptools import setup

def build_package_data(package):
    abs_stubs = glob.glob(f'{package}/**/*.py', recursive=True)
    stubs = []
    for f in abs_stubs:
        stubs.append(os.path.relpath(f, package))
    return {package: stubs}


setup(
    name="PyGObject-stubs",
    url="https://github.com/arkraft/pygobject-stubs",
    author="Christoph Reiter",
    author_email="reiter.christoph@gmai.com",
    version="0.0.4",
    package_data=build_package_data("gi-stubs"),
    packages=["gi-stubs"],
    install_requires=["PyGObject"],
)
