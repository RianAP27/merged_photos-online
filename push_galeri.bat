@echo off
cd merged_photos-online
git add index.html imgur_links.txt
git commit -m "update galeri otomatis"
git push
pause