# Use functions to create self-portrait 
import sys

def create_self_portrait():
    self_portrait='''
                   11111111
                11111111111111
            1111111        1111111
            11111   _    _   11111
            11111  1_1 -1_1  11111
            11111     '      11111
            11111    1_1     11111
             1111            1111
              111___1    1___111
               11___1    1___11
                1            1
    '''
    print(self_portrait)

# Takes in user input
#  - Allow user to store portrait in a file registered to their name
def store_portrait(name:str, portrait_bytes:bytes):
    print(f"Storing portrait for {name}")


#  - Allow user to view their stored portrait
def view_portrait(name:str):
    print(f"Viewing portrait for {name}")
#  - Allow user to View awesome ASCII portrait of Leah

if __name__ == "__main__":
    # sys.argv is a list of command line arguments
    # sys.argv[0] is the file being run
    # sys.argv[1] is the first argument after the file name (e.g. - `leah` in `py app.py "leah"`)
    file_name = sys.argv[0]
    print(f"Running {file_name} with arguments {sys.argv[1:]}")
    if(len(sys.argv) > 1 and sys.argv[1] == "leah"):
        create_self_portrait()
    if(len(sys.argv) > 2 and sys.argv[1] == "save"):
        # TODO implement photo capture
        name = sys.argv[2]
        store_portrait(name, b"portrait_bytes")

# {} - Squiggly brackets - dictionaries, string formatting
# [] - Square brackets - lists, indexing
# () - Parentheses - tuples, function calls
# '' - Single quotes - string literals
