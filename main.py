import os
import easyocr
import cv2
import numpy as np
import random

INPUT_DIR = 'input/'
OUTPUT_DIR = 'output/'

# SEARCH_TEXTS = ['Hello Fellas',  'Put Your Text You want to Search for Here!']
SEARCH_TEXTS = ['remember']
os.makedirs(OUTPUT_DIR, exist_ok=True)

reader = easyocr.Reader(['en'])

for filename in os.listdir(INPUT_DIR):
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
        image_path = os.path.join(INPUT_DIR, filename)
        img = cv2.imread(image_path)
        
        result = reader.readtext(image_path)
        
        overlay = np.zeros_like(img, dtype=np.uint8)
        overlay.fill(255)  # Fill with white
        
        text_found = False
        detected_texts = []
        for detection in result:
            text = detection[1]
            for search_text in SEARCH_TEXTS:
                if search_text in text:
                    text_found = True
                    detected_texts.append(text)
                    bbox = detection[0]
                    cv2.rectangle(overlay, tuple(bbox[0]), tuple(bbox[2]), (0, 0, 0), -1)  # Fill with black
                    break  
        
        if text_found:
            random_filename = str(random.randint(10000, 99999))  # Generate a 5-digit random number
            output_image_path = os.path.join(OUTPUT_DIR, f"{random_filename}.png")
            output_text_path = os.path.join(OUTPUT_DIR, f"{random_filename}.txt")
            
            cv2.imwrite(output_image_path, cv2.addWeighted(img, 1, overlay, 0.5, 0))
            
            with open(output_text_path, 'w') as f:
                for text in detected_texts:
                    f.write(text + '\n')
            
            print(f"Processed: {filename} - Saved as: {output_image_path}")
            print(f"Text saved to: {output_text_path}")
        else:
            print(f"Skipped: {filename} - Specific texts not found")
