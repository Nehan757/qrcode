import streamlit as st
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from io import BytesIO

st.set_page_config(page_title="QR Generator ❤️", page_icon="❤️", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Nunito', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #fff0f5 0%, #fce4ec 50%, #fff8e1 100%);
    }

    .hero {
        text-align: center;
        padding: 2.5rem 1rem 1rem;
    }

    .hero h1 {
        font-size: 2.8rem;
        font-weight: 800;
        color: #c2185b;
        margin-bottom: 0.2rem;
    }

    .hero p {
        font-size: 1.1rem;
        color: #e91e8c;
        opacity: 0.8;
        margin-top: 0;
    }

    .card {
        background: white;
        border-radius: 24px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(194, 24, 91, 0.1);
        margin: 1.5rem auto;
        max-width: 520px;
    }

    .qr-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        background: linear-gradient(145deg, #fff0f5, #fce4ec);
        border-radius: 20px;
        padding: 1.5rem;
        margin-top: 1rem;
        border: 2px dashed #f48fb1;
    }

    .scan-label {
        font-size: 1rem;
        color: #c2185b;
        font-weight: 700;
        margin-top: 0.8rem;
        letter-spacing: 0.05em;
    }

    .footer {
        text-align: center;
        color: #e91e8c;
        font-size: 0.9rem;
        padding: 1.5rem 0 2rem;
        opacity: 0.7;
    }

    div[data-testid="stTextInput"] input {
        border-radius: 14px !important;
        border: 2px solid #f48fb1 !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
        font-family: 'Nunito', sans-serif !important;
        background: #fff0f5 !important;
        color: #880e4f !important;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #c2185b !important;
        box-shadow: 0 0 0 3px rgba(194,24,91,0.15) !important;
    }

    div[data-testid="stDownloadButton"] button {
        background: linear-gradient(135deg, #e91e8c, #c2185b) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 0.6rem 2rem !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        font-family: 'Nunito', sans-serif !important;
        cursor: pointer !important;
        transition: transform 0.2s, box-shadow 0.2s !important;
        box-shadow: 0 4px 15px rgba(194,24,91,0.3) !important;
        width: 100% !important;
    }

    div[data-testid="stDownloadButton"] button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(194,24,91,0.4) !important;
    }

    div[data-testid="stImage"] img {
        border-radius: 16px;
    }

    label {
        color: #880e4f !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
    <h1>✨ QR Generator ❤️</h1>
    <p>Made with love for my beautiful girlfriend 🌸</p>
</div>
""", unsafe_allow_html=True)

# Card
st.markdown('<div class="card">', unsafe_allow_html=True)

url = st.text_input("🔗 Paste your link here", placeholder="https://example.com")

if url:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    try:
        img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
    except Exception:
        img = qr.make_image(fill_color="#c2185b", back_color="white")

    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    st.markdown('<div class="qr-container">', unsafe_allow_html=True)
    st.image(buf, width=260)
    st.markdown('<div class="scan-label">📱 Scan me!</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.download_button("💾 Download QR Code", data=buf.getvalue(), file_name="qr_code.png", mime="image/png")

elif not url:
    st.markdown("""
    <div style="text-align:center; color:#f48fb1; padding: 1.5rem 0; font-size:0.95rem;">
        💡 Enter any link above to instantly generate your QR code
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    Made with 💕 just for you
</div>
""", unsafe_allow_html=True)
