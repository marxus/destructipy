virtualenv .2 -p 2 && .2/bin/python setup.py sdist bdist_wheel
virtualenv .3 -p 3 && .3/bin/python setup.py sdist bdist_wheel
rm -rf .2 .3
