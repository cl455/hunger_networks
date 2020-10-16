from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar, LTTextBoxHorizontal

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

record = False

for page in extract_pages("./Abraham Peter_37735_M.pdf"):
    for element in page:
        if isinstance(element, LTTextBoxHorizontal):
            if element.get_text() == "Transcript\n":
                record = False
                
            if record == True:
                if hasNumbers(element.get_text()): 
                    continue
                if "VHA" in element.get_text():
                    continue
                else: 
                    print(element.get_text())
            
                
            if element.get_text() == "All People\n": 
                record = True
            
