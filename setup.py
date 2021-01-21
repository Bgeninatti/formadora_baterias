import setuptools


setuptools.setup(
    name="formadora-pkg-BGENINATTI", # Replace with your own username
    version="0.1.0",
    author="Bruno Geninatti",
    author_email="brunogeninatti@gmail.com",
    description="Utility to interact with the TKL688",
    url="https://bitbucket.org/tklrepo/formadora_baterias",
    packages=setuptools.find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    install_requires=[
    'python-telegram-bot==12.2.0',
    'pyzmq',
    ],
    scripts=['bin/formadora'],
)

