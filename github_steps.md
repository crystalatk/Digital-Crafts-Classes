Overview of connecting to GitHub repo:
-On GitHub-
# create new repository
# copy SSH path (should start with git@github…)
-In your terminal-
# cd into folder you want to connect to repository
# git init
*make sure you have at least one file*
# git status
# git add [filename]
# git status
# git commit -m “your commit message - make it descriptive”
# git remote add origin [SSH path]
# git remote -v 
(This checks connection to repo)
# git branch -M main (renames branch from master to main)
# git push -u origin main (edited) 