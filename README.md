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
