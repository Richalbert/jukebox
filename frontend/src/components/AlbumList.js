/* frontend/src/components/AlbumList.js
    Composant pour afficher les albums  */

import React from 'react';

function AlbumList({ albums }) {
    return (
        <div>
            {albums.map(album => (
                <div key={album.id}>
                    <h2>{album.titre}</h2>
                    <p>{album.artiste}</p>
                    <ul>
                        {album.morceaux.map(morceau => (
                            <li key={morceau.id}>
                                {morceau.titre} - {morceau.code}
                            </li>
                        ))}
                    </ul>
                </div>
            ))}
        </div>
    );
}

export default AlbumList;
    