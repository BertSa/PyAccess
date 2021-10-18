import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='py_access',
    version='0.0.2',
    python_requires='>3.7',
    packages=find_packages(),
    url='https://github.com/BertSa/PyAccess',
    license='',
    author='bertsa',
    author_email='bertsa.pro@gmail.com',
    description='This is an app I made specifically for me but I made it public beacause it could be useful for some '
                'people.',
    long_description=read('README'),
    install_requires=[
        'PyGObject>=3.42.0',
        'pyperclip>=1.8.2',
    ],
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Operating System :: Linux :: Ubuntu 20.x',
        'Programming Language :: Python',
        'Topic :: Office/Business',
    ],
)
