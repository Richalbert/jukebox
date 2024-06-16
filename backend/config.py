# backend/config.py 
#   Configuration de l'application Flask

import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'jukebox.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
