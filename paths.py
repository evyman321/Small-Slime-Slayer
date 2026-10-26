from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def getPath(*parts):
    return str(BASE_DIR.joinpath(*parts))
