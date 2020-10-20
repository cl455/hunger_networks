import os
import glob

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar, LTTextBoxHorizontal

def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)

record = False
survivor_name = ""
path = "../../Hunger/Lodz Transcripts"

for file_name in glob.glob(os.path.join(path, "*.pdf")):
    for page in extract_pages(file_name):
        for element in page:
            if isinstance(element, LTTextBoxHorizontal):
                if "VHA - Testimony" in element.get_text():
                    survivor_name = element.get_text().split(" - ")[2]

                if element.get_text() == "Transcript\n":
                    record = False

                if record == True:
                    name_and_description = element.get_text()
                    if has_numbers(name_and_description): 
                        continue

                    elif "VHA" in name_and_description:
                        continue

                    else:
                        name = name_and_description.split(" - ")[0]
                        first_name = name.split(" ")[0]
                        if " " in name: 
                            last_name = name.split(" ")[1]
                        else:
                            last_name = ""
                        try:
                            description = name_and_description.split(" - ")[1].rstrip("\n")
                        except IndexError:
                            continue

                        print(name + ", " + first_name + ", " + last_name + ", " + "[" + description + "]" + ", " + survivor_name)

                if element.get_text() == "All People\n": 
                    record = True

