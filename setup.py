from distutils.core import setup
from distutils.core import Command


setup(name='vizard_graphs',
      version='0.0.1',
      packages=['vizard_graphs'],
      license='MIT',
      author='Ciudadano Inteligente',
      author_email='lab@ciudadanointeligente.org',
      url='https://ciudadanointeligente.org/',
      description='',
      long_description=open("README.md").read(),
      install_requires=['Django >= 1.4.3'],
      tests_require=['Django >= 1.4.3'],
      cmdclass={'test': ""},
      classifiers=[
          'Framework :: Django',
      ],
)
