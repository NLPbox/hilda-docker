FROM nlpbox/nlpbox-base:16.04
MAINTAINER Arne Neumann <nlpbox.programming@arne.cl>

RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install -y gcc g++ make python-pip

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

RUN pip install pudb ipython
RUN apt-get install -y openjdk-8-jre

# 2.0.1rc3 this is the newest version of nltk that seems to work with HILDA. 
# We don't install this via pip because this version chokes on the version
# of 'distribute' it requires (0.6.21).
WORKDIR /opt
RUN git clone https://github.com/nltk/nltk
WORKDIR /opt/nltk
RUN git checkout tags/2.0.1rc3 -b nltk-2.0.1rc3

# installing nltk-2.0.1rc3 does not seem to work when setuptools is installed,
# but we'll need it to install pyyaml
RUN apt-get remove -y python-setuptools
RUN python setup.py install

RUN pip install setuptools==30.0.0 && pip install pyyaml==3.12

WORKDIR /opt/hilda
ENTRYPOINT ["python", "hilda.py"]
CMD ["texts/szeryng_wikipedia.txt"]
