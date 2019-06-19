from setuptools import setup

setup(
    name='host-manager',
    version='1.0.0',
    packages=['hostman'],
    url='https://github.com/thomxc/host-manager',
    license='MIT',
    author='Thomas Wiersema',
    author_email='thomas.wiersema@gmail.com',
    description='Generates a hosts file to minimize ads on the web while keeping your custom host entries',
    scripts=['bin/hostman']
)
