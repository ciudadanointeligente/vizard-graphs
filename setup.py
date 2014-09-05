from distutils.core import setup

setup(name='vizard_graphs',
      version='0.0.1',
      packages=['vizard_graphs'],
      package_data = {'vizard_graphs': ['templates/*.html','static/*',],},
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
