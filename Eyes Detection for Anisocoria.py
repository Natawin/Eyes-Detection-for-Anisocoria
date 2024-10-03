import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

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

def detect_eyes(image, output_text):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    if len(eyes) == 0:
        output_text.insert(tk.END, "Can't detect the eyes.\n")
        return None

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(image, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    
    return image

def compare_eyes(right_eye_path, left_eye_path, output_text):
    right_eye = cv2.imread(right_eye_path)
    left_eye = cv2.imread(left_eye_path)

    if right_eye is not None and left_eye is not None:
        right_eye_detected = detect_eyes(right_eye, output_text)
        left_eye_detected = detect_eyes(left_eye, output_text)

        if right_eye_detected is None or left_eye_detected is None:
            output_text.insert(tk.END, "Error in detecting eyes.\n")
            return

        white_percentage_right, black_percentage_right = calculate_inverted_white_black_percentage(right_eye_detected)
        white_percentage_left, black_percentage_left = calculate_inverted_white_black_percentage(left_eye_detected)

        white_diff = abs(white_percentage_right - white_percentage_left)
        black_diff = abs(black_percentage_right - black_percentage_left)

        output_text.insert(tk.END, f"White Percentage in Inverted Right Eye: {white_percentage_right:.2f}%\n")
        output_text.insert(tk.END, f"White Percentage in Inverted Left Eye: {white_percentage_left:.2f}%\n")
        output_text.insert(tk.END, f"Difference in White Percentage: {white_diff:.2f}%\n")

        if white_diff > 20 or black_diff > 20:
            output_text.insert(tk.END, "You are at risk of Anisocoria\n")
        else:
            output_text.insert(tk.END, "Your images are normal\n")
    else:
        messagebox.showerror("Error", "Could not load one or both eye images.")

def browse_file(entry):
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    entry.delete(0, tk.END)
    entry.insert(0, filepath)

def reset_output(output_text):
    output_text.delete("1.0", tk.END)


def start_gui():
    window = tk.Tk()
    window.title("Eye Image Comparison")

    # ตาซ้าย
    left_eye_label = tk.Label(window, text="Left Eye Image:")
    left_eye_label.grid(row=0, column=0, padx=10, pady=5)
    
    left_eye_entry = tk.Entry(window, width=40)
    left_eye_entry.grid(row=0, column=1, padx=10, pady=5)
    
    browse_left_button = tk.Button(window, text="Browse", command=lambda: browse_file(left_eye_entry))
    browse_left_button.grid(row=0, column=2, padx=10, pady=5)

    # ตาขวา
    right_eye_label = tk.Label(window, text="Right Eye Image:")
    right_eye_label.grid(row=1, column=0, padx=10, pady=5)
    
    right_eye_entry = tk.Entry(window, width=40)
    right_eye_entry.grid(row=1, column=1, padx=10, pady=5)
    
    browse_right_button = tk.Button(window, text="Browse", command=lambda: browse_file(right_eye_entry))
    browse_right_button.grid(row=1, column=2, padx=10, pady=5)

    
    output_label = tk.Label(window, text="Output:")
    output_label.grid(row=2, column=0, padx=10, pady=5)

    output_text = tk.Text(window, height=10, width=50)
    output_text.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

    compare_button = tk.Button(window, text="Compare", command=lambda: compare_eyes(right_eye_entry.get(), left_eye_entry.get(), output_text))
    compare_button.grid(row=4, column=0, columnspan=2, pady=10)

    reset_button = tk.Button(window, text="Reset", command=lambda: reset_output(output_text))
    reset_button.grid(row=4, column=1, pady=10)

    window.mainloop()

# เริ่มต้น GUI
if __name__ == "__main__":
    start_gui()
