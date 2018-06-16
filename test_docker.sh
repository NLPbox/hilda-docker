# This script can be run locally to build the container and run the tests.

# We use this, because we can't build the container and run the tests on Travis CI,
# as HILDA's license doesn't allow that.

docker build -t hilda .
docker run --entrypoint=pytest -ti hilda test_hilda.py
