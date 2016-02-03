from setuptools import setup, find_packages

setup(
    name='bridge_mgr_rest',
    version='0.1',
    description='bridge manager rest service',
    author='oleksii.iaroshenko',
    author_email='oleksii.iaroshenko@gmail.com',
    install_requires=[
        "pecan",
        "pika",
    ],
    test_suite='bridge_mgr_rest',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages()
)