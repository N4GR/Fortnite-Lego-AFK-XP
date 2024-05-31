@echo off
pip install pipreqs
cls
pipreqs -f
cls
pip install -r "requirements.txt"
cls
python ./main.py
pause