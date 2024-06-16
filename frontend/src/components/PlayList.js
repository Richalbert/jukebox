/* frontend/src/components/Playlist.js 
    Composant pour afficher la playlist  */


import React from 'react';

function Playlist({ playlist }) {
    return (
        <div>
            <h2>Playlist</h2>
            <ul>
                {playlist.map((morceau, index) => (
                    <li key={index}>{morceau.titre} - {morceau.artiste}</li>
                ))}
            </ul>
        </div>
    );
}

export default Playlist;
    