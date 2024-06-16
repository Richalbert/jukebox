# backend/routes.py 
#   Definitions des routes Flask

from flask import request, jsonify
from app import app, db
from models import Album, Morceau, Playlist, Selection

@app.route('/api/albums', methods=['GET'])
def get_albums():
    albums = Album.query.all()
    response = []
    for album in albums:
        morceaux = [{'id': m.id, 'titre': m.titre, 'code': m.code} for m in album.morceaux]
        response.append({'id': album.id, 'titre': album.titre, 'artiste': album.artiste, 'morceaux': morceaux})
    return jsonify(response)

@app.route('/select', methods=['POST'])
def select():
    data = request.json
    code = data['code']
    morceau = Morceau.query.filter_by(code=code).first()
    if not morceau:
        return jsonify({'error': 'Morceau non trouvé'}), 404

    playlist_id = data['playlist_id']
    selection = Selection(playlist_id=playlist_id, morceau_id=morceau.id)
    db.session.add(selection)
    db.session.commit()
    return jsonify({'message': 'Morceau ajouté à la playlist'}), 201

@app.route('/playlists/<int:playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    selections = Selection.query.filter_by(playlist_id=playlist_id).all()
    playlist = []
    for selection in selections:
        morceau = Morceau.query.get(selection.morceau_id)
        album = Album.query.get(morceau.album_id)
        playlist.append({'titre': morceau.titre, 'artiste': album.artiste})
    return jsonify(playlist), 200
