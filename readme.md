# Batch script for resizing images for studies
#### Author: Amanda Pogue
#### Date last edited: September 19, 2016
This is just a small snippet of python code that will allow you to batch update images in a folder. Put this file in a folder full of images. When called it will prompt you for the max dimension size you want your image sized to, what width and height you would like the canvas to be, and what extension you would like to append to the filename for the new files (this will also create a new folder within the source folder with the extension name; the program itself will append the _extensionName to your files). It will then autocrop your images and resize them to your specification. Simple. Easy. It'll save your RAs countless boring hours of image editing.

#### Notes:
* this code is currently written to take .png files and export .png files, you can easily edit it to take other image file types, and could easily be edited to take multiple file types.
* this code will not remove backgrounds for you. PIL in pyhton does have a sort of function to allow you to swap colors (from color X to trasnparent), but that is not included in this snippet.