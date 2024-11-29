from template import TEMPLATES  # Import the templates from template.py
import cv2 as cv
import numpy as np

# Function to recognize a single character using template matching
def recognize_character(character_image):
    max_corr = -1
    best_match = None

    for char_label, template_image in TEMPLATES.items():
        if template_image is None:
            continue  # Skip missing templates
        # Resize the character image to match the template size
        resized_char = cv.resize(character_image, (template_image.shape[1], template_image.shape[0]))
        # Calculate correlation
        correlation = cv.matchTemplate(resized_char, template_image, cv.TM_CCOEFF_NORMED)
        _, corr_value, _, _ = cv.minMaxLoc(correlation)  # Extract the maximum correlation value
        if corr_value > max_corr:
            max_corr = corr_value
            best_match = char_label
    return best_match

# Main function to process the license plate
def process_license_plate(image_path):
    # Step 1: Load the image and preprocess
    image = cv.imread(image_path)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    edges = cv.Canny(blurred, 100, 200)  # Edge detection

    # Step 2: Find contours to locate the license plate region
    contours, _ = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    license_plate_contour = None
    max_area = 0

    for contour in contours:
        area = cv.contourArea(contour)
        if area > max_area:
            max_area = area
            license_plate_contour = contour

    if license_plate_contour is None:
        print("License plate not found.")
        return ""

    x, y, w, h = cv.boundingRect(license_plate_contour)
    license_plate = gray[y:y+h, x:x+w]

    # Step 3: Binarize and clean up the license plate
    _, binary_plate = cv.threshold(license_plate, 127, 255, cv.THRESH_BINARY_INV)
    binary_plate_cleaned = cv.morphologyEx(binary_plate, cv.MORPH_CLOSE, np.ones((3, 3), np.uint8))

    # Step 4: Find contours within the license plate (characters)
    char_contours, _ = cv.findContours(binary_plate_cleaned, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    height, width = binary_plate_cleaned.shape
    characters = []

    for contour in char_contours:
        x, y, w, h = cv.boundingRect(contour)
        if h > height / 3 and w < width / 2:  # Filter based on character size
            char_crop = binary_plate_cleaned[y:y+h, x:x+w]
            characters.append((x, char_crop))

    # Sort characters from left to right
    characters = sorted(characters, key=lambda x: x[0])

    # Step 5: Recognize each character
    license_plate_text = ""
    for _, char_image in characters:
        recognized_char = recognize_character(char_image)
        if recognized_char:
            license_plate_text += recognized_char

    return license_plate_text

# Main Execution
if __name__ == "__main__":
    image_path = "/Users/murathatunoglu/Desktop/plate_recognition/license-plate-images/image (5).png"  # Path to the image containing the car license plate
    license_plate_text = process_license_plate(image_path)
    if license_plate_text:
        print(f"Recognized License Plate: {license_plate_text}")
    else:
        print("Failed to recognize the license plate.")
