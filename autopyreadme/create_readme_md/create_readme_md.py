import json
from datetime import date

class Readme:
    '''Create Readme.md'''

    def __init__(self) -> None:
        # read from json file to data variable
        with open('readme.json', 'r') as f:
            self.data = json.load(f)

        # open readme.md - New
        file = open('readme.md', 'w')
        file.close()

        # open readme.md - Append
        self.file = open('readme.md', 'a')

        # Adding Sections to readme.md
        self.add_description()
        self.add_authors()
        self.add_license()
        self.add_scripts()
        self.add_readers_notes()
        self.add_important_links()
        self.add_dependencies()
        self.add_date()

        # close readme.md
        self.file.close()

    def add_description(self) -> None:
        '''Add Description to Readme.md'''

        description = self.data['description']
        project_name = self.data['project_name']

        if description == '': return

        if project_name == '': project_name = 'PyProject:'

        self.file.write(f'### {project_name}:\n\n')
        self.file.write(description + '\n\n')

    
    def add_authors(self) -> None:
        '''Add Authors to Readme.md'''

        authors = self.data['authors']

        if authors == [""]: return

        self.file.write('### Authors:\n\n')
        
        authors_string = ''

        for author in authors:
            authors_string+= author.strip()
            authors_string+= ' | '
        
        authors_string = authors_string[:-3]

        self.file.write(authors_string + '\n\n')
    

    def add_license(self) -> None:
        '''Add License to Readme.md'''

        if self.data['license'] == None: return

        self.file.write('### License:\n\n')
        self.file.write(self.data['license'] + '\n\n')

    
    def add_scripts(self) -> None:
        '''Add Scripts to Readme.md'''

        scripts = self.data['commands'] # dictionary of commands

        if scripts == dict(): return
        
        self.file.write('### Scripts:\n\n')

        for script_key, script_value in scripts.items():
            self.file.write('**'+script_key+':**\n\n')
            self.file.write('\t'+script_value+'\n\n')
        
            self.file.write('\n')
        

    def add_readers_notes(self) -> None:
        '''Add Reader's Notes to Readme.md'''

        readers_notes = self.data['readers_note']

        if readers_notes == dict(): return
        
        self.file.write('### Reader\'s Notes:\n\n')

        for note_key, note_value in readers_notes.items():
            self.file.write('**'+note_key+':**  '+note_value+'\n\n')
        
        self.file.write('\n')
    

    def add_important_links(self) -> None:
        '''Add Important Links to Readme.md'''

        important_links = self.data['important_links']

        if important_links == dict(): return

        self.file.write('### Check These Out:\n\n')
        
        imp_links_string = ''

        for link_key, link_value in important_links.items():
            imp_links_string += f'[{link_key}]({link_value}) | '
        
        imp_links_string = imp_links_string[:-2]
        
        self.file.write(imp_links_string+'\n\n')


    def add_dependencies(self) -> None:
        '''Add Project Dependencies to Readme.md'''

        dependencies = self.data['dependencies']

        if dependencies == []: return
        
        self.file.write('### Project Dependencies:\n\n')

        for dep in dependencies:
            self.file.write(f'\t{dep}\n')

    def add_date(self) -> None:
        '''Add Date Created On to Readme.md'''

        today_date = str(date.today())
        self.file.write(f'\n**Published On:** {today_date}\n')

if __name__ == '__main__':
    Readme()