#!/bin/bash
function do_or_die() {
  $*
  if [ $? != 0 ]; then
    echo "Failed"
    exit 1
  fi
}

if [ -z "${BUILD_NUMBER}" ]; then
BUILD_NUMBER=DEV
fi

# assumes working directory is teamcity configs dir
echo "build.number is ${BUILD_NUMBER}"
pushd ../..
if [ -d ve ]; then
    rm -rf ve
fi
echo "creating virtualenv"
do_or_die virtualenv2.6 ve

echo "installing dependencies"
do_or_die ve/bin/pip install --no-index -r requirements.txt --upgrade
do_or_die virtualenv2.6 --relocatable ve

echo "cleaning"
do_or_die ve/bin/python2.6 setup.py clean

echo "Running tests..."
do_or_die ve/bin/python2.6 ve/bin/nosetests -e handlers
echo "Tests completed succesfully"

echo "Building distribution zip"
do_or_die ve/bin/python2.6 setup.py sdist --formats=zip

echo "Uploading distributon to pypi.gudev.gnl"
cp dist/pyidml-0.3-dev.zip /r2/python_repository/
echo "Cleaning up"

do_or_die rm -rf ve
popd
