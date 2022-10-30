## Mass GDrive Downloader From CSV or CLI

This project solves the problem of downloading multiple files from Google Drive.

### Limitations:

Only can download small files (which dont need to be scanned by Google Drive)

It can download only one type of file. (eg. only pdf, only png ...)

## Prerequisites

1. Python
2. Pip

## Setting Up:

1. Clone the project

2. Go into the project
```
cd gdrive-mass-downloader
```
3. Install all packages
```
pip install -r ./requirements.txt
```
Now clear any contents which of the `files` folder if there are any contents from the previous run of the project

Now the project is ready to be used

## Usage

Run
```
make
```
This will run the python script. By default it will try to run in `python3` but if you are using any other version run `python main.py`

First thing which will be asked is the extension of the files you are about to download.

You can only download files of any one type of extension.

So for example if you are about to download pdf files then type `pdf` and press `Enter`.

## Types of Input [IMPORTANT]

There are 2 types of input which the script accepts.

### 1. CSV Upload

Just place a CSV file at the root of the project directory with these 2 headers `Name` and `Link`. Note that this is case sensitive.

The script will automatically detect the `csv` and start to download the Link column and give it the `Name` given to it.

**Note :**
There should be at most one CSV file in the project directory

### 1. CLI Input

Suppose you have a Google Sheet with the name of the files and links. So just copy those two columns and paste in the CLI.

The CLI mode will be automatically triggered if the scripts doesn't find a CSV file.

**Note:**
The input should be in this format
```
<FILENAME> <LINK>
```
When you type `0` and press `Enter`, the CLI will stop accepting input and start processing

An example of the input is
```
File1 https://googledrivelink1
File2 https://googledrivelink2
0
```
If you copy from Google Sheets the 2 columns in the correct order, it will automatically paste in this format itself.

** Where are the files.

The downloaded files will be in the `files` folder.
