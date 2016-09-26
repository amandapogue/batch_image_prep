from PIL import Image
import numpy as np
import glob, os, math


# This bit of code asks the user to input the dimensions they want for their files
max_image_size = eval(raw_input("What max dimension size do you want your image to be in pixels? "))
canvas_width = eval(raw_input("What width do you want your canvas to be in pixels? "))
canvas_height = eval(raw_input("What height do you want your canvas to be in pixels? "))
extension = eval(raw_input("What extension would you like to add onto your filename? "))

# This bit of code makes a new folder for the modified files
os.makedirs(os.getcwd() + "/" + extension)

# This tells the program to resize all of the files in the folder of the type .png    
for infile in glob.glob("*.png"):
    file, ext = os.path.splitext(infile)

    image=Image.open(infile)
    image.load()

    # This bit of code autocrops the image 
    image_data = np.asarray(image)
    image_data_bw = image_data.max(axis=2)
    non_empty_columns = np.where(image_data_bw.max(axis=0)>0)[0]
    non_empty_rows = np.where(image_data_bw.max(axis=1)>0)[0]
    cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))

    image_data_new = image_data[cropBox[0]:cropBox[1]+1, cropBox[2]:cropBox[3]+1 , :]

    new_image = Image.fromarray(image_data_new)
    
    # This function takes the input from above and uses it to resize the file
    def image_resize(max_image_size, canvas_width, canvas_height, extension):
   
    	size = max_image_size, max_image_size
    	new_image.thumbnail(size)

        # This function resizes the canvas surrounding the image, centering it with
        # a transparent border
    	def resize_canvas(canvas_width, canvas_height):
        	
            # Determine the current dimensions of the image
            old_width, old_height = new_image.size
            
            # Center the image
            x1 = int(math.floor((canvas_width - old_width) / 2))
            y1 = int(math.floor((canvas_height - old_height) / 2))
            
            # Checks the image type and codes the new_background as transparent in all modes
            mode = new_image.mode
            if len(mode) == 1:  # L, 1
                new_background = (0)
            if len(mode) == 3:  # RGB
                new_background = (0,0,0)
            if len(mode) == 4:  # RGBA, CMYK
                new_background = (0,0,0,0)

            # Centers the image on the new canvas and saves the new file to the new folder
            newImage = Image.new(mode, (canvas_width, canvas_height), new_background)
            newImage.paste(new_image, (x1, y1, x1 + old_width, y1 + old_height))
            newImage.save(os.getcwd() + "/" + extension + "/" + file + "_" + extension + ".png", "PNG")

    	resize_canvas(canvas_width, canvas_height)
    image_resize(max_image_size, canvas_width, canvas_height, extension) 