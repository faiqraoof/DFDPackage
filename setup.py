from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='facewarpingmodulev6',
    version='0.0.1',
    description='Face Warping module',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Faiq Rauf',
    author_email='faiqrauf64@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='deepfakes',
    packages=find_packages(),
    install_requires=[]
)