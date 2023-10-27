import pytesseract
from PIL import Image
import spacy

pytesseract.pytesseract.tesseract_cmd = r''

# def extract_dialogue_info_from_image(image_path):

#     # Load the spaCy English language model
#     nlp = spacy.load("en_core_web_sm")

#     # Tesseract OCR to extract text from the image
#     image = Image.open(image_path)
#     extracted_text = pytesseract.image_to_string(image)

#     # print(extracted_text)

#     # Initialize variables to store the results
#     results = {}
#     current_time = None

#     # Split the extracted text by lines
#     lines = extracted_text.strip().split('\n')
#     # print(lines)

#     for line in lines:

#         # print(line)
#         # Check if the line contains a time (e.g., '3:00 PM')
#         if any(time_str in line for time_str in ('AM', 'PM')):
#             current_time = line.strip()
#             results[current_time] = [[], []]  # Initialize empty lists for nouns and verbs
#         else:
#             # Extract nouns and verbs from the dialogue text
#             dialogue_text = line.strip()
#             doc = nlp(dialogue_text)  # You can use spaCy as you did before
#             nouns = [token.text for token in doc if token.pos_ == "NOUN"]
#             verbs = [token.text for token in doc if token.pos_ == "VERB"]

#             if current_time:
#                 results[current_time][0].extend(nouns)
#                 results[current_time][1].extend(verbs)

#     return results


def extract_dialogue_info_from_image(image_path):
    # Load the spaCy English language model
    nlp = spacy.load("en_core_web_sm")

    # Use Tesseract OCR to extract text from the image
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)

    # Initialize variables to store the results for each line
    dialogue_info = []

    # Split the extracted text by lines
    lines = extracted_text.strip().split('\n')

    for line in lines:
        # Extract nouns, verbs, and adjectives for each line
        line_info = {'nouns': [], 'verbs': [], 'adjectives': []}
        line_text = line.strip()
        line_doc = nlp(line_text)

        for token in line_doc:
            if token.pos_ == "NOUN":
                line_info['nouns'].append(token.text)
            elif token.pos_ == "VERB":
                line_info['verbs'].append(token.text)
            elif token.pos_ == "ADJ":
                line_info['adjectives'].append(token.text)

        # Append the line's information to the list
        dialogue_info.append(line_info)

    return dialogue_info

def For_noun_verb_adj(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)

    nouns = [token.text for token in doc if token.pos_ == "NOUN"]
    adjectives = [token.text for token in doc if token.pos_ == "ADJ"]
    verbs = [token.text for token in doc if token.pos_ == "VERB"]

    return nouns,adjectives,verbs