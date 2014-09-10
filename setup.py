import os
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name='vizard_graphs',
      version='0.0.1',
      packages=find_packages(),
      include_package_data=True,
      license='MIT',
      author='Ciudadano Inteligente',
      author_email='lab@ciudadanointeligente.org',
      url='https://ciudadanointeligente.org/',
      description='',
      long_description=open("README.md").read(),
      install_requires=['Django >= 1.4.3', 'jsonfield'],
      tests_require=['Django >= 1.4.3'],
      cmdclass={'test': ""},
      classifiers=[
          'Framework :: Django',
      ],
)
