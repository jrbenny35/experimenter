#/bin/sh
./scripts/echo_version_json.sh > ./app/experimenter/version.json
cp ./app/experimenter/version.json ./app/version.json
docker build -f app/Dockerfile -t app:build app/
