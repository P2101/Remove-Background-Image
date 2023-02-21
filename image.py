# pip install rembg
from rembg import remove 
from PIL import Image

# REQUEST THE IMAGE
input_path = 'original.jpeg'
# CREATE THE NAME OF THE NEW IMAGE
output_path = 'without-background.png'
# OPEN THE IMAGE
bg = Image.open(input_path)
# REMOVE THE BACKGROUND 
output = remove(bg)
# SAVING THE NEW IMAGE WITH THE NAME INDICATED
output.save(output_path)
