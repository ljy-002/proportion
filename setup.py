import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="proportion-gitignore",  # Replace with your own username
    version="0.0.1",
    author="gitignore",
    author_email="ljy123ljy123@dingtalk.com",
    description="proportion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ljy-002/proportion",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
