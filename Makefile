clean:
	python dev/clean.py

deps:
	pip install -r requirements.txt --upgrade

deploy: clean pypi
	git push --tags
	twine upload -r pypi dist/*
	python dev/clean.py

pypi: clean
	python setup.py sdist bdist_wheel

register:
	python setup.py register -r pypi
