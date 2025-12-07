from setuptools import setup, find_packages

# Read your README for the long description on PyPI
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='contextuaize',
    version='0.1.0',
    author="Arsen Ohanyan",
    author_email="arsenohanyan@gmail.com",
    description="A CLI tool to flatten codebases for LLM context",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ohharsen/contextuaize",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'contextuaize = contextuaize:main',
        ],
    },
)