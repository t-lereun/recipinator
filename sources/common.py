from pathlib import Path 

ROOT = Path(__file__).parents[1]

def read_txt(path):

    
    with open(path, 'r') as file:
        file_content = file.read()
    file.close()
    
    return file_content
