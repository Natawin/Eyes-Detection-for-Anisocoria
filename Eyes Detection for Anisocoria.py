import cv2
import numpy as np

# ฟังก์ชันเพื่อกลับสีภาพและคำนวณเปอร์เซ็นต์ของพิกเซลสีขาวและสีดำ
def calculate_inverted_white_black_percentage(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = cv2.bitwise_not(gray)
    _, binary_image = cv2.threshold(inverted_image, 127, 255, cv2.THRESH_BINARY)
    total_pixels = binary_image.shape[0] * binary_image.shape[1]
    white_pixels = np.sum(binary_image == 255)
    black_pixels = total_pixels - white_pixels
    white_percentage = (white_pixels / total_pixels) * 100
    black_percentage = (black_pixels / total_pixels) * 100
    return white_percentage, black_percentage

def compare_eyes(right_eye_path, left_eye_path):
    right_eye = cv2.imread(right_eye_path)
    left_eye = cv2.imread(left_eye_path)

    if right_eye is not None and left_eye is not None:
        white_percentage_right, black_percentage_right = calculate_inverted_white_black_percentage(right_eye)
        white_percentage_left, black_percentage_left = calculate_inverted_white_black_percentage(left_eye)

        white_diff = abs(white_percentage_right - white_percentage_left)
        black_diff = abs(black_percentage_right - black_percentage_left)

        print(f"White Percentage in Inverted Right Eye: {white_percentage_right:.2f}%")
        print(f"White Percentage in Inverted Left Eye: {white_percentage_left:.2f}%")
        print(f"Difference in White Percentage: {white_diff:.2f}%")
        
        if white_diff > 20 or black_diff > 20:
            print("You are at risk of Anisocoria")
        else:
            print("Your images are normal")
    else:
        print("Could not load one or both eye images.")

right_eye_path = input("Please enter the path for the right eye image: ")
left_eye_path = input("Please enter the path for the left eye image: ")

compare_eyes(right_eye_path, left_eye_path)