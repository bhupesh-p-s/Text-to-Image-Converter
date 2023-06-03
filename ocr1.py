from nanonets import NANONETSOCR
import os
import sys
import cv2
from gtts import gTTS

async def read_image(img_path):

    model = NANONETSOCR()
    model.set_token('8353140a-fe38-11ed-b0f2-9a7cae96d88d')

    try:
        response = model.convert_to_string(img_path, formatting='lines and spaces')
        return response
    except:
        return "[ERROR] Unable to process file: {0}".format(img_path)

