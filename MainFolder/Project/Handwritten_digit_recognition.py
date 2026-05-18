import pygame
import sys
import numpy as np
import cv2
from keras.models import load_model
from pygame.locals import *

# ---------------- SETTINGS ----------------
WINDOWSIZEX = 640
WINDOWSIZEY = 480

BOUNDARYINC = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

IMAGESAVE = False  # set True if you want to save drawings

MODEL = load_model("bestmodel.h5")

LABELS = {
    0: "Zero", 1: "One",
    2: "Two", 3: "Three",
    4: "Four", 5: "Five",
    6: "Six", 7: "Seven",
    8: "Eight", 9: "Nine"
}

# ---------------- INIT ----------------
pygame.init()

FONT = pygame.font.Font("freesansbold.ttf", 18)

DISPLAYSURF = pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY))
pygame.display.set_caption("Digit Board")

iswriting = False

number_xcord = []
number_ycord = []

image_cnt = 0

# ---------------- MAIN LOOP ----------------
while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # start drawing
        if event.type == MOUSEBUTTONDOWN:
            iswriting = True

        # stop drawing → process image
        if event.type == MOUSEBUTTONUP:
            iswriting = False

            if len(number_xcord) > 0 and len(number_ycord) > 0:

                number_xcord = sorted(number_xcord)
                number_ycord = sorted(number_ycord)

                rect_min_x = max(number_xcord[0] - BOUNDARYINC, 0)
                rect_max_x = min(number_xcord[-1] + BOUNDARYINC, WINDOWSIZEX)

                rect_min_y = max(number_ycord[0] - BOUNDARYINC, 0)
                rect_max_y = min(number_ycord[-1] + BOUNDARYINC, WINDOWSIZEY)

                # reset cords
                number_xcord = []
                number_ycord = []

                # extract screen area
                img_arr = np.array(pygame.PixelArray(DISPLAYSURF))[
                    rect_min_x:rect_max_x,
                    rect_min_y:rect_max_y
                ].T.astype(np.float32)

                # optional save
                if IMAGESAVE:
                    cv2.imwrite(f"image_{image_cnt}.png", img_arr)
                    image_cnt += 1

                # ---------------- PREDICTION ----------------
                try:
                    image = cv2.resize(img_arr, (28, 28))
                    image = np.pad(image, ((10, 10), (10, 10)), 'constant', constant_values=0)
                    image = cv2.resize(image, (28, 28)) / 255.0

                    prediction = MODEL.predict(image.reshape(1, 28, 28, 1), verbose=0)
                    label = LABELS[np.argmax(prediction)]

                    textSurface = FONT.render(label, True, RED, WHITE)
                    textRect = textSurface.get_rect()
                    textRect.left, textRect.bottom = rect_min_x, rect_max_y

                    DISPLAYSURF.blit(textSurface, textRect)

                except Exception as e:
                    print("Prediction error:", e)

        # drawing motion
        if event.type == MOUSEMOTION and iswriting:
            xcord, ycord = event.pos

            pygame.draw.circle(DISPLAYSURF, WHITE, (xcord, ycord), 4)

            number_xcord.append(xcord)
            number_ycord.append(ycord)

        # clear screen
        if event.type == KEYDOWN:
            if event.unicode == "n":
                DISPLAYSURF.fill(BLACK)

    pygame.display.update()