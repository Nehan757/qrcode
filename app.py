import streamlit as st
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from io import BytesIO

st.set_page_config(page_title="QR Generator ❤️", layout="centered", page_icon="❤️")

st.markdown("""
<style>
    /* Larger touch-friendly input */
    input[type="text"] {
        font-size: 1.1rem !important;
        padding: 0.75rem !important;
    }
    /* Full-width download button, large tap target */
    .stDownloadButton > button {
        width: 100%;
        padding: 0.75rem;
        font-size: 1.1rem;
        border-radius: 12px;
    }
    /* Reduce side padding on small screens */
    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 2rem !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("QR Code Generator ❤️")
st.caption("Made with love for my beautiful girlfriend 🌸")

url = st.text_input("Enter a URL", placeholder="https://example.com")

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
        img = qr.make_image(fill_color="black", back_color="white")

    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    st.image(buf, caption="Scan me!", use_container_width=True)

    st.download_button("⬇️ Download QR Code", data=buf.getvalue(), file_name="qr_code.png", mime="image/png")
