from setuptools import setup

setup(
    name="cxxd",
    version="1.0.0",
    description="A colorized drop-in replacement for xxd.",
    author="Sai Kalidindi",
    url="https://github.com/anowlcalledjosh/cxxd",
    license="MIT",
    classifiers=[
        "Environment :: Console",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    py_modules=["cxxd"],
    entry_points={"console_scripts": ["cxxd=cxxd:main"]},
)
