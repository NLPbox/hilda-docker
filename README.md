# hilda-docker

This docker container allows you to build, install and run the HILDA
RST discourse parser (Hernault et al. 2010) in a docker container.

## Obtaining HILDA

The HILDA parser is available without pay for academic research, but it
can't be downloaded directly. You'll need to sign a license agreement first.
Please contact [Prof. Helmut Prendinger](http://research.nii.ac.jp/~prendinger/).

## Building HILDA

```
git clone https://github.com/nlpbox/hilda-docker
cp hilda_0.9.5_full.tar.gz hilda-docker/
cd hilda-docker
docker build -t hilda .
```

## Running HILDA

To test if parser works, just run ``docker run -ti hilda``.
To run the parser on the file ``/tmp/input.txt`` on your
local machine, run:

```
docker -v /tmp:/tmp -ti hilda-parser /tmp/input.txt
```

The input files should be encoded in UTF-8. Each sentence ending must
be marked with ``<s>`` and each paragraph ending with ``<p>``.


# Citation

Hernault, H., Prendinger, H., DuVerle, D. A., Ishizuka, M., & Paek, T. (2010).  
[HILDA: a discourse parser using support vector machine classification](http://journals.linguisticsociety.org/elanguage/dad/article/download/591/591-2300-1-PB.pdf). Dialogue and Discourse, 1(3), 1-33.
