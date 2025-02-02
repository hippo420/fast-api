from setuptools import setup, find_packages

setup(
    name="fast_gaebabja_api",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pandas",
        "lxml",
        "finance-datareader",
        "beautifulsoup4",
    ],
)
