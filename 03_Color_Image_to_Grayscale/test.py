import numpy as np
from PIL import Image
from tkinter import Tk
from tkinter import filedialog
import matplotlib.pyplot as plt

#loading the image
Tk().withdraw()
file_path = filedialog.askopenfilename()
data = Image.open(file_path)

#Converting image to an array
img = np.array(data)

#Get intital data from the array
print(data.format, data.size, data.mode)
print(type(img))
print(img.dtype)
print(img.ndim)
print(img.shape)

# #Plotting the Color image
plt.imshow(img) 
plt.axis('off')
plt.savefig("og.jpg")
plt.show()


#Converting RGB Channel to Grayscale

def Grayscale_engine(R, G, B):
    Grayscale = 0.299*R + 0.587*G + 0.114*B
    return Grayscale

vecotrized_Grayscale_engine = np.vectorize(Grayscale_engine)

Grayscale_image = vecotrized_Grayscale_engine(
    #Here these 3 dots(Ellipsis) tells python  to include every dimension that comes before this point.
    # (Height, Width, 3) -> img[..., 0] -> means give me all rows, all columns, only the first color channel index(0)
    #syntax (3 dots) is built in python object, 2 dots would look like an error 
    img[..., 0],
    img[..., 1],
    img[..., 2]
    )
    
#Grayscale image data
print(type(Grayscale_image))
print(Grayscale_image.shape)
print(Grayscale_image.dtype)
print(Grayscale_image.ndim)

# #Plotting the Grayscale image
plt.imshow(Grayscale_image, cmap='gray') 
plt.axis('off')
plt.savefig("grayscale.jpg")
plt.show()