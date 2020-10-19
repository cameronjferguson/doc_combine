# doc_combine
Combine all .doc files in a directory. This includes .docx. It combines them into one .docx file with the title 'combined'. Each new doc is separated by a page break. The docs are ordered alpha-numerically.

## Requirements

1. Must have a version of python 3 installed ([Python](https://www.python.org/))
2. Need to install the python-docx module. To do this type the following into your environments terminal
```
pip install python-docx
```
3. Need to have 2 or more .doc files you wish to combine and place them in a single directory together, making sure the order you want them to be combined is alphanumeric (easiest way is to rename each file with a 1, 2, 3... beforehand to ensure the correct order)
4. Make sure none of the original files are called 'combined' as this is the name given to the new combined file. You could edit the code to adjust this if you wish.

## Use instructions

1. Download the doc_combine.py file
2. Move the doc_combine.py file to the directory where the .doc files you want to concatenate are
3. Copy directory path
4. Open the command line and enter
```
cd 'your\copied\path\here'
```
This will navigate to the directory with the doc_combine.py and your .doc files
5. Type the following in cmd to run the code
```
python combine_doc.py
```
This will create a new file in the directory called combined

## Background
I put together this small snippet of code to help out my mum. She is writing a book and has separated each chapter into its own .docx file. However, whenever she wanted to send a part of the book off to a friend or editor she was having to concatenate them all by hand. The method she was using was to create a new file and to open each chapter one by one and copy them across to the new file. I tried to show her a method within Word that would have worked but she kept forgetting how to do it. In the end, I thought it would be easier to just create this little Python snippet to do the job for her. I also turned it into a .exe file and set it in a single directory giving her the instructions to place the chapters she wishes to combine in the folder and run the .exe. At the moment I have decided against uploading the .exe file to this repository as it didn't seem helpful as most PCs will freak out about it being a .exe. Also, it wouldn't allow you to make adjustments if you wanted to add or adjust the code. Finally, if you are tech-savvy enough to be on GitHub looking at this code you'll likely be able to figure out from the instructions above how to use it.
