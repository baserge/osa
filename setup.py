from setuptools import setup, find_packages
import sys

CLASSIFIERS = """\
Development Status :: 5 - Production/Stable
Environment :: Console
Environment :: Web Environment
Intended Audience :: Developers
Intended Audience :: End Users/Desktop
License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python
Topic :: Internet
Topic :: Internet :: WWW/HTTP
Topic :: Software Development :: Libraries
Topic :: Software Development :: Object Brokering""".split("\n")

setup(
    name='osa',
    version='0.2.1',
    description='Python fast/slim/convenient SOAP/WSDL client.',
    author="Sergey A. Bozhenkov",
    author_email='ba-serge@yandex.ru',
    url="https://github.com/baserge/osa",
    download_url="https://github.com/baserge/osa/archive/master.zip",
    packages=["osa",],
    license="LGPLv3",
    classifiers=CLASSIFIERS,
    )
