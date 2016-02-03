from setuptools import setup, find_packages

setup(
    name='bridge_mgr_cli',
    version='0.1',
    description='bridge manager backend',
    author='oleksii.iaroshenko',
    author_email='oleksii.iaroshenko@gmail.com',
    install_requires=[
        "pika",
    ],
    zip_safe=False,
    include_package_data=True,
    packages=find_packages()
)