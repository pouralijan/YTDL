
# YTDL
YouTube Downloader App For Django

# install
First clone source code and change directory in YTDL.
```
git clone https://github.com/pouralijan/YTDL.git
cd ./YTDL
```
# install and start backend
Backend write with python django.
```
virtualenv ./venv
source ./venv/bin/activate
pip install -i -U pip
pip install -r requrments.txt
cd ./src/backend
./manage.py migrate
./manage.py runserver
```

# install and start frontend

Frontend write with javascript and reactjs.
```
cd ./src/frontend
npm install --save
npm start
```
