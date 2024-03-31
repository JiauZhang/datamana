from setuptools import setup, find_packages

setup(
    name = 'datashare',
    packages = find_packages(exclude=['examples']),
    version = '0.0.1',
    license='MIT',
    description = 'Dataset Sharing',
    author = 'JiauZhang',
    author_email = 'jiauzhang@163.com',
    url = 'https://github.com/JiauZhang/datashare',
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type = 'text/markdown',
    keywords = [
        'Deep Learning',
        'Dataset Sharing',
        'Artificial Intelligence',
    ],
    install_requires=[
        'numpy',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)