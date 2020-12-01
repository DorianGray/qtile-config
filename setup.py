import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qtile_config",
    version="0.0.1",
    author="Drew Ditthardt",
    author_email="drew.ditthardt@gmail.com",
    description="Drew's qtile config",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DorianGray/qtile-config",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
