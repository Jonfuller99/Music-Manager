const API_BASE= import.meta.env.VITE_API_BASE || 'http://localhost:8000'

export async function fetchSongs(){
    const res = await fetch(`${API_BASE}/songs`)
    if (!res.ok) throw new Error('Failed to fetch songs')
    return await res.json()
}

export async function fetchData(){
    const res = await fetch(`${API_BASE}/`)
    if (!res.ok) throw new Error('Failed to fetch data')
    return await res.json()
}

