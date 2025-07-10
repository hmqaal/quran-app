import psycopg2
import pandas as pd
import streamlit as st

def get_connection():
    creds = st.secrets["postgres"]
    return psycopg2.connect(
        host=creds["host"],
        database=creds["dbname"],
        user=creds["user"],
        password=creds["password"],
        port=creds["port"]
    )

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS commitments (
            id SERIAL PRIMARY KEY,
            name TEXT,
            commitment INTEGER,
            surah TEXT,
            ayah_start INTEGER,
            ayah_end INTEGER,
            lines INTEGER,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_entry(name, commitment, surah, ayah_start, ayah_end, lines):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO commitments (name, commitment, surah, ayah_start, ayah_end, lines)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (name, commitment, surah, ayah_start, ayah_end, lines))
    conn.commit()
    cursor.close()
    conn.close()
