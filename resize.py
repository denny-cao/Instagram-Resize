import tkinter as tk
from tkinter import filedialog
from PIL import Image


def main():
    filepaths = filedialog.askopenfilenames(title="Select Images",
                                            filetypes=(("Image Files",
                                                        "*.png *.jpg"),
                                                       ("All Files", "*.*")))
    dimensions = getDimensions(filepaths)

    name_counter = 0
    for path in filepaths:
        borders(scale(path, dimensions), dimensions, name_counter)
        name_counter += 1


def getDimensions(images):
    largest_width = 0
    largest_height = 0
    for image in images:
        with Image.open(image) as im:
            if im.width > largest_width:
                largest_width = im.width
            if im.height > largest_height:
                largest_height = im.height
    return (largest_width, largest_height)


def scale(image, dimensions):
    scale_factor = 0
    with Image.open(image) as im:
        if im.width >= im.height:
            scale_factor = dimensions[0]/im.width
        else:
            scale_factor = dimensions[1]/im.height
        return im.resize((int(im.width * scale_factor),
                          int(im.height * scale_factor)))


def borders(scaled_image, dimensions, name_counter):
    new_im = Image.new("RGB", dimensions)
    new_im.paste(scaled_image, (int((dimensions[0] - scaled_image.width)/2),
                                int((dimensions[1] - scaled_image.height)/2)))
    new_im.save(f"{name_counter}.png")


window = tk.Tk()
window.title("Resize Images")
window.geometry("500x500")
button = tk.Button(text="Resize Images", command=main)
button.pack()
window.mainloop()
