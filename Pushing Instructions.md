> This is just a push practice

## Pushing a file on a repository:

* Create a folder in desktop with the name ```Reddit Project```
* Open command prompt and change the directory to this folder ```cd Desktop/Reddit\ Project```
* Initialised the current working directory (Reddit Project) to be the working directory of git using ```git init```
* Created the file 'Pushing Instructions.md' inside the project folder using ```touch 'Pushing Instructions.md```
* Adds the files in the local repository and stages them for commit using ```git add .```
* Commit the tracked changes and prepare them to be pushed to a remote repository using ```git commit -m "Instructions for Pushing"```
* Set the remote URL (The repository where the files are to be uploaded) ```git remote add origin https://github.com/Learning-Python-Team/Data-Analysis-Project```
* Verify if the URL is valid ```git remote -v```
* Finally Push the changes! ```git push origin master```
