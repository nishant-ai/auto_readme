from .create_readme_md import Readme
from .create_readme_json import ReadmeData


def create_readme():
    '''Call to Create Readme for 1st Time'''

    ReadmeData() # Create readme.json
    Readme() # Create readme.md

def update_readme():
    '''
    Call to Update readme.json: and call this function to see
    changes being reflected in readme.json
    '''
    Readme()