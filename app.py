import streamlit as st

# ==============================================================================
# PROYEK: PERSONAL TO-DO LIST (Python + Streamlit)
# Tingkat: SMP Pemula (Sesi 60 Menit)
# Konsep Utama: Variable, Boolean, Percabangan (If - Else)
# ==============================================================================

# ------------------------------------------------------------------------------
# 0. KONFIGURASI HALAMAN & HEADER
# ------------------------------------------------------------------------------
st.set_page_config(page_title="My Personal To-Do List", page_icon="📋", layout="centered")

st.title("📋 My Personal To-Do List")
st.write("Selamat datang! Ini adalah aplikasi web personal to-do list interaktif pertama kamu.")
st.caption("Dibuat menggunakan Python & Streamlit di GitHub Codespaces 🚀")

st.divider()

# ------------------------------------------------------------------------------
# 1. KONSEP VARIABLE (Menyimpan Teks & Pilihan ke Memori)
# ------------------------------------------------------------------------------
st.subheader("1. Masukkan Rincian Tugas")

# Variable 'task_name' menyimpan data String (teks) dari input user
task_name = st.text_input(
    label="Apa kegiatan / tugas yang ingin kamu selesaikan?",
    placeholder="Misal: Mengerjakan PR Matematika Halaman 45"
)

# Variable 'priority' menyimpan pilihan kategori dari dropdown
priority = st.selectbox(
    label="Pilih tingkat prioritas tugas:",
    options=["Tinggi 🔴", "Sedang 🟡", "Rendah 🟢"]
)

# Variable 'estimated_time' menyimpan angka (Integer)
estimated_time = st.number_input(
    label="Berapa menit perkiraan waktu mengerjakannya?",
    min_value=5,
    max_value=180,
    value=30,
    step=5
)

st.divider()

# ------------------------------------------------------------------------------
# 2. KONSEP BOOLEAN (True atau False)
# ------------------------------------------------------------------------------
st.subheader("2. Status Pengerjaan")

# st.checkbox mengembalikan nilai BOOLEAN:
# - Bernilai True jika kotak dicentang
# - Bernilai False jika kotak TIDAK dicentang
is_completed = st.checkbox("Tandai tugas ini sudah selesai dikerjakan")

st.divider()

# ------------------------------------------------------------------------------
# 3. KONSEP IF - ELSE (Pengambilan Keputusan Komputer)
# ------------------------------------------------------------------------------
st.subheader("3. Ringkasan & Kartu Tugas")

# Validasi awal: Jika pengguna belum menuliskan nama tugas
if task_name == "":
    st.info("💡 Ayo ketik nama tugasmu di bagian atas untuk melihat kartu tugas!")
else:
    # Komputer memeriksa nilai Boolean 'is_completed'
    if is_completed:
        st.success(f"🎉 **SELESAI!** Kamu berhasil menyelesaikan: **{task_name}**!")
        st.balloons()
        st.write(f"• **Prioritas:** {priority}")
        st.write(f"• **Waktu terselesaikan:** ±{estimated_time} menit")
        st.write("Kerja bagus! Istirahat sejenak atau ambil tugas berikutnya! ✨")
    else:
        st.warning(f"⏳ **PENDING:** Tugas **{task_name}** belum selesai.")
        st.write(f"• **Prioritas:** {priority}")
        st.write(f"• **Perkiraan waktu pengerjaan:** {estimated_time} menit")
        st.write("Semangat fokus dan selesaikan tugas ini tepat waktu! 💪")

st.divider()
st.caption("💡 Tips Belajar: Ubah status centang di atas untuk melihat bagaimana kondisi IF dan ELSE bereaksi seketika di layar!")
