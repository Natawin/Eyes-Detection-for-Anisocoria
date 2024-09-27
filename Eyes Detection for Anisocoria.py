import cv2
import numpy as np

# ฟังก์ชันเพื่อแปลงเป็นภาพขาวดำและคำนวณเปอร์เซ็นต์ของพิกเซลสีขาวและสีดำ
def calculate_white_black_percentage(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    total_pixels = binary_image.shape[0] * binary_image.shape[1]
    white_pixels = np.sum(binary_image == 255)
    black_pixels = total_pixels - white_pixels
    white_percentage = (white_pixels / total_pixels) * 100
    black_percentage = (black_pixels / total_pixels) * 100
    return white_percentage, black_percentage

def compare_eyes(right_eye_path, left_eye_path):
    white_percentage_right, black_percentage_right = calculate_white_black_percentage(right_eye_path) 
    white_percentage_left, black_percentage_left = calculate_white_black_percentage(left_eye_path)
    white_diff = abs(white_percentage_right - white_percentage_left)
    black_diff = abs(black_percentage_right - black_percentage_left)
    
    print(f"White Percentage in Right Image: {white_percentage_right:.2f}%")
    print(f"White Percentage in Left Image: {white_percentage_left:.2f}%")
    print(f"Difference in White Percentage: {white_diff:.2f}%")
    if white_diff > 20 or black_diff > 20:
        print("You are at risk of Anisocoria")
    else:
        print("Your images are normal")

right_eye_path = input("Please enter the path for Right Image: ")
left_eye_path = input("Please enter the path for Left Image: ")

compare_eyes(right_eye_path, left_eye_path)
