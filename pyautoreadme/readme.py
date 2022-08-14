from .create_readme_md.create_readme_md import Readme
from .create_readme_json.create_readme_json import ReadmeData


def create():
    '''Call to Create Readme for 1st Time'''

    ReadmeData() # Create readme.json
    Readme() # Create readme.md

def update():
    '''
    Call to Update readme.json: and call this function to see
    changes being reflected in readme.json
    '''
    Readme()