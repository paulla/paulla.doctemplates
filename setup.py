from setuptools import setup, find_packages
import os

version = '0.1'

here = os.path.abspath(os.path.dirname(__file__))
tests_dir = os.path.join(here, 'src/paulla/doctemplates/tests/docs/')

try:
        README = open(os.path.join(here, 'README.rst')).read()
        TESTS = open(os.path.join(tests_dir, 'index.txt')).read()
        CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
        CONTRIBUTORS = open(os.path.join(here, 'CONTRIBUTORS.txt')).read()
except IOError:
        README = CHANGES = CONTRIBUTORS = TESTS = ''


long_description = README + '\n\n' + TESTS + '\n\n' + CHANGES \
                   + '\n\n'+ CONTRIBUTORS

install_requires=[
    'setuptools',
    'PasteScript',
    'Cheetah',
    'IPy',
    'iniparse'
    ]

tests_require = [
    'Cheetah',
    'PasteScript',
    'IPy']

setup(name='paulla.doctemplates',
      version=version,
      description="Documentation templates hosts PauLLA",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords="pastescript documentation templates for paulla's hosts",
      author='Jean-Philippe Camguilhem',
      author_email='jp_dot_camguolhem_at_gmail_dot_com',
      url='https://github.com/paulla/paulla.doctemplates',
      license='BSD',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir = {'': 'src'},
      namespace_packages=['paulla'],
      include_package_data=True,
      data_files = [('etc', ['src/paulla/doctemplates/etc/defaults.cfg'])],
      zip_safe=False,
      install_requires=install_requires,
      tests_require = tests_require,
      extras_require=dict(test=tests_require),
      test_suite="paulla.doctemplates.tests",
      entry_points=""" # -*- Entry points: -*-
      [paste.paster_create_template]
#      [console_scripts]
      debian = paulla.doctemplates.templates:DebianTemplate
      ubuntu = paulla.doctemplates.templates:UbuntuTemplate
      freebsd = paulla.doctemplates.templates:FreeBsdTemplate
      freebsd-jail = paulla.doctemplates.templates:FreeBsdJailTemplate
      openbsd = paulla.doctemplates.templates:OpenBsdTemplate
      netbsd = paulla.doctemplates.templates:NetBsdTemplate
      """,
      )
