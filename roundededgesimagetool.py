from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk

def round_corners(image_path, radius_percent):
    image = Image.open(image_path)
    width, height = image.size
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle((0, 0, width, height), fill=255)
    draw.rounded_rectangle((0, 0, width, height), radius_percent*width/100, fill=0)
    result = Image.new("RGBA", (width, height))
    result.paste(image, (0, 0), mask)
    return result

def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        radius_text = radius_entry.get()
        if radius_text.strip():  # Kontrola, zda vstupní pole není prázdné
            radius_percent = int(radius_text)
            rounded_image = round_corners(file_path, radius_percent)
            rounded_image.thumbnail((300, 300))
            rounded_image_tk = ImageTk.PhotoImage(rounded_image)
            image_label.config(image=rounded_image_tk)
            image_label.image = rounded_image_tk
        else:
            messagebox.showerror("Error", "Please enter a radius percentage.")


root = Tk()
root.title("Round Image Tool")

radius_label = Label(root, text="Round Radius (%):")
radius_label.pack()

radius_entry = Entry(root)
radius_entry.pack()

select_button = Button(root, text="Select Image", command=select_image)
select_button.pack()

image_label = Label(root)
image_label.pack()

root.mainloop()