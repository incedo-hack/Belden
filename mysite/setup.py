from distutils.core import setup

setup(
    name='LFA',
    version='1.0',
    packages=['myapp', 'myapp.migrations', 'mysite'],
    url='',
    license='GPL',
    author='saurabh',
    author_email='',
    description='',
    install_requires=[
              'Django==1.11.9', "django-tables2==1.18.0",
    ]
)
