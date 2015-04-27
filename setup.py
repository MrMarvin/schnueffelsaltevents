from setuptools import setup

setup(name='schnueffelsaltevents',
      version='0.42',
      description='Attaches to a salt-masters event bus and logs all events to a (remote) log collecter',
      url='https://github.com/MrMarvin/schnueffelsaltevents',
      author='Marvin Frick',
      author_email='marvin.frick@sinnerschrader.com',
      license='BSD',
      packages=['schnueffelsaltevents'],
      zip_safe=False)
