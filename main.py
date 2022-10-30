import pandas as pd
import os
import sys
import gdown

# get all the files in a specific directory
def getFiles(directory):
    files = [f for f in os.listdir(directory)]
    return files


def checkFile(extension,fileArray):
    files = []
    for f in fileArray:
        if(f.endswith(extension)):
            files.append(f);
    return files;

def print_progress_bar(index, total, label):
    n_bar = 50  # Progress bar width
    progress = index / total
    sys.stdout.write('\r')
    sys.stdout.write(f"[{'=' * int(n_bar * progress):{n_bar}s}] {int(100 * progress)}%  {label}")
    sys.stdout.flush()

files = getFiles(".")
fileCSV = checkFile("csv",files)
requiredFiles = []

print("Enter the file extension you are trying to downlaod (eg csv, pdf, png etc)\nYou can only download only one format")
fileExtension = input()

if(len(fileCSV) == 0) :
    print("No csv found  :(")
    print("Enter in this format\n<NAME_OF_THE_FILE> <URL>\nType 0 and press enter to stop the extraction\n")
    while(1):
        userInput = input()
        if(userInput == "0"):
            break
        requiredFiles.append(userInput.split("\t"))

else :
    resumeCSV = fileCSV[0]
    print("Found : " + resumeCSV + "\n")
    print("Extracting csv ....\n")
    CSVReader = pd.read_csv(resumeCSV)
    for row in CSVReader.Name:
        requiredFiles.append([row])
    for index,row in enumerate(CSVReader.Link):
        requiredFiles[index].append(row)

if len(requiredFiles) == 0: 
    print("Please ensure that you have followed the instructions.\nProgram terminated as it cant find anything to download");
    exit();

for i,row in enumerate(requiredFiles):
    fileId = row[1].split("id=")[1].split("/")[0];
    fileName = "./files/" + row[0] + "." + fileExtension;
    gdown.download(row[1], fileName, quiet=False, fuzzy=True)
    print_progress_bar(i+1,len(requiredFiles),"Downloaded "+str(i+1)+ "/" + str(len(requiredFiles)) + "\n\n") 


