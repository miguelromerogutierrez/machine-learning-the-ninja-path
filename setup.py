from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Machine Learning the Ninja Path'
LONG_DESCRIPTION = 'This package is used to learn the basics of machine learning'

setup(
       # El nombre debe coincidir con el nombre de la carpeta
       #'modulomuysimple'
        name="machine-learning-the-ninja-path", 
        version=VERSION,
        author="Miguel Romero",
        author_email="<miguel.angel.romero.gtz@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        
        keywords=['python', 'primer paquete'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
