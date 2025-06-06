const API_BASE= import.meta.env.VITE_API_BASE || 'http://localhost:8000'

export async function fetchSongs(){
    const resp = await fetch(`${API_BASE}/songs/`)
    if (!resp.ok) throw new Error('Failed to fetch songs')
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

export async function removeSong(song_id){
    const resp = await fetch(`${API_BASE}/remove-song/${song_id}`, {
        method: 'DELETE'
    })
    if (!resp.ok) throw new Error('Failed to delete song')
    return await resp.json()
}

export async function uploadFile(uploadedFile){
    const formData = new FormData();
    formData.append('uploaded_file', uploadedFile);
    const resp = await fetch(`${API_BASE}/upload-file/`, {
        method: 'POST',
        body: formData
    });
    if (!resp.ok) throw new Error('Failed to upload file', formData)
    return await resp.json()
}

