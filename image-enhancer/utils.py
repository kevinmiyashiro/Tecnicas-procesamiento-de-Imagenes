import cv2
import numpy as np

def resize_max(img, max_dim=1024):
    h, w = img.shape[:2]
    if max(h, w) <= max_dim:
        return img
    scale = max_dim / float(max(h, w))
    return cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)

def denoise_fastnlmeans(img, h=10, hColor=10, templateWindowSize=7, searchWindowSize=21):
    return cv2.fastNlMeansDenoisingColored(img, None, h, hColor, templateWindowSize, searchWindowSize)

def apply_clahe(img, clipLimit=2.0, tileGridSize=(8,8)):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l,a,b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)
    l2 = clahe.apply(l)
    lab2 = cv2.merge((l2,a,b))
    return cv2.cvtColor(lab2, cv2.COLOR_LAB2BGR)

def unsharp_mask(img, kernel_size=(5,5), sigma=1.0, amount=1.0, threshold=0):
    blurred = cv2.GaussianBlur(img, kernel_size, sigma)
    sharpened = cv2.addWeighted(img, 1 + amount, blurred, -amount, 0)
    return sharpened

def bilateral_filter(img, d=9, sigmaColor=75, sigmaSpace=75):
    return cv2.bilateralFilter(img, d, sigmaColor, sigmaSpace)

def preset_cleanup(img):
    x = denoise_fastnlmeans(img, h=8, hColor=8)
    x = apply_clahe(x, clipLimit=2.0)
    return x

def preset_revive(img):
    x = denoise_fastnlmeans(img, h=6, hColor=6)
    x = apply_clahe(x, clipLimit=3.0)
    x = unsharp_mask(x, amount=0.8)
    return x

def preset_sharp(img):
    x = bilateral_filter(img, d=9, sigmaColor=60, sigmaSpace=60)
    x = unsharp_mask(x, amount=1.2)
    return x
