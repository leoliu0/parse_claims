from distutils.core import setup

setup(
    name="parse_claims",  # How you named your package folder (MyLib)
    package="parse_claims",
    version="0.1",  # Start with a small number and increase it with every change you make
    author="Leo Liu",  # Type in your name
    install_requires=[
        "loguru",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Programming Language :: Python :: 3",  # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
