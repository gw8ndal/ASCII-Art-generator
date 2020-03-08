from PIL import Image
import io
import easygui
from resizeimage import resizeimage
import webbrowser

print('What resolution should be the final image ?')
resX = int(input('Resoltion X ='))
resY = int(input('Resoltion Y ='))

image_path = easygui.fileopenbox()
image_original = Image.open(image_path)


image = resizeimage.resize_thumbnail(image_original, [resX, resY]) 

largeur, hauteur = image.size

output = io.StringIO()

image_nb = image.convert('L')

for y in range(0, hauteur, 2):
    for x in range(largeur):
        value = image_nb.getpixel((x, y))
        if value < 64:
            output.write('@')

        elif value < 128:
            output.write('#')

        elif value < 192:
            output.write('/')
        else :
            output.write(',')
    output.write('\n')

with open('Final image.txt', mode='w') as f: 
    print(output.getvalue(), file=f)

webbrowser.open('Final image.txt')