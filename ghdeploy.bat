call pelpub.bat
git add -A
git commit -m "Deploying changes"
git push origin source
pushd output
git add -A
git commit -m "Deploying changes"
git push origin master
popd