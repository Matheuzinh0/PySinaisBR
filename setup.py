from setuptools import setup, find_packages
from pathlib import Path

# Leia o conteúdo do README
readme_path = Path(__file__).parent / "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pysinaisbr",
    version="2.0",
    author="Matheus Sousa",
    author_email="matheus.henriquesousa@ufpe.br",
    description="Biblioteca brasileira para processamento de sinais e sistemas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/PySinaisBR",
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
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
        "Intended Audience :: Science/Research",
        "Development Status :: 5 - Production/Stable"
    ],
    python_requires='>=3.8',
    license="MIT",
    license_files=["LICENSE.txt"],
    include_package_data=True,
    keywords=[
        'sinais', 
        'processamento digital',
        'comunicações',
        'transformada fourier',
        'engenharia'
    ],
    project_urls={
        "Documentação": "https://github.com/seu-usuario/PySinaisBR/wiki",
        "Código Fonte": "https://github.com/seu-usuario/PySinaisBR",
        "Tracker de Issues": "https://github.com/seu-usuario/PySinaisBR/issues"
    },
    options={
        'bdist_wheel': {
            'universal': False
        }
    }
)
