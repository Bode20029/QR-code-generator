import qrcode
import tkinter as tk
from PIL import ImageTk, Image

def generate_qr_code():
    info = "https://www.youtube.com/@JirayuVijjakajohn"
    qr_code_filename = "qrcode_image.png"
    
    qr_code = qrcode.make(info)
    qr_code.save(qr_code_filename)
    
    return qr_code_filename

def main():
    window = tk.Tk()
    window.title("QR CODE")
    
    qr_code_filename = generate_qr_code()
    
    image = Image.open(qr_code_filename)
    photo = ImageTk.PhotoImage(image)
    
    image_label = tk.Label(window, image=photo)
    image_label.pack()
    
    window.mainloop()

if __name__ == "__main__":
    main()