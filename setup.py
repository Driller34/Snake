from setuptools import setup

setup(
    name="PySnake",
    version="0.1.0",
    packages=["src"],
    install_requires=[
        "pygame-ce"
    ],
    entry_points={
        "console_scripts": [
            "pysnake = src.main:main",
        ],
    },
)