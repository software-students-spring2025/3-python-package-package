from setuptools import setup, find_packages

setup(
    name='magic8ball',
    version='0.1.0',
    author='Team Package',
    description='A lighthearted fortune-telling package',
    packages=find_packages(),
    include_package_data=True,
    package_data={'magic8ball': ['data.json']},
    install_requires=[],
    classifiers=[],
)
