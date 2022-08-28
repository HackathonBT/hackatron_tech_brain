import shutil
from typing import Dict
from fastapi import UploadFile, File
from app.services.convert import docx_to_list


def load_file(file: UploadFile = File(...)) -> Dict:
    data = docx_to_list(file=file.file._file)
    return data
