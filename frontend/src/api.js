const API_BASE= import.meta.env.VITE_API_BASE || 'http://localhost:8000'

export async function fetchSongs(){
    const resp = await fetch(`${API_BASE}/songs/`)
    if (!resp.ok) throw new Error('Failed to fetch songs')
    return await resp.json()
}

export async function fetchData(){
    const resp = await fetch(`${API_BASE}/`)
    if (!resp.ok) throw new Error('Failed to fetch data')
    return await resp.json()
}

export async function postSong(songData){
    const resp = await fetch(`${API_BASE}/add-song/`, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(songData)
    });
    if (!resp.ok) throw new Error('Failed to post song')
    return await resp.json()
}

