import streamlit as st
import time

# ==============================================================================
# 🚀 ULTRA WOW DEMO: TASK HERO & STUDY BUDDY AI (Pertemuan 10)
# Ditampilkan Guru di Depan Kelas untuk Menginspirasi Siswa!
# Fondasi Logika: Variable (String, Int), Boolean (Checkbox), Smart If-Elif-Else
# ==============================================================================

st.set_page_config(
    page_title="Task Hero — Study Buddy AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS UNTUK TAMPILAN GAMIFIKASI MODERN ---
st.markdown("""
<style>
    .metric-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 14px;
        padding: 1.2rem;
        text-align: center;
    }
    .level-badge {
        background: linear-gradient(135deg, #6366f1, #a855f7);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 9999px;
        font-weight: 700;
        font-size: 0.85rem;
    }
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #6366f1, #06b6d4, #10b981);
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# 1. SIDEBAR: KARAKTER SISWA & POMODORO STUDY TIMER (VARIABLE & BOOLEAN)
# ------------------------------------------------------------------------------
with st.sidebar:
    st.image("https://api.dicebear.com/7.x/bottts/svg?seed=CoderHero", width=120)
    st.title("⚡ Study Buddy AI")
    st.caption("Asisten Belajar Pertemuan 10")
    
    st.divider()
    
    # Variable Input Teks & Dropdown
    student_name = st.text_input("Nama Siswa:", value="Budi Si Koder")
    study_mode = st.selectbox("Mode Belajar:", ["🎯 Deep Focus (Ujian)", "📚 Santai (PR Harian)", "🎮 Break & Refresh"])
    
    st.divider()
    
    # Pomodoro Timer Mini (Boolean State)
    st.subheader("⏱️ Focus Timer (Pomodoro)")
    timer_minutes = st.slider("Durasi Fokus (Menit):", 5, 60, 25)
    start_timer = st.button("🔥 Mulai Sesi Fokus")
    
    if start_timer:
        st.success(f"Sesi fokus {timer_minutes} menit dimulai untuk {student_name}!")
        st.toast("Fokus aktif! Jangan buka YouTube dulu ya! 🤫")

# ------------------------------------------------------------------------------
# 2. MAIN HEADER & STATUS XP DASHBOARD
# ------------------------------------------------------------------------------
header_col1, header_col2 = st.columns([3, 1])

with header_col1:
    st.title(f"🚀 Mission Board: {student_name}")
    st.write(f"Mode Aktif: **{study_mode}** • Selesaikan misi untuk naik level!")

with header_col2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<span class="level-badge">LEVEL 2: CODE APPRENTICE 🛡️</span>', unsafe_allow_html=True)

st.divider()

# ------------------------------------------------------------------------------
# 3. DAFTAR MISI HARIAN (INPUT VARIABLE & BOOLEAN CHECKBOX)
# ------------------------------------------------------------------------------
st.subheader("📋 3 Misi Belajar Hari Ini")

col_a, col_b, col_c = st.columns([3, 1.5, 1.2])

with col_a:
    q1_name = st.text_input("Misi 1 (Tugas Utama):", value="Kerjakan Soal Latihan Aljabar Bab 4")
with col_b:
    q1_priority = st.selectbox("Prioritas 1:", ["Tinggi 🔴", "Sedang 🟡", "Rendah 🟢"], key="p1")
with col_c:
    st.write("Status:")
    q1_done = st.checkbox("Selesai ✅", key="d1")

col_a, col_b, col_c = st.columns([3, 1.5, 1.2])

with col_a:
    q2_name = st.text_input("Misi 2 (Skill Koding):", value="Latihan Variable & If-Else di Codespaces")
with col_b:
    q2_priority = st.selectbox("Prioritas 2:", ["Tinggi 🔴", "Sedang 🟡", "Rendah 🟢"], index=1, key="p2")
with col_c:
    st.write("Status:")
    q2_done = st.checkbox("Selesai ✅", key="d2")

col_a, col_b, col_c = st.columns([3, 1.5, 1.2])

with col_a:
    q3_name = st.text_input("Misi 3 (Kebiasaan Baik):", value="Rapikan Meja Belajar & Minum 2 Gelas Air")
with col_b:
    q3_priority = st.selectbox("Prioritas 3:", ["Tinggi 🔴", "Sedang 🟡", "Rendah 🟢"], index=2, key="p3")
with col_c:
    st.write("Status:")
    q3_done = st.checkbox("Selesai ✅", key="d3")

st.divider()

# ------------------------------------------------------------------------------
# 4. LOGIKA PINTAR IF - ELIF - ELSE UNTUK MENGHITUNG SCORE & TINGKAT BAHAYA
# ------------------------------------------------------------------------------
completed_count = 0
earned_xp = 0

if q1_done:
    completed_count += 1
    earned_xp += 100

if q2_done:
    completed_count += 1
    earned_xp += 100

if q3_done:
    completed_count += 1
    earned_xp += 50

progress_pct = int((completed_count / 3) * 100)

# TAMPILAN PROGRES BAR REAL-TIME
st.subheader("📊 Statistik Pencapaian Harian")
st.progress(progress_pct)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Misi Dituntaskan", f"{completed_count} / 3")
m2.metric("Total XP Hari Ini", f"{earned_xp} XP", delta=f"+{earned_xp}" if earned_xp > 0 else None)
m3.metric("Persentase Kemenangan", f"{progress_pct}%")
m4.metric("Kesehatan Disiplin", "Sangat Baik 🌟" if completed_count >= 2 else "Perlu Ditingkatkan ⚠️")

st.divider()

# ------------------------------------------------------------------------------
# 5. EVALUASI ADVISOR AI (IF - ELIF - ELSE BERTINGKAT)
# ------------------------------------------------------------------------------
st.subheader("🤖 Analisis Asisten Belajar Pintar:")

# Evaluasi 1: Jika Semua Misi Tuntas
if completed_count == 3:
    st.balloons()
    st.success(f"👑 **PERFECT RUN!** Luar biasa, {student_name}! Seluruh misi belajar berhasil kamu tuntaskan 100%! Kamu layak dapat predikat Raja Disiplin hari ini! 🎉")

# Evaluasi 2: Jika Misi 1 (Prioritas Tinggi) Belum Selesai tapi Siswa Malah Bereskan Misi Lain
elif not q1_done and q1_priority == "Tinggi 🔴":
    st.error(f"🚨 **PERHATIAN DARURAT!** Misi 1 (**{q1_name}**) memiliki prioritas TINGGI tetapi belum selesai! Jangan tergoda mengerjakan hal sepele dulu, tuntaskan yang ini sekarang juga! 🔥")

# Evaluasi 3: Jika Sudah 2 Misi Selesai
elif completed_count == 2:
    st.info(f"⚡ **TINGGAL 1 LANGKAH LAGI!** Dua misi sudah beres. Sisihkan 15 menit untuk menuntaskan misi terakhir dan dapatkan bintang emas!")

# Evaluasi 4: Jika Baru 1 Misi Selesai
elif completed_count == 1:
    st.warning("💪 **MOMENTUM BAGUS!** Misi pertama sudah pecah telur. Teruskan fokus belajarmu ke tugas berikutnya!")

# Evaluasi 5: Belum Ada Misi yang Dimulai
else:
    st.error("💤 **MISI BELUM DIMULAI.** Ayo centang misi pertamamu dan lihat bagaimana skor serta progress bar di atas bereaksi seketika!")

st.divider()
st.caption("💡 Rahasia Dibalik Layar: Seluruh dashboard cerdas ini dibangun murni menggunakan 3 konsep yang kita pelajari: Variable, Boolean, dan If-Elif-Else!")
