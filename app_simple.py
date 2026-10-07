import streamlit as st

# ==========================================================
# VERSI 1: KELAS (SUPER SIMPLE & MUDAH DIKETIK SISWA SMP)
# Total: Hanya ~20 Baris!
# ==========================================================

# 1. Judul Aplikasi Web
st.title("📋 To-Do List Pribadi Saya")
st.write("Aplikasi web Python pertama saya!")

st.divider()

# 2. VARIABLE: Menyimpan teks tugas ke memori komputer
nama_tugas = st.text_input("Apa tugas yang mau kamu kerjakan?")

# 3. BOOLEAN: Kotak centang yang menghasilkan True atau False
sudah_selesai = st.checkbox("Tandai jika tugas sudah selesai")

st.divider()

# 4. IF - ELSE: Komputer memeriksa status tugas
if nama_tugas == "":
    st.info("Ketik tugasmu di kotak atas ya! 👆")
else:
    if sudah_selesai:
        st.success(f"🎉 Keren! Tugas '{nama_tugas}' sudah SELESAI!")
    else:
        st.warning(f"⏳ Tugas '{nama_tugas}' BELUM selesai. Semangat!")
