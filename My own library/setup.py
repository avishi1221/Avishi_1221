from setuptools import setup, find_packages

setup(
    name="custom_math_lib",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    description="A custom math library for AI, cryptography, and matrix algebra",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/custom_math_lib",
    author="Your Name",
    license="MIT",
)
