from setuptools import setup


def readme():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name="smooth",
    version="0.1.2",
    description="Data approximation using a cubic smoothing spline",
    long_description=readme(),
    long_description_content_type='text/markdown',
    license="MIT License",
    url="https://github.com/kevinmmendez/smooth",
    packages=["smooth"],
    python_requires='>=3.5',
    install_requires=[
        "numpy",
        "pandas",
        "scipy"],
    author='Kevin Mendez, David Broadhurst',
    author_email='k.mendez@ecu.edu.au, d.broadhurst@ecu.edu.au',
)
