pelican content --debug --output output --settings pelicanconf.py

pelican content --output output --settings publishconf.py


cd output
git init
git add .
git commit -m Updates
git remote add origin https://github.com/subwayharearmy/subwayharearmy.github.io.git
git push origin master --force

cd .. 
git init
git add .
git commit -m Updates
git branch -m master source
git remote add origin https://github.com/subwayharearmy/subwayharearmy.github.io.git
git push origin source --force
