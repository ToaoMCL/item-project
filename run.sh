sudo apt update
pip3 install -r requirements.txt
python3 create.py
gunicorn --workers=4 --bind=0.0.0.0:5000 app:app