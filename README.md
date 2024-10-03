# Anisocoria Risk Assessment Tool

## Overview

This project aims to assess the risk of **Anisocoria**, a condition where the pupils of the two eyes are unequal in size. Anisocoria can be a symptom of underlying medical conditions such as brain injury, glaucoma, or neurological disorders, which may pose significant health risks.

This tool uses **OpenCV** and **Tkinter** to compare images of the left and right eye, calculate the percentage of white and black pixels in the inverted images, and help detect discrepancies in the pupils' sizes. It also provides feedback on whether the user is at risk of Anisocoria.

## How Anisocoria Is Assessed

Anisocoria is characterized by a difference in pupil size between the two eyes. A difference of less than **1 millimeter** is usually considered normal. However, if the difference exceeds **1 millimeter**, it may indicate potential health risks, such as neurological disorders or glaucoma. This tool helps assess whether there is a significant difference in the size of the pupils by comparing pixel data from the inverted eye images.

## Features

- Detects eyes using **Haar Cascade Classifiers**.
- Inverts the color of the eye images and calculates the percentage of black and white pixels in each eye.
- Compares the white and black pixel percentages of both eyes to check for significant discrepancies.
- Provides a **GUI (Graphical User Interface)** for easy image input and comparison.
- Displays results with a suggestion on whether the user is at risk of Anisocoria based on the pixel percentage differences.

## Prerequisites

- **Python 3.x**
- **OpenCV** library
- **Tkinter** library (usually pre-installed with Python)

## Installation

To install the required packages, use the following commands:

```bash
pip install opencv-python
pip install numpy
```

## Usage Instructions
### 1.Ensure that the input images are consistent:

+Both eye images should have the same aspect ratio.
+The zoom level should be the same for both images (e.g., if the left eye is zoomed at x1, the right eye should also be zoomed at x1).
+The distance between the camera and the eyes should be consistent for both images.

### 2.Running the Tool:
+Simply execute the Python script using your Python interpreter:
```bash
python <script_name>.py
```

### 3.Using the GUI:
+Browse and select the images for the left and right eye.
+Click the Compare button to compare the pixel data of the two eye images.
+The results will be shown in the output box below, including whether the difference is significant enough to suggest the risk of Anisocoria.
+If you want to reset the output, click the Reset button.

## GUI Overview
+Left Eye Image: Browse and select the image of the left eye.
+Right Eye Image: Browse and select the image of the right eye.
+Compare Button: Click to compare the eye images.
+Output Section: Displays the percentage of white and black pixels for each eye and shows whether there is a risk of Anisocoria.
+Reset Button: Clears the output section for a new comparison.

## Code Structure
### 1. Eye Detection:
The tool uses OpenCV's Haar Cascade Classifier to detect eyes in the input images. If no eyes are detected, an error message is displayed.
### 2. Pixel Inversion and Calculation:
The tool converts the image to grayscale, inverts it, and calculates the percentage of white and black pixels. These values are then compared to detect significant differences.
### 3. Comparison Logic:
If the difference in white or black pixel percentages between the two eyes exceeds 20%, the tool flags the user as being at risk of Anisocoria. Otherwise, it indicates that the pupils are within a normal range.

Example Output
```plaintext
White Percentage in Inverted Right Eye: 62.34%
White Percentage in Inverted Left Eye: 59.23%
Difference in White Percentage: 3.11%
Your images are normal.
```

or

```plaintext
White Percentage in Inverted Right Eye: 72.45%
White Percentage in Inverted Left Eye: 50.23%
Difference in White Percentage: 22.22%
You are at risk of Anisocoria.
```

## Limitations
The tool assumes consistent image quality and zoom levels. Variations in image resolution, lighting, and zoom can affect the accuracy of the results.
The tool assesses risk based on pixel differences but does not replace a medical diagnosis. If you are concerned about the condition of your eyes, consult a medical professional.
