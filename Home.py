import streamlit as st
from utils.db import insert_entry, init_db

# Surah names (short list - replace with full 114 if needed)
surahs = [
    "Al-Fatiha", "Al-Baqarah", "Al-Imran", "An-Nisa", "Al-Ma'idah",
    "Al-An'am", "Al-A'raf", "Al-Anfal", "At-Tawbah", "Yunus"
]

names = ["Alice", "Bob", "Charlie", "Diana"]

st.title("📖 Qur'an Memorisation Submission")

init_db()

name = st.selectbox("Your Name", names)
commitment = st.number_input("Weekly Commitment (lines)", min_value=1)
surah = st.selectbox("Surah", surahs)
ayah_start = st.number_input("Ayah Start", min_value=1)
ayah_end = st.number_input("Ayah End", min_value=ayah_start)
lines = st.number_input("Number of Lines Completed", min_value=0)

if st.button("Submit"):
    insert_entry(name, commitment, surah, ayah_start, ayah_end, lines)
    st.success("✅ Your submission has been saved.")
