from setuptools import setup, find_packages

setup(
    name="arcade",  # Package name
    version="0.1.0",  # Version
    description="Radiative transfer disk modeling",  # Short description
    long_description=open("README.md").read(),  # Long description (usually from README)
    long_description_content_type="text/markdown",  # Content type for the long description
    author="Blake Drechsler",  # Author name
    author_email="wbd814@gmail.com",  # Author email
    url="https://github.com/bdrechsler/arcade.git",  # URL of the project
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=["requests>=2.25.1", "numpy>=1.21.0"],  # List of dependencies
    classifiers=[  # Classifiers for package metadata
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version requirement
    # entry_points={                          # Optional: for command-line tools
    #     "console_scripts": [
    #         "your_command=your_package_name.module:function",  # e.g., `your_command` is callable in CLI
    #     ],
    # },
    include_package_data=True,  # Include additional files as specified in MANIFEST.in
    license="MIT",  # License type
)
