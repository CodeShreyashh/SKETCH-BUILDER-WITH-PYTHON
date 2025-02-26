import cv2
import numpy as np

def pencil_sketch(image_path, output_path):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found!")
        return
    
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    inverted_image = 255 - gray_image
    
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)  
    inverted_blurred_image = 255 - blurred_image
    
    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    cv2.imwrite(output_path, pencil_sketch_image)
    
    cv2.imshow("Pencil Sketch", pencil_sketch_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = '2212775.jpg'  
output_path = 'pencil_sketch.jpg'  
pencil_sketch(image_path, output_path)
