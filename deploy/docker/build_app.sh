#!/bin/bash
shell_dir=$(dirname $0)
cd ${shell_dir}

echo ${shell_dir}


# docker run -it --rm=true -p 5001:5001 -v /Users/liampro/Downloads/pro/git/meta-liam/python-server/python-build-docker-demo/:/mydata liam1803/python_installer:0.0.1 /mydata/deploy/docker/build_exe.sh

cd publish/

docker  image rm  liam1803/python_installer_ubuntu:0.0.2

docker build -t  liam1803/python_installer_ubuntu:0.0.2 -f Dockerfile-ubuntu .
