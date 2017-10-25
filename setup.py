from setuptools import setup

def readme():
    with open('README.rst') as r:
        return r.read()

setup(name='time-ago',
      version='1.0',
      description='Turns input datetime into fuzzy timestamp format',
      keywords='date time datetime timeago fuzzy'
      url='https://github.com/harshildp/time-ago',
      author='harshildp',
      author_email='harshilp@uw.edu',
      packages=['time-ago'],
      zip_safe=False)