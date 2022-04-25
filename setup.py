import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-package-YOUR-USERNAME-HERE",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="play rsp ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Go-davi/rsp_pakage",
    project_urls={
        "Bug Tracker": "https://github.com/Go-davi/rsp_pakage/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "pakage_rsp"},
    packages=setuptools.find_packages(where="pakage_rsp"),
    python_requires=">=3.6",
)