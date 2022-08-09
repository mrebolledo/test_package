
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='test_package',
    version='0.0.1',
    author='Mrebolledo',
    author_email='maxi.rebolledo@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mrebolledo/helpers',
    project_urls={
        "Bug Tracker": "https://github.com/mrebolledo/helpers/issues"
    },
    license='MIT',
    packages=['test_package'],
    install_requires=[],
)