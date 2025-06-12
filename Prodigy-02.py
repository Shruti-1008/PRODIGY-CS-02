import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# --- Functions for Pixel Manipulation ---
def encrypt_image(img, key=50):
    """Encrypts image by adding key to RGB values."""
    encrypted = img.copy()
    pixels = encrypted.load()
    for y in range(encrypted.height):
        for x in range(encrypted.width):
            r, g, b = pixels[x, y]
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    return encrypted

def decrypt_image(img, key=50):
    """Decrypts image by subtracting key from RGB values."""
    decrypted = img.copy()
    pixels = decrypted.load()
    for y in range(decrypted.height):
        for x in range(decrypted.width):
            r, g, b = pixels[x, y]
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    return decrypted

# --- GUI Class for the App ---
class ImageEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryptor & Decryptor")

        self.image = None
        self.tk_img = None

        # Canvas to display image
        self.canvas = tk.Canvas(root, width=500, height=500, bg="gray")
        self.canvas.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack()

        load_btn = tk.Button(button_frame, text="Load Image", command=self.load_image)
        load_btn.grid(row=0, column=0, padx=10)

        encrypt_btn = tk.Button(button_frame, text="Encrypt", command=self.encrypt)
        encrypt_btn.grid(row=0, column=1, padx=10)

        decrypt_btn = tk.Button(button_frame, text="Decrypt", command=self.decrypt)
        decrypt_btn.grid(row=0, column=2, padx=10)

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if path:
            self.image = Image.open(path).convert("RGB")
            self.display_image(self.image)

    def display_image(self, img):
        resized = img.resize((400, 400))
        self.tk_img = ImageTk.PhotoImage(resized)
        self.canvas.delete("all")  # Clear previous image
        self.canvas.create_image(250, 250, image=self.tk_img)

    def encrypt(self):
        if self.image:
            self.image = encrypt_image(self.image)
            self.display_image(self.image)
        else:
            messagebox.showinfo("Notice", "Please load an image first.")

    def decrypt(self):
        if self.image:
            self.image = decrypt_image(self.image)
            self.display_image(self.image)
        else:
            messagebox.showinfo("Notice", "Please load an image first.")

# --- Run the App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorApp(root)
    root.mainloop()
