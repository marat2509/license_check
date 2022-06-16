import setuptools
setuptools.setup(
    name = "license_check",
    version = "0.1",
    author = "marat2509",
    description = "This module allows you to use it in your program in order to verify the product license key",
    packages = ["license_check"],
    install_requires = ["requests", "loguru"]
)