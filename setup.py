from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(
    name='grafos-ryan',
    version='0.0.1',
    license='MIT License',
    author='Ryan Samuel',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='ryansamuel262@gmail.com',
    keywords='Parte 1 Grafos PucMg',
    description=u'Parte 1 trabalho grafos',
    packages=['GrafoPt1'],
    install_requires=['requests'],
)
