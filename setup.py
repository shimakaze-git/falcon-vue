from setuptools import setup, find_packages

VERSION = '0.1'
REQUIRES = ['falcon>=1.4.0']


setup(
    name = 'falcon_vue',
    version = VERSION,
    packages = find_packages(exclude=('tests')),
    test_suite = 'tests',
    author = 'shimakaze-git',
    author_email = "shimakaze.soft@.com",
    description = "An unladen web framework for building APIs and app backends.",
    license = "MIT",
    keywords = "falcon vue falcon-vue falcon_vue",
    url = "",
    python_requires='>=3.4, !=2.7.*',
    install_requires=REQUIRES
)
