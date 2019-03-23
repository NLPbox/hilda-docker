FROM alpine:3.8 as builder

RUN apk update && apk add git gcc g++ make

# We can't distribute the HILDA parser.
#
# You'll need to sign a license agreement with the Prendinger lab and
# get the parser from them.
# Please contact Prof. Helmut Prendinger <helmut@nii.ac.jp>
ADD hilda_0.9.5_full.tar.gz /opt/hilda/

WORKDIR /opt/hilda/svm_tools
RUN gcc -o svm-scale svm-scale.c

WORKDIR /opt/hilda/svm_tools/liblinear
RUN make clean && make

WORKDIR /opt/hilda/svm_tools/libsvm
RUN make clean && make

# 2.0.1rc3 is the newest version of nltk that seems to work with HILDA. 
# We don't install this via pip because this version chokes on the version
# of 'distribute' it requires (0.6.21). We only clone the specific tag,
# because cloning the complete history takes a long time.
WORKDIR /opt/hilda
RUN git clone -b '2.0.1rc3' --single-branch --depth 1 https://github.com/nltk/nltk.git

# installing nltk-2.0.1rc3 would fail with "urllib2.HTTPError: HTTP Error 403: SSL is required"
# because it is trying to download "distribute" using HTTP instead of HTTPS
WORKDIR /opt/hilda/nltk
RUN sed -i 's/http/https/g' distribute_setup.py

WORKDIR /opt/hilda
ADD hilda_wrapper.py input_*.txt test_hilda.py /opt/hilda/

# minimal modification to the original HILDA parser to work with parse trees as nltk Tree objects
RUN sed -i 's/print out/#print out/g' hilda.py && \
    sed -i 's/return 0/return pt/g' hilda.py


# keep only the stuff we need to run (and test) HILDA
FROM alpine:3.8

# pyyaml is needed for nltk, pytest and sh are only needed to run the test.
RUN apk update && \
    apk add git python2 py2-pip openjdk8-jre-base && \
    pip install pyyaml==3.12 pytest==3.5.1

WORKDIR /opt/hilda
COPY --from=builder /opt/hilda .

# Installing nltk-2.0.1rc3 does not seem to work when setuptools is installed,
# but we'll need it to install pyyaml.
# Afterwards, we'll install nltk's punkt tokenizer, as HILDA only accepts
# sentence-split input (with sentence endings marked as '<s>').
WORKDIR /opt/hilda/nltk
RUN apk del py-setuptools py2-pip && \
    python setup.py install && \
    python -c "import nltk; dl = nltk.downloader.Downloader('https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml'); dl.download('punkt')"

WORKDIR /opt/hilda
ENTRYPOINT ["./hilda_wrapper.py"]
CMD ["input_long.txt"]
