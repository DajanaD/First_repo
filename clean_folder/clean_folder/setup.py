from setuptools import setup, find_packages
setup(name='sort',
      version='0.1',
      url='https://github.com/DajanaD/First_repo/blob/326846427377c277e77655ebdf2034c41ff6e0b2/sort.py',
      license='MIT',
      author='Diana',
      author_email='ccv080480@gmail.com',
      description='Manage configuration files',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False,
      setup_requires=['nose>=1.0'],
      test_suite='nose.collector')