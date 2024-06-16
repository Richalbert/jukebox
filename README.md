# Jukebox d'anniversaire

l'utilisateur telecharge sur son mobile une application sur laquelle il s'identifie
il peut alors choisir dans un catalogue de musiques
son choix est rajoute a une liste de lecture partage

c'est la selection de la musique

le format des musiques est mp3 

## les extensions
- authentification des users
- creations de playlist
- memorisation de la playlist de la soiree
- diffusion sur internet de la playlist
- election d un morceau qui peut passer en tete de liste

# Le projet Jukebox

## Etape 1 : la conception de l'architecture

1. Backend: un serveur pour gerer

   - les requetes des utilisateurs
   - les selections des morceaux
   - les playlists

2. Frontend: l'interface utilisateur

    - pour afficher les albums
    - entrer les codes des morceaux
    - visualiser les playlists

## Etape 2: la mise en place de la base de donnees (SQLite)

Les tables:

    - Albums : id, titre, artiste, annee
    - Morceaux : id, titre, album_id (cle etrangere vers Albums), code
    - Playlist : id, nom
    - Selections: id, playlist_id (cle etrangere vers Playlists), morceau:id (cle etrangere vers Morceaux), timestamp


## Etape 3: le developpement de l'interface utilisateur (UI)

Un site web:

    - une page d'acceuil : liste des albums et morceaux
    - une page de selection: formulaire pour entrer le code du morceau
    - une page de playlist: affiche les morceaux selectionnes

## Etape 4: l'implementation de la logique de selection et la gestion des playlists