import os, re

if __name__ == '__main__':
    for filename in os.listdir("."):
        """ For each file in current directory. The RE is
            split into two lines for readability, as it's
            usually <40 characters to process. """

        newName = re.sub(r"\(([A-Za-z0-9_]+\))","", filename)    
        newName = re.sub(r"\[([A-Za-z0-9_]+\])","", newName)
        
        
        os.rename(filename, newName)



