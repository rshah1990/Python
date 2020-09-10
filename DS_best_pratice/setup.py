from setuptools import setup, find_packages
setup(
    name = "preprocess",
    version = "1.0",
    packages = find_packages(),
	test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False
    ) 