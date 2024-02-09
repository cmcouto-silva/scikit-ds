from setuptools import setup, find_packages

setup(
    name='scikit-ds',
    version='0.0.1',
    author='Cainã Max Couto da Silva',
    author_email='cmcouto.silva@gmail.com',
    packages=find_packages(),
    license='LICENSE',
    description='Scientific toolkit for data science',
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
    ],
    entry_points={
        'console_scripts': [
            'ds-hello = scikit_ds:hello'
        ]
    }
)
