from setuptools import setup, find_packages

setup(
    name='flaskApiJenkins',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'flask_testing'
    ]
)