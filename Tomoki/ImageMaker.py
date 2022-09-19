import cv2
import numpy as np

#blank = np.zeros((28, 28, 3))
#blank += 255
#cv2.imwrite('white.png',blank)

letters = cv2.imread('letters.png')
letters = cv2.bitwise_not(letters)
letters = cv2.rotate(letters, cv2.ROTATE_90_CLOCKWISE)
letters = cv2.flip(letters, 1)
for i in range(26):
  letter = letters[2+30*i:30+30*i, 2:30]
  cv2.imwrite(f'./letters/letter{10+i}.png', letter)