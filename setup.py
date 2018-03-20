from setuptools import setup

setup(
    name='winepair',
    packages=['winepair'],
    include_package_data=True,
    install_requires=[
        'arrow',
        'Flask',
        'Flask-Compress',
        'Jinja2',
        'numpy',
        'pandas',
        'PyMySQL',
        'pyOpenSSL',
        'SQLAlchemy',
        'uWSGI',
    ],
)
