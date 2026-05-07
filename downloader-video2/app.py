# =========================================
# PWA VIDEO DOWNLOADER
# Android Style UI
# Streamlit + yt-dlp
# =========================================

# INSTALL:
# pip install streamlit yt-dlp streamlit-pwa

# RUN:
# streamlit run app.py

import streamlit as st
import yt_dlp
import os
from datetime import datetime

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="Downloader PWA",
    page_icon="📥",
    layout="centered",
)

DOWNLOAD_DIR = "downloads"

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

html, body, [class*="css"]  {
    background-color: #0f172a;
    color: white;
    font-family: sans-serif;
}

.main-title {
    text-align:center;
    font-size:34px;
    font-weight:700;
    margin-bottom:10px;
}

.sub-title {
    text-align:center;
    color:#94a3b8;
    margin-bottom:30px;
}

.download-box {
    background:#1e293b;
    padding:25px;
    border-radius:22px;
    margin-top:20px;
    box-shadow:0 0 20px rgba(0,0,0,0.3);
}

.stButton button {
    width:100%;
    height:55px;
    border-radius:16px;
    border:none;
    background:#2563eb;
    color:white;
    font-size:18px;
    font-weight:bold;
}

.stTextInput input {
    border-radius:14px;
}

.stSelectbox div[data-baseweb="select"] {
    border-radius:14px;
}

.footer {
    text-align:center;
    color:#64748b;
    margin-top:50px;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown(
    '<div class="main-title">📥 Downloader PWA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">YouTube • TikTok • Instagram • Facebook</div>',
    unsafe_allow_html=True
)

# =========================================
# FORM
# =========================================

with st.container():

    st.markdown('<div class="download-box">', unsafe_allow_html=True)

    video_url = st.text_input(
        "URL Video",
        placeholder="https://..."
    )

    quality = st.selectbox(
        "Kualitas",
        [
            "Best Quality",
            "720p",
            "480p",
            "MP3 Audio"
        ]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    download_btn = st.button("⬇ Download")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# FORMAT
# =========================================

def get_format(q):
    if q == "720p":
        return "bestvideo[height<=720]+bestaudio/best"
    elif q == "480p":
        return "bestvideo[height<=480]+bestaudio/best"
    elif q == "MP3 Audio":
        return "bestaudio"
    else:
        return "bestvideo+bestaudio/best"

# =========================================
# DOWNLOAD
# =========================================

def download_video(url, quality):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    options = {
        "format": get_format(quality),
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s_{timestamp}.%(ext)s",
        "noplaylist": True,
    }

    if quality == "MP3 Audio":
        options["postprocessors"] = [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        return info

# =========================================
# BUTTON ACTION
# =========================================

if download_btn:

    if video_url == "":
        st.warning("Masukkan URL video.")
    else:

        progress = st.progress(0)
        status = st.empty()

        try:

            status.info("Menghubungkan server...")

            progress.progress(20)

            status.info("Memproses video...")

            progress.progress(50)

            info = download_video(video_url, quality)

            progress.progress(100)

            status.success("Download selesai!")

            st.markdown(f"""
            <div class="download-box">
                <h3>🎬 {info.get("title")}</h3>
                <p>👤 {info.get("uploader")}</p>
                <p>⏱ {info.get("duration")} detik</p>
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")

# =========================================
# FOOTER
# =========================================

st.markdown(
    '<div class="footer">Modern Downloader PWA • Python + Streamlit</div>',
    unsafe_allow_html=True
)