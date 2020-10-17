from tkinter import *
import cv2
import numpy as np


def toascii(path):
    originalimage = cv2.imread(path)
    main_image = cv2.cvtColor(originalimage, cv2.COLOR_BGR2GRAY)
    dimensions = main_image.shape
    x = dimensions[0]
    y = dimensions[1]

    main_image = cv2.resize(main_image, (200, int(120*x/y)))
    dimensions = main_image.shape
    print(dimensions)
    x = dimensions[0]
    y = dimensions[1]
    frame = main_image
    cols = y
    rows = x
    height, width = frame.shape
    cell_width = width / cols
    cell_height = height / rows
    if cols > width or rows > height:
        raise ValueError('Too many cols or rows.')
    result = ""
    for i in range(rows):
        for j in range(cols):
            gray = np.mean(
                frame[int(i * cell_height):min(int((i + 1) * cell_height), height), int(j * cell_width):min(int((j + 1) * cell_width), width)]
            )
            result += graytochar(gray)
        result += '\n'
    return result


def graytochar(gray):
    char_list = ' .:-=+*#%@'
    num_chars = len(char_list)
    return char_list[
        min(
            int(gray * num_chars / 255),
            num_chars - 1
        )
    ]

"""
def sayhello():
    window.destroy()
    print('taking results of entries...')
    resultat = myEntry.get()
    filepath = myEntry2.get()
    print('results taken !')
    print('converting image...')
    final = toascii(resultat)
    print('image converted !')
    print('writing final document...')
    if filepath[-1] != '/':
        filepath += '/'
    filepath += 'finalfile.txt'
    finalfile = open(filepath, 'w')
    finalfile.write(final)
    finalfile.close()
    print('final document written !')
    print('end')


print('begining')
print('creating window...')
window = Tk()
window.title('ImageToAscii')
window.geometry("510x300")
window.minsize(300, 300)
texte1 = Label(window, text='Type image path here...', font=("Regular", 20), bg='#955D53', fg='orange')
texte1.pack(side='top')

window.config(background='#955D53')

myEntry = Entry(window, width=40)
myEntry.pack(pady=20)

texte2 = Label(window, text='Type text path here...', font=("Regular", 20), bg='#955D53', fg='orange')
texte2.pack(side='top')

myEntry2 = Entry(window, width=40)
myEntry2.pack(pady=20)

texte3 = Label(window, text='Press that after writing in paths, after 5 second, you will find text in the path you made', font=("Regular", 12), bg='#955D53', fg='orange')
texte3.pack(side='top')

btn = Button(window, height=2, width=10, text="PRESS", font=("Regular", 30), command=sayhello)
btn.pack()
print('window created !')

window.mainloop()
"""
final = toascii('/Users/cdupouy/Desktop/images.jpg')
finalfile = open('/Users/cdupouy/Desktop/doc.txt', 'w')
finalfile.write(final)
finalfile.close()