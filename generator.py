#!/usr/bin/env python3

import io
import easygui
from resizeimage import resizeimage
import webbrowser

def main():
    print("Quelle largeur doit faire l'image finale ?")

    resX = int(input('Largeur = '))
    resY = resX

    image_path = easygui.fileopenbox()
    image_original = Image.open(image_path)

    image = resizeimage.resize_thumbnail(image_original, [resX, resY])

    largeur, hauteur = image.size

    output = io.StringIO()

    image_nb = image.convert('L')

    for y in range(0, hauteur, 2):
        for x in range(largeur):
            value = image_nb.getpixel((x, y))
            if value < 28:
                output.write('@')
            elif value < 56:
                output.write('%')
            elif value < 84:
                output.write('#')
            elif value < 112:
                output.write('*')
            elif value < 140:
                output.write('+')
            elif value < 168:
                output.write('=')
            elif value < 196:
                output.write('-')
            elif value < 224:
                output.write(':')
            else :
                output.write('.')
        output.write('\n')

    with open('Final image.txt', mode='w') as f:
        print(output.getvalue(), file=f)

    webbrowser.open('Final image.txt')

if __name__ == '__main__':
    main()

