import os

HOST = "0.0.0.0"
PORT = os.environ.get('PORT', 5000)
cmd = f'python3 manage.py runserver {HOST}:{PORT}'
os.system(cmd)
