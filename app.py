import streamlit as st
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from io import BytesIO

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

    st.image(buf, caption="Scan me!", width=300)

    st.download_button("Download QR Code", data=buf.getvalue(), file_name="qr_code.png", mime="image/png")
