import pytesseract
from PIL import Image
import spacy

pytesseract.pytesseract.tesseract_cmd = r''

def extract_dialogue_info_from_image(image_path):

    # Load the spaCy English language model
    nlp = spacy.load("en_core_web_sm")

    # Now, you can use the `nlp` object for natural language processing tasks.

    # Use Tesseract OCR to extract text from the image
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)

    # print(extracted_text)

    # Initialize variables to store the results
    results = {}
    current_time = None

    # Split the extracted text by lines
    lines = extracted_text.strip().split('\n')
    # print(lines)

    for line in lines:

        # print(line)
        # Check if the line contains a time (e.g., '3:00 PM')
        if any(time_str in line for time_str in ('AM', 'PM')):
            current_time = line.strip()
            results[current_time] = [[], []]  # Initialize empty lists for nouns and verbs
        else:
            # Extract nouns and verbs from the dialogue text
            dialogue_text = line.strip()
            doc = nlp(dialogue_text)  # You can use spaCy as you did before
            nouns = [token.text for token in doc if token.pos_ == "NOUN"]
            verbs = [token.text for token in doc if token.pos_ == "VERB"]

            if current_time:
                results[current_time][0].extend(nouns)
                results[current_time][1].extend(verbs)

    return results


# Example usage:
# image_path = "your_image.png"  # Replace with the path to your image
# result_dict = extract_dialogue_info_from_image(image_path)
# print(result_dict)