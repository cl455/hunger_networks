from pdfminer.high_level import extract_text_to_fp
import sys
if sys.version_info > (3, 0):
     from io import StringIO
else:
     from io import BytesIO as StringIO
from pdfminer.layout import LAParams
output_string = StringIO()
with open('Abraham Peter_37735_M.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string, laparams=LAParams(), output_type='html', codec=None)
    print(output_string.getvalue())