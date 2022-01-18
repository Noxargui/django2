docker login <<EOF
theo237
PNgo1998!
EOF
docker build -t appli_django /var/jenkins_home/workspace/Dernier_projet/
docker tag appli_django theo237/repo_django:$BUILD_NUMBER
docker push theo237/repo_django:$BUILD_NUMBER
