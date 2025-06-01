CREATE SCHEMA IF NOT EXISTS music;

DROP TABLE IF EXISTS music.songs;

/*
Create Tables
*/
CREATE TABLE music.songs
(
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    artist TEXT,
    genre TEXT,
    bpm INTEGER,
    file_path TEXT NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);