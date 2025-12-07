from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='contextuaize',
    version='0.2.0',
    author="Arsen Ohanyan",
    author_email="arsenohanyan@gmail.com",
    description="Smart codebase context extraction for LLMs - with optional AI-powered filtering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ohharsen/contextuaize",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Documentation",
        "Topic :: Utilities",
    ],
    keywords="llm, context, codebase, ai, claude, gpt, documentation, code-analysis",
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'contextuaize = contextuaize:main',
        ],
    },
    extras_require={
        'smart': [],  # No extra deps - uses stdlib urllib for API calls
    },
)