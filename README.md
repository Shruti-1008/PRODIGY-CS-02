# PRODIGY-CS-02

# 🖼️ ɪᴍᴀɢᴇ ᴇɴᴄʀʏᴘᴛᴏʀ & ᴅᴇᴄʀʏᴘᴛᴏʀ (ᴛᴋɪɴᴛᴇʀ + ᴘɪʟʟᴏᴡ)

A simple GUI-based image encryption and decryption tool using pixel manipulation. Built with **Python**, **Tkinter**, and **Pillow**, this tool lets users load images, apply basic pixel-level encryption, and revert them back with decryption.

---

## 📌 ꜰᴇᴀᴛᴜʀᴇꜱ:

- 🖼️ Load `.png`, `.jpg`, `.jpeg` images
- 🔐 Encrypt images using RGB pixel transformation
- 🔓 Decrypt back to original using same logic
- 🖥️ Simple and intuitive GUI using Tkinter
- ⚙️ Customizable encryption logic (basic key-based RGB shift)

---

# ɪɴꜱᴛᴀʟʟ ʀᴇqᴜɪʀᴇᴅ ᴘᴀᴄᴋᴀɢᴇ:

pip install pillow

---

# ▶️ ʜᴏᴡ ᴛᴏ ʀᴜɴ:
1.Click "Load Image" to select a file.

2.Click "Encrypt" to scramble it.

3.Click "Decrypt" to restore it.

---

# 🧠 ʜᴏᴡ ɪᴛ ᴡᴏʀᴋꜱ:

Each pixel's R, G, B values are shifted by a key (e.g., +50) during encryption.

During decryption, the same key is subtracted (e.g., -50) to restore original image.

All values are wrapped with % 256 to stay within valid color range.

---

✅ Conclusion
This project offered a hands-on experience in combining Python, Tkinter, and Pillow to build a functional GUI-based image encryption and decryption tool. By applying simple pixel-level operations, we explored the foundational concepts of how digital data—like images—can be secured and manipulated.

🔒 Encryption doesn’t always have to be complex—this tool demonstrates how even basic logic like pixel shifting can teach important lessons in data transformation, modular arithmetic, and GUI development.

