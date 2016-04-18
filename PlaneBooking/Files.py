import os

class NewDoc:

    def writethis(message):
        
        """
        1. Check if folder is created - otherwise create it
        2. ....
        3. What is BitWise?
        4. Ducktyping??
        """       

        f = open("c:\\pyfolder\newtext.txt", mode="w", encoding="utf-8")
        f.write(message)
        f.close()

    def readthis():
        f = open("c:\newtext", mode="R")
        f.read()