import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chiyi",
    version="0.0.1",
    author="chiyi",
    author_email="chishishuan@163.com",
    description="Python wrapper for chiyi: natural language processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: os Independent",
    ],

)