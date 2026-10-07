import streamlit as st

# ==============================================================================
# SMART PERSONAL TO-DO LIST & PRIORITY ADVISOR (Python + Streamlit)
# Tingkat: SMP Pemula (Sesi 60 Menit)
# Konsep Utama: Variable (String, Number), Boolean (Checkbox), Smart If-Elif-Else
# ==============================================================================

st.set_page_config(page_title="Smart To-Do & Priority Advisor", page_icon="🤖")

st.title("🤖 Smart To-Do & Priority Advisor")
st.write("Aplikasi asisten pintar pengingat tugas harian bertenaga logika Python!")

st.divider()

# ------------------------------------------------------------------------------
# 1. KONSEP VARIABLE (Menyimpan Input Teks, Pilihan Dropdown & Angka Slider)
# ------------------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    nama_tugas = st.text_input("📝 Nama Tugas:", placeholder="Contoh: PR Matematika Aljabar")
    prioritas = st.selectbox("🎯 Tingkat Prioritas:", ["Tinggi 🔴", "Sedang 🟡", "Rendah 🟢"])

with col2:
    sisa_hari = st.slider("⏳ Sisa Waktu (Hari menuju deadline):", min_value=0, max_value=7, value=2)
    sudah_selesai = st.checkbox("✅ Tandai tugas ini sudah selesai")

st.divider()

# ------------------------------------------------------------------------------
# 2. LOGIKA IF - ELIF - ELSE PINTAR (Otak Pengambil Keputusan Komputer)
# ------------------------------------------------------------------------------
st.subheader("💡 Analisis & Rekomendasi Asisten:")

# KONDISI 1: Cek apakah nama tugas masih kosong
if nama_tugas == "":
    st.info("👆 Masukkan nama tugasmu di atas untuk melihat analisis asisten!")

# KONDISI 2: Cek apakah tugas sudah ditandai selesai (Boolean = True)
elif sudah_selesai:
    st.balloons()
    st.success(f"🎉 **MISSION COMPLETED!** Tugas **{nama_tugas}** berhasil diselesaikan!")
    
    # If bertingkat: memberi apresiasi berbeda berdasarkan sisa hari
    if sisa_hari >= 3:
        st.info("🏆 **PRODUKTIF MAKSIMAL!** Selesai jauh sebelum deadline! Kamu dapat bonus +100 XP!")
    else:
        st.caption("👏 Selesai tepat waktu! Pertahankan disiplin belajarmu!")

# KONDISI 3: Tugas BELUM selesai -> Komputer menghitung urgensi & bahaya!
else:
    # 3A. Deadline HARI INI dan Prioritas TINGGI (BAHAYA!)
    if sisa_hari == 0 and prioritas == "Tinggi 🔴":
        st.error(f"🚨 **BAHAYA MAKSIMAL!** Tugas **{nama_tugas}** deadlinenya **HARI INI** dan sangat penting! Matikan game, kerjakan sekarang juga! 🔥")
        
    # 3B. Deadline HARI INI tapi prioritas sedang/rendah
    elif sisa_hari == 0:
        st.warning(f"⚠️ **HARI INI TERAKHIR!** Tugas **{nama_tugas}** harus diserahkan hari ini sebelum malam!")
        
    # 3C. Sisa waktu 1-2 hari dan prioritas TINGGI (DARURAT)
    elif sisa_hari <= 2 and prioritas == "Tinggi 🔴":
        st.warning(f"⚡ **PERINGATAN DARURAT:** Tugas **{nama_tugas}** tinggal {sisa_hari} hari lagi & prioritas tinggi. Cicil 30 menit sekarang!")
        
    # 3D. Prioritas Sedang
    elif prioritas == "Sedang 🟡":
        st.info(f"📌 **TERJADWAL AMAN:** Masih ada {sisa_hari} hari untuk **{nama_tugas}**. Kerjakan santai agar tidak menumpuk.")
        
    # 3E. Prioritas Rendah (SANTAI)
    else:
        st.success(f"🌱 **SANTAI:** Tugas **{nama_tugas}** prioritas rendah dan masih ada {sisa_hari} hari. Bisa dikerjakan nanti.")

st.divider()
st.caption("💡 Geser slider hari atau ubah prioritas di atas untuk melihat bagaimana kondisi IF-ELIF-ELSE bereaksi seketika di layar!")
