import cv2
import numpy as np
import time
import os
def toascii(originalimage):
    #originalimage = cv2.imread(path)
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



fileName=input('video path ?')
cap = cv2.VideoCapture(fileName)
while (cap.isOpened()):  # play the video by reading frame by frame
    ret, frame = cap.read()
    if ret == True:
        print(toascii(frame))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
