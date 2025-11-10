from setuptools import setup

setup(
    name='babyweb',
    version="0.1.1.2",
    author='Mario Balibrera',
    author_email='mario.balibrera@gmail.com',
    license='MIT License',
    description='Basic Asynchronous weB librarY',
    long_description='repackages async dez components like HTTPApplication and SocketController into a minimalist config-driven web (backend) framework',
    packages=[
        'babyweb',
        'babyweb.util'
    ],
    zip_safe = False,
    install_requires = [
        "fyg >= 0.1.7.6",
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
