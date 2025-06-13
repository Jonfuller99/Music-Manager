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
    if (!resp.ok) throw new Error('Failed to register user', userData)
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
    if (!resp.ok) throw new Error('Failed to login user', formData)

    const data = await resp.json()
    localStorage.setItem('access_token', data.access_token)
    return data
}

export async function getCurrentUser() {
    const token = localStorage.getItem('access_token')
    if (!token) throw new Error('No token found')
    
    const resp = await fetch(`${API_BASE}/users/me`, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    
    if (!resp.ok) {
        if (resp.status === 401) {
            // Token expired or invalid
            localStorage.removeItem('access_token')
            throw new Error('Please login again')
        }
        throw new Error('Failed to get user info')
    }
    
    return await resp.json()
}

