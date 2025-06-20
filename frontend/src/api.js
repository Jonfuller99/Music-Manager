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


export async function registerUser(userData){
    const resp = await fetch(`${API_BASE}/register/`, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(userData)
    })
    if (!resp.ok) {
        const errorData = await resp.json() // Get the error details from FastAPI
        const error = new Error('Failed to register user')
        error.response = {
            status: resp.status,
            data: errorData
        }
        throw error
    }
    return await resp.json()
}

export async function loginUser(username, password){
    const formData = new FormData();

    formData.append('username', username);
    formData.append('password', password);
    const resp = await fetch(`${API_BASE}/token/`, {
        method: 'POST',
        body: formData
    });
    const data = await resp.json()
    if(!resp.ok){
        const error = new Error(data?.detail || `Failed to login: ${resp.status}`)
        error.response = {
            status: resp.status,
            data: data
        }
        throw error
    }

    return data
}

export async function getCurrentUser(token) {
    if (!token) throw new Error('No token found')
    
    const resp = await fetch(`${API_BASE}/users/me`, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    
    if (!resp.ok) {
        const errorData = await resp.json().catch(() => ({}))
        const error = new Error('Failed to get user info')
        error.response = {
            status: resp.status,
            data: errorData
        }
        throw error
    }
    
    return await resp.json()
}

