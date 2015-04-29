from setuptools import setup

setup(name='schnueffelsaltevents',
      version='0.44',
      description='Attaches to a salt-masters event bus and logs all events to a (remote) log collecter',
      url='https://github.com/MrMarvin/schnueffelsaltevents',
      author='Marvin Frick',
      author_email='marvin.frick@sinnerschrader.com',
      license='BSD',
      packages=['schnueffelsaltevents'],
      dependency_links=['https://github.com/MrMarvin/gelfHandler/tarball/master-ng'],
      scripts=['bin/schnueffel-salt-events'],
      zip_safe=False)
