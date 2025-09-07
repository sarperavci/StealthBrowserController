from setuptools import setup, find_packages

VERSION = "0.1.7"

setup(
    name="stealth-browser-controller",
    version=VERSION,
    description="A stealthy browser automation tool with only screen and mouse",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Sarper AVCI",
    author_email="sarperavci20@gmail.com",
    url="https://github.com/sarperavci/stealth-browser-controller",
    packages=find_packages(exclude=["examples"]),
    install_requires=[
        "pyautogui",
        "human-mouse",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
) 