```bash
# create repo called <user>.github.io -> robertvigil.github.io
cd /media/sf_dropbox/code/_production
git clone https://github.com/robertvigil/robertvigil.github.io
cd robertvigil.github.io

# add index.html, styles.css

git config --global --add safe.directory /media/sf_dropbox/code/_production/robertvigil.github.io
git add --all
git commit -m "initial commit"
git push -u origin main
```