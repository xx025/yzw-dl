from setuptools import setup

setup(
    name='yzw-dl',
    version='1.0.0-202308111',
    author='xx025',
    packages=['yzw_dl', 'yzw_dl.utils','yzw_dl.data'],
    install_requires=[
        'pydantic',
        'requests_enhance @ git+https://github.com/xx025/requests_enhance.git'
    ],
)
