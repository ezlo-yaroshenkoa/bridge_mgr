from setuptools import setup, find_packages
from pip.req import parse_requirements
import uuid

install_requires_pip = [str(ir.req) for ir in parse_requirements('requirements.txt', session=uuid.uuid1())]

setup(
    name='bridge_mgr_backend',
    version='0.1',
    description='bridge manager backend',
    author='oleksii.iaroshenko',
    author_email='',
    setup_requires=[
        'setuptools_git >= 0.3'],
    install_requires=install_requires_pip,
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bridge_mgr_backend = bridge_mgr_backend:start_rpc_server',
        ]
    }
)