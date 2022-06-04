# 开发文档

python 开发 http服务，然后打linux安装包，最后在ubuntu镜像发布。

## 环境

建议安装 Anaconda管理python环境。

```shell
 #python 3.10 (官方要求 3.4)
conda info -e
conda activate bing-ad-310

pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
or
pip3 install -r requirements.txt

```

## 快速开始

```shell
#更新 refresh.txt 文件(环境变量)，DEVELOPER_TOKEN，CLIENT_ID
cd src
python app.py
```

## 测试

```shell
curl  http://localhost:5001/

curl -H 'AppID: web' -H 'AppSecret: 123456' -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"start": "2022-05-01", "stop":"2022-06-01"}'  http://localhost:5001/report_request

```

## 打包文档

deploy/docker/build.md

## docker测试

docker-compose -f docker-compose-dev.yml up -d

http://192.168.31.235:6401/
