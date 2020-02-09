from setuptools import setup

setup(
    name='Flask-Banana',
    version='0.1.1',
    packages=['flask_banana'],
    package_data={'flask_banana': ['py.typed']},
    url='https://git.legoktm.com/legoktm/flask-banana',
    python_requires='>=3.5',
    install_requires=['Flask', 'banana-i18n'],
    license='GPL-3.0-or-later',
    author='Kunal Mehta',
    author_email='legoktm@member.fsf.org',
    long_description=open('README.rst').read(),
    description='Integrates the banana i18n library into Flask applications'
)
