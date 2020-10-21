import os
import glob
import csv

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar, LTTextBoxHorizontal

def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)

record = False
survivor_name = ""
path = "../../Hunger/Lodz Transcripts"
file_names_with_errors = []

with open("Lodz_Transcript_Names.csv", mode="w") as names_file:
    file_writer = csv.writer(names_file, delimiter=",")
    for file_name in glob.glob(os.path.join(path, "*.pdf")):
        for page in extract_pages(file_name):
            for element in page:
                if isinstance(element, LTTextBoxHorizontal):
                    if "VHA - Testimony" in element.get_text():
                        survivor_name = element.get_text().split(" - ")[2].rstrip("\n")

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
                                file_names_with_errors.append(file_name)
                                continue

#                            print(name + ", " + first_name + ", " + last_name + ", " + "[" + description + "]" + ", " + survivor_name)
                            
                            file_writer.writerow([name, first_name, last_name, description, survivor_name])
                            
                    if element.get_text() == "All People\n": 
                        record = True

print(file_names_with_errors)

