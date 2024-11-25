#!/usr/bin/env bash
./process_templates.py

git add .
git commit -m 'latest'
git push -u origin main
