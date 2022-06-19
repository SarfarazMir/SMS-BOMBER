from setuptools import setup, find_packages

setup(
    name='sms-bomber',
    version='0.2.2',
    packages=find_packages(),
    install_requires=['requests', 'requests[socks]', 'stem', 'colorama'],
    url='',
    license='',
    author='Sarfaraz Mir',
    author_email='sfmir000@gmail.com',
    description=''
)
