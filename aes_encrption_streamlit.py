import streamlit as st
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

st.title('AES encryption details')
### st.write("AES encryption")
### st.write("<B>AES encryption</B>", unsafe_allow_html=True)

data = b"Hello, this is a secret message!"

keybyte = st.selectbox(
    "You can select 16 or 24 or 32 as key byte. : ",
    (16, 24, 32),
)

st.write("You selected:", keybyte)


key = get_random_bytes(keybyte)
cipher = AES.new(key, AES.MODE_CBC)

ciphertext = cipher.encrypt(pad(data, AES.block_size))

st.write("Ciphertext:", ciphertext)
st.write("IV:", cipher.iv)

decipher = AES.new(key, AES.MODE_CBC, iv=cipher.iv)
plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size)

st.write("Plaintext:", plaintext)
