from setuptools import setup

def readme():
    with open('README.rst') as r:
        return r.read()

setup(name='time_ago',
      version='1.0',
      description='Turns input datetime into fuzzy timestamp format',
      keywords='date time datetime timeago fuzzy',
      url='https://github.com/harshildp/time_ago',
      author='harshildp',
      author_email='harshilp@uw.edu',
      packages=['time_ago'],
      zip_safe=False)