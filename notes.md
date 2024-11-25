# GitHub Pages

```bash
# create repo called <user>.github.io -> robertvigil.github.io
cd /media/sf_dropbox/code/_production
git clone https://github.com/robertvigil/robertvigil.github.io
cd robertvigil.github.io

# add index.html, styles.css

# git config --global --add safe.directory /media/sf_dropbox/code/_production/robertvigil.github.io
# may have to follow instructions in github-notes.md about setting up gh client and auth

git config --global user.email "rvigil@roylu.com"
git config --global user.name "Robert Vigil"

git add --all
git commit -m "initial commit"
git push -u origin main
```
