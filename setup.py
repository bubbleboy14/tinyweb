from setuptools import setup

setup(
    name='tinyweb',
    version="0.1.0",
    author='Mario Balibrera',
    author_email='mario.balibrera@gmail.com',
    license='MIT License',
    description='ThINlY WrappEd weB',
    long_description='repackages async dez components like HTTPApplication and SocketController into a minimalist config-driven web (backend) framework',
    packages=[
        'tinyweb'
    ],
    zip_safe = False,
    install_requires = [
        "fyg >= 0.1.7.5",
        "dez >= 0.10.10.42"
    ],
    entry_points = '''''',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
