from setuptools import setup, find_packages

setup(
    name="stealth-browser-controller",
    version="0.1.0",
    description="A stealthy browser automation tool with only screen and mouse",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Sarper AVCI",
    author_email="sarperavci20@gmail.com",
    url="https://github.com/sarperavci/stealth-browser-controller",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["pyautogui", "human-mouse"],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
) 