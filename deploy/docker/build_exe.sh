#!/bin/bash
shell_dir=$(dirname $0)

echo ${shell_dir}

cd ${shell_dir}

echo "start build"

cd ../../src

rm -r ../deploy/docker/publish/dist

pip install -r ../requirements.txt

pyinstaller -D app.py --clean --distpath ../deploy/docker/publish/dist

cp -r ../publish/* ../deploy/docker/publish/dist/app/

#rm -r ../deploy/docker/publish/dist/app
#cp -r ./dist/* ../deploy/docker/publish/dist/

echo "start end"
# ./tokmodel.sh out/yolo_1