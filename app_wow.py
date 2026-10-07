import streamlit as st

# ==============================================================================
# VERSI 2: WOW DEMO (UNTUK DIPAMERKAN GURU DI DEPAN KELAS)
# Fitur: Multi-Task, Real-time Progress Bar, Level Gamifikasi & Confetti Balon!
# Fondasi Logika: Tetap hanya menggunakan Variable, Boolean, dan If-Else!
# ==============================================================================

st.set_page_config(
    page_title="Task Hero — Daily Quest Master",
    page_icon="⚡",
    layout="centered"
)

# --- CSS SEDERHANA UNTUK AESTHETICS ---
st.markdown("""
    <style>
    .main { background: #0f172a; }
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #6366f1, #06b6d4, #10b981); }
    </style>
""", unsafe_allow_html=True)

# HEADER
st.title("⚡ Task Hero: Daily Quest Tracker")
st.caption("🚀 Master your day • Built with Python & Streamlit on GitHub Codespaces")

st.divider()

# SIDEBAR: PROFIL USER (KONSEP VARIABLE)
with st.sidebar:
    st.header("👤 Karakter Pemain")
    user_name = st.text_input("Nama Siswa:", value="Alex Si Koder")
    user_avatar = st.selectbox("Pilih Avatar:", ["🧙‍♂️ Wizard Koding", "🥷 Ninja Python", "🚀 Cyber Pilot"])
    target_xp = 100
    st.success(f"{user_avatar} **{user_name}** siap beraksi!")
    st.info("💡 Selesaikan 3 misi harian untuk mencapai Level MAX!")

# SECTION: DAFTAR MISI (3 TUGAS DENGAN VARIABLE & BOOLEAN)
st.subheader("🎯 3 Misi Utama Hari Ini")

col1, col2 = st.columns([3, 1])

with col1:
    task1 = st.text_input("Misi 1 (Pelajaran):", value="Kerjakan PR Matematika bab Aljabar")
with col2:
    done1 = st.checkbox("Selesai 1", key="c1")

col1, col2 = st.columns([3, 1])
with col1:
    task2 = st.text_input("Misi 2 (Hobi/Skill):", value="Latihan ngetik 10 jari & baca Python")
with col2:
    done2 = st.checkbox("Selesai 2", key="c2")

col1, col2 = st.columns([3, 1])
with col1:
    task3 = st.text_input("Misi 3 (Kebaikan/Rumah):", value="Bantu bereskan meja belajar & minum air")
with col2:
    done3 = st.checkbox("Selesai 3", key="c3")

st.divider()

# ==============================================================================
# LOGIKA IF - ELSE UNTUK MENGHITUNG SCORE & PROGRESS
# ==============================================================================
# Variabel penghitung skor awal
total_done = 0

# Cek kondisi task 1
if done1:
    total_done = total_done + 1

# Cek kondisi task 2
if done2:
    total_done = total_done + 1

# Cek kondisi task 3
if done3:
    total_done = total_done + 1

# Hitung persentase progress
progress_percentage = int((total_done / 3) * 100)

# TAMPILAN DASHBOARD PERFORMA
st.subheader("📊 Status Progres Kamu")
st.progress(progress_percentage)

# METRIC DISPLAY
m_col1, m_col2, m_col3 = st.columns(3)
m_col1.metric("Misi Selesai", f"{total_done} / 3")
m_col2.metric("Total XP", f"{total_done * 50} XP")
m_col3.metric("Persentase", f"{progress_percentage}%")

st.divider()

# EVALUASI AKHIR (IF - ELIF - ELSE)
st.subheader("🏆 Evaluasi Mentor AI")

if total_done == 3:
    st.balloons()
    st.success(f"👑 **LEGENDARY!** Selamat {user_name}! Semua misi berhasil dituntaskan 100%! Kamu pahlawan hari ini! 🎉")
elif total_done == 2:
    st.info(f"🔥 **HAMPIR SEMPURNA!** 2 misi sudah beres, sisa 1 misi lagi menuju kemenangan penuh!")
elif total_done == 1:
    st.warning(f"⚡ **AWAL YANG BAGUS!** Kamu sudah menyelesaikan 1 tugas. Teruskan momentum belajarmu!")
else:
    st.error("💤 **BELUM ADA MISI DIMULAI.** Buka bukumu, centang misi pertama, dan lihat keajaiban aplikasi ini!")

st.divider()
st.caption("💡 Rahasia Dibalik Layar: Seluruh fitur interaktif di atas murni dibangun dari Variable, Boolean (checkbox), dan If-Else!")
