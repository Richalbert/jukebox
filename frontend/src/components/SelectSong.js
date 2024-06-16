/* frontend/src/components/SelectSong.js
    Composant pour selectionner un morceau */

import React, { useState } from 'react';

function SelectSong({ onSelect }) {
    const [code, setCode] = useState('');

    const handleSubmit = () => {
        onSelect(code);
        setCode('');
    };

    return (
        <div>
            <h2>Entrer le code du morceau</h2>
            <input value={code} onChange={(e) => setCode(e.target.value)} />
            <button onClick={handleSubmit}>Sélectionner</button>
        </div>
    );
}

export default SelectSong;
    