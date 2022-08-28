from docx import Document
from typing import Dict, BinaryIO


def docx_to_list(file: BinaryIO) -> Dict:
    content = []
    doc = Document(file)
    list_text = []
    for paragraph in doc.paragraphs:
        list_text.append(paragraph.text)
    max_len = 0
    for i in range(len(list_text)):
        if len(list_text[i]) > max_len:
            max_len= len(list_text[i])
        if len(list_text[i]) > 10:
            content.append((list_text[i]))
    return {'sentences': content}
