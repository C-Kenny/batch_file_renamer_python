import os, re

def regularFunction(filename):
    """ Removes leading and trailing white space, as well as contents
        between () and [], also removes said brackets """
   
    newName = filename.strip() # removes leading and trailing white space
    newName = re.sub(r"\(*([A-Za-z0-9_]+\))*","", newName)   # ()
    newName = re.sub(r"\[*([A-Za-z0-9_]+\])*","", newName)   # []
    os.rename(filename, newName)

if __name__ == '__main__':
    for filename in os.listdir("."):
        """ For each file in current directory. The RE is split into
            multiple lines for readability, as it's usually <=40 
            characters to process. """
        regularFunction(filename) 
