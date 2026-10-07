# 📋 Python Streamlit Personal To-Do List Template

Repository template untuk pembelajaran pemrograman Python dan pembuatan web app interaktif menggunakan **Streamlit** di **GitHub Codespaces**.

Dirancang khusus untuk siswa SMP pemula (usia 12–15 tahun) yang baru belajar `print()`, Variable, Boolean, dan If-Else.

---

## 🚀 Cara Menjalankan di GitHub Codespaces

1. Klik tombol hijau **Use this template** di kanan atas → pilih **Create a new repository**.
2. Beri nama repositori kamu (misal: `todolist-saya`).
3. Di repo baru kamu, klik tombol hijau **Code** → pilih tab **Codespaces** → klik **Create codespace on main**.
4. Tunggu beberapa saat sampai lingkungan Codespaces selesai disiapkan (Python & Streamlit terpasang otomatis).
5. Di panel **Terminal** di bagian bawah, ketik salah satu perintah berikut:

   **Untuk Latihan Siswa di Kelas:**
   ```bash
   streamlit run app_simple.py
   ```

   **Untuk Demo Fitur Lengkap:**
   ```bash
   streamlit run app_wow.py
   ```

6. Klik tombol popup **Open in Browser** pada port `8501`. Selamat mencoba! 🎉

---

## 📁 Struktur Berkas

- `.devcontainer/devcontainer.json`: Konfigurasi otomatis environment Codespaces & port forwarding `8501`.
- `requirements.txt`: Dependensi library Streamlit.
- `app_simple.py`: Kode latihan sederhana (~25 baris) untuk diketik bersama di kelas.
- `app_wow.py`: Versi demo spektakuler dengan gamifikasi, progress bar, dan efek balon confetti.
- `app.py`: Versi kartu tugas teranotasi lengkap.
