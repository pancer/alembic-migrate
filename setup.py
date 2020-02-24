"""
Flask-Migrate
--------------

SQLAlchemy database migrations for Flask applications using Alembic.
"""
from setuptools import setup


VERSION = open('__version__').read()

setup(
    name='raw-migrate',
    version=VERSION,
    url='https://github.com/withmehealth/raw-migrate',
    license='MIT',
    author='Filip Dimitrovski',
    author_email='filipdimitrovski22@gmail.com',
    description=('A fork of flask-migrate that is independent.'),
    long_description=__doc__,
    packages=['raw_migrate'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'alembic>=0.7',
        'click'
    ],
    entry_points={
        'entry_point': [
            'r-db = raw_migrate.cli.db'
        ],
    },
    test_suite="tests",
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
