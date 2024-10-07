from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='cookies_converter',
    version='0.3.2',
    author='REDKLAUS',
    author_email='reallifestd@gmail.com',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/RedKlaus/cookies_converter',
    packages=find_packages(),
    install_requires=['pydantic~=2.8.2'],
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='cookies_converter',
    project_urls={
        'Write me': 'https://t.me/REDKLAUS'
    },
    python_requires='>=3.12'
)
