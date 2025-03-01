from setuptools import setup, find_packages

setup(
    name="pysinaisbr",
    version="2.0",
    author="Matheus Sousa",
    author_email="matheus.henriquesousa@ufpe.br",
    description="Biblioteca brasileira para processamento de sinais e sistemas",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Matheuzinh0/PySinaisBR",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        'numpy>=1.21',
        'scipy>=1.7',
        'matplotlib>=3.5',
        'pywavelets>=1.3',
        'reedsolo>=1.5',
        'numba>=0.55'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
