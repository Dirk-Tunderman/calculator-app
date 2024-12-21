from setuptools import setup, find_packages

setup(
    name="calculator-app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pytest>=7.0.0',
    ],
    author="Dirk Tunderman",
    author_email="your.email@example.com",
    description="A simple calculator implementation in Python",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Dirk-Tunderman/calculator-app",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)