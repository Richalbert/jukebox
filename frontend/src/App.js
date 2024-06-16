/* frontend/src/AudioParamMap.js 
    Composant principal de l'application 
 */

import React, { useState, useEffect } from 'react';
import AlbumList from './components/AlbumList';
import SelectSong from './components/SelectSong';
import Playlist from './components/Playlist';

function App() {
    const [albums, setAlbums] = useState([]);
    const [playlist, setPlaylist] = useState([]);

    useEffect(() => {
        fetch('/api/albums')
            .then(response => response.json())
            .then(data => setAlbums(data));
        fetch('/playlists/1')
            .then(response => response.json())
            .then(data => setPlaylist(data));
    }, []);

    const handleSelect = (code) => {
        fetch('/select', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code, playlist_id: 1 })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                fetch('/playlists/1')
                    .then(response => response.json())
                    .then(data => setPlaylist(data));
            }
        });
    };

    return (
        <div>
            <h1>Jukebox</h1>
            <AlbumList albums={albums} />
            <SelectSong onSelect={handleSelect} />
            <Playlist playlist={playlist} />
        </div>
    );
}

export default App;
    