URL = "https://ibanknet.com/scripts/callreports/getbank.aspx?ibnid=usa_1039502"
captcha_text="Please verify you are human by typing the text below and clicking submit."

import cv2 
import pytesseract


def captcha_solver(img):
    captcha=pytesseract.image_to_string(img)
    return captcha