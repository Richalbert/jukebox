# backend/models.py 
#   Definitions des modeles SQLAlchemy

from app import db

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    artiste = db.Column(db.String(100), nullable=False)
    annee = db.Column(db.Integer, nullable=False)
    morceaux = db.relationship('Morceau', backref='album', lazy=True)

class Morceau(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    selections = db.relationship('Selection', backref='playlist', lazy=True)

class Selection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)
    morceau_id = db.Column(db.Integer, db.ForeignKey('morceau.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
