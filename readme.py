from .create_readme_md import Readme
from .create_readme_json import ReadmeData


def create_readme():
    '''Create Readme for 1st Time'''

    ReadmeData() # Create readme.json
    Readme() # Create readme.md

def update_readme():
    '''
    Update readme.json: and call this function to see
    changes being reflected in readme.json
    '''
    Readme()