from setuptools import find_packages, setup
import pathlib

readme = (pathlib.Path(__file__).parent / "README.md").read_text()
changelog = (pathlib.Path(__file__).parent / "CHANGELOG.md").read_text()


setup(
    name="yavin",
    version="1.0.1",
    description="Python API client for the Yavin API",
    long_description="{}\n\n{}".format(readme, changelog),
    long_description_content_type="text/markdown",
    url="https://github.com/yavinapi/yavin-python-client",
    author="Yavin",
    author_email="tech@yavin.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests"
    ],
)