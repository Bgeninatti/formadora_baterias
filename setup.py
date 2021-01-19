import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="formadora-pkg-BGENINATTI", # Replace with your own username
    version="0.1.0",
    author="Bruno Geninatti",
    author_email="brunogeninatti@gmail.com",
    description="Utility to interact with the TKL688",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/tklrepo/formadora_baterias",
    packages=setuptools.find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    install_requires=[
    'Pillow',
    'matplotlib',
    'numpy',
    'attrs'
    ],
    python_requires='>=3.4',
    scripts=['bin/formadora'],
)

