# 发布

## 打linux执行包

### 自动打dist文件

docker run -it --rm=true -p 5001:5001 -v /Users/liampro/Downloads/pro/git/meta-liam/python-server/python-build-docker-demo/:/mydata liam1803/python_installer:0.0.1 /mydata/deploy/docker/build_exe.sh

### 手工测试Installer

docker run -it --rm=true -p 5001:5001 -v /Users/liampro/Downloads/pro/git/meta-liam/python-server/python-build-docker-demo/:/mydata liam1803/python_installer:0.0.1 /bin/bash

```shell
cd /mydata
./deploy/docker/build_exe.sh


cd /mydata/deploy/docker/publish/dist/app
./app

http://192.168.31.235:5001/
(不用IP访问，会有乱码)
```

小结：打出来的包在 python环境正常运行。

## 打ubuntu包

cd deploy/docker/publish/
docker  image rm  liam1803/python_installer_ubuntu:0.0.1

docker build -t  liam1803/python_installer_ubuntu:0.0.1 -f Dockerfile-ubuntu .

### 手工测试ubuntu包

- 测试1
docker run -it --rm=true -p 5001:5001 -v /Users/liampro/Downloads/pro/git/meta-liam/python-server/python-build-docker-demo/:/mydata ubuntu:latest /bin/bash

cd /mydata/deploy/docker/publish/dist/app
./app

curl http://192.168.31.235:5001/api/v1/hello
curl http://192.168.31.235:5001

- 测试2 
docker run -it --rm=true -p 5001:5001 -v /Users/liampro/Downloads/pro/git/meta-liam/python-server/python-build-docker-demo/:/mydata liam1803/python_installer_ubuntu:0.0.1 /bin/bash

./app

- 测试3
docker run -it --rm=true -p 5001:5001 -v /Users/liampro/Downloads/pro/git/meta-liam/python-server/python-build-docker-demo/:/mydata liam1803/python_installer_ubuntu:0.0.1

小结：要用ip访问，localhost有乱码问题！

## Auto

chmod a+x ./build_app.sh && ./build_app.sh

## 参考

https://stackoverflow.com/questions/49389535/problems-with-flask-and-bad-request
