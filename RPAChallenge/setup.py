from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'selenium',
    ],
    entry_points={
        'console_scripts': [
            'my_command=my_package.module:main_function',
        ],
    },
    author='Seu Nome',
    author_email='seu.email@example.com',
    description='Uma breve descrição do pacote',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/seu_usuario/seu_repositorio',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
