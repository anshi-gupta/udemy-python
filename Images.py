## In the folder "Working with Images" (same folder this notebook is located in) there are two images we will be working with:

##      word_matrix.png
##      mask.png

##The word_matrix is a .png image that contains a spreadsheet of words with a hidden message in it.
##Your task is to use the mask.png image to reveal the hidden message inside the word_matrix.png.

from PIL import Image

word_matrix = Image.open('word_matrix.png')
mask = Image.open('mask.png')
resized_mask = mask.resize((1015, 559))
resized_mask.putalpha(200)
word_matrix.paste(resized_mask, (0, 0), resized_mask)
word_matrix.save('Hidden_message.png', format='png')
hm = Image.open('Hidden_message.png')
hm.show()