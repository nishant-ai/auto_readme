import os
import json
from colorama import Fore, Style


class ReadmeData:
    '''
    Create Readme.json -> this file can be updated to
    change the Readme.md after calling update_readme()
    '''

    def __init__(self) -> None:
        self.licenses = [
            None, 'afl-3.0','apache-2.0','artistic-2.0','bsl-1.0','bsd-2-clause','bsd-3-clause',
            'bsd-3-clause-clear','cc','cc0-1.0','cc-by-4.0','cc-by-sa-4.0','wtfpl','ecl-2.0','epl-1.0',
            'epl-2.0','eupl-1.1','agpl-3.0','gpl','gpl-2.0','gpl-3.0','lgpl','lgpl-2.1','lgpl-3.0','isc',
            'lppl-1.3c','ms-pl','mit','mpl-2.0','osl-3.0','postgresql','ofl-1.1','ncsa','unlicense','zlib'
        ]

        self.readme_data = {
            'project_name': '',
            'authors': [], # list of authors
            'description': None, # string
            'license': None, # string
            'important_links': dict(), # link title : link
            'readers_note': dict(), # title : note
            'commands': dict(), # cmd title : cmd
            'dependencies': [], # project dependencies
        }

        # Welcome Message
        print(Fore.CYAN, Style.BRIGHT, end="")
        print(" Hello, Welcome to Readme Generator :) ", Style.RESET_ALL)
        
        # Prompt Input
        print(Fore.LIGHTBLUE_EX, end="\n")
        print("  Please Enter the details about project... ")
        print(Fore.GREEN)

        try:
            self.set_project_name()
            self.set_authors()
            self.set_description()
            self.set_license()
            self.set_important_links()
            self.set_readers_note()
            self.set_commands()
            self.set_dependencies()
            self.set_project_structure()
            self.save_data()

            print(Fore.CYAN, Style.BRIGHT, "README JSON CREATED SUCCESSFULLY! IF YOU WANT TO EDIT THE DATA, EDIT IT IN README.JSON AND RUN UPDATES (update_readme())")
        
        except Exception as e:
            print(Fore.RED, Style.RESET_ALL, e)


    def save_data(self):
        '''Save All Data (JSON) to Readme.md'''

        json_obj = json.dumps(self.readme_data, indent=4)
        with open('readme.json', 'w') as f:
            f.write(json_obj)


    def set_data(self, attribute):
        '''Helper Function used in various entries'''

        while True:
            title = input("Enter Title: ")

            if title == "":
                break

            value = input("Enter Value: ")

            self.readme_data[attribute][title] = value

    
    def set_project_name(self) -> None:
        self.readme_data['project_name'] = input("  # Project Name: ")
        print()

    def set_authors(self) -> None:
        self.readme_data['authors'] = input("  # Authors (author 1, author 2, etc...): ").split(',')
        print()


    def set_description(self) -> None:
        self.readme_data['description'] = input('  # Description: ')
        print()
    

    def set_license(self) -> None:
        print(Fore.WHITE, Style.DIM, "Choose license (1 - 35)\n")
        print('1: None \t\t\t\t\t\t\t 2: Academic Free License v3.0 (afl-3.0)')
        print('3: Apache license 2.0 (apache-2.0) \t\t\t\t 4: Artistic license 2.0 (artistic-2.0)')
        print('5: Boost Software License 1.0 (bsl-1.0) \t\t\t 6: BSD 2-clause "Simplified" license (bsd-2-clause)')
        print('7: BSD 3-clause "New" or "Revised" license (bsd-3-clause) \t 8: BSD 3-clause Clear license (bsd-3-clause-clear)')
        print('9: Creative Commons license family (cc) \t\t\t 10: Creative Commons Zero v1.0 Universal (cc0-1.0)')
        print('11: Creative Commons Attribution 4.0 (cc-by-4.0) \t\t 12: Creative Commons Attribution Share Alike 4.0 (cc-by-sa-4.0)')
        print('13: Do What The F*ck You Want To Public License (wtfpl) \t 14: Educational Community License v2.0 (ecl-2.0)')
        print('15: Eclipse Public License 1.0 (epl-1.0) \t\t\t 16: Eclipse Public License 2.0 (epl-2.0)')
        print('17: European Union Public License 1.1 (eupl-1.1) \t\t 18: GNU Affero General Public License v3.0 (agpl-3.0)')
        print('19: GNU General Public License family (gpl) \t\t\t 20: GNU General Public License v2.0 (gpl-2.0)')
        print('21: GNU General Public License v3.0 (gpl-3.0) \t\t\t 22: GNU Lesser General Public License family (lgpl)')
        print('23: GNU Lesser General Public License v2.1 (lgpl-2.1) \t\t 24: GNU Lesser General Public License v3.0 (lgpl-3.0)')
        print('25: ISC (isc) \t\t\t\t\t\t\t 26: LaTeX Project Public License v1.3c (lppl-1.3c)')
        print('27: Microsoft Public License (ms-pl) \t\t\t\t 28: MIT (mit)')
        print('29: Mozilla Public License 2.0 (mpl-2.0) \t\t\t 30: Open Software License 3.0 (osl-3.0)')
        print('31: PostgreSQL License (postgresql) \t\t\t\t 32: SIL Open Font License 1.1 (ofl-1.1)')
        print('33: University of Illinois/NCSA Open Source License (ncsa) \t 34: The Unlicense (unlicense)')
        print('35: zLib License (zlib)')

        print(Fore.GREEN, Style.NORMAL)
        license_no = input(' # license (1-35): ')

        if license_no == '': license_no = 1

        self.readme_data['license'] = self.licenses[int(license_no)-1]
        print()


    def set_important_links(self) -> None:
        print("  # Important Links (Enter if any, else Leave empty to exit): ")
        self.set_data('important_links')
        print()


    def set_readers_note(self) -> None:
        print("  # Reader's Notes (Enter if any, else Leave empty to exit): ")
        self.set_data('readers_note')
        print()


    def set_commands(self) -> None:
        print("  # Commands (Enter if any, else Leave empty to exit): ")
        self.set_data('commands')
        print()


    def set_dependencies(self) -> None:
        os.system('pip3 freeze > temp_req.txt')

        with open ('temp_req.txt', 'r') as f:
            self.readme_data['dependencies'] = f.read().split()

        os.remove('temp_req.txt')


    def set_project_structure(self) -> None:
        '''
        Planned to Create another Section of Project Structure.
        So that developer can see project structure from automated
        Readme.
        '''
        pass


if __name__ == '__main__':
    ReadmeData()