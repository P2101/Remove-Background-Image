from rembg import remove # pip install rembg
from PIL import Image

# REQUEST THE IMAGE
input_path = 'lapo.jpeg'
# CREATE THE NAME OF THE NEW IMAGE
output_path = 'solo.png'
# OPEN THE IMAGE
bg = Image.open(input_path)
# REMOVE THE BACKGROUND 
output = remove(bg)
# SAVING THE NEW IMAGE WITH THE NAME INDICATED
output.save(output_path)
