from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Konfigurasi Kebijakan CORS dan Header Keamanan Talisman
CORS(app)
Talisman(app, force_https=False)

from app import routes