from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
	long_description_readme = readme_file.read()

requirements = [
		"pandas>=1.0.1"
		]

setup(
	author = "Abhishek R",
	author_email = "abhishek@pluto7.com",


	name = "feature_engineering_package",
	version = '0.1.0',
	description = "A simple package with all basic files in the structure",
	long_description = long_description_readme,
	

	install_requires = requirements,
	packages = find_packages(),
	include_packages_data = True,
	python_requires = ">=3.7"
	
)
