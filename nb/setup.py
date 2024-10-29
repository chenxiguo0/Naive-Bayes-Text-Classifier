import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()
setuptools.setup(
    name='nb',
    version='0.0.1',
    author='Chenxi Guo',
    author_email='cg1372@georgetown.edu',
    description='nb.py package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    extras_requres={"dev": ["pytest", "flake8", "autopep8"]},
)
