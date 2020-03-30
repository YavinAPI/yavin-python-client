from setuptools import find_packages, setup


setup(
    name="yavin",
    version="1.2.0.dev0",
    description="Python API client for the Yavin API",
    long_description="Python API client for the Yavin API",
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