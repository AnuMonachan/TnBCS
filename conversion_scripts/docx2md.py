import os
import glob
import docx
from docx import Document
import re

docxFiles = glob.glob(os.getcwd() + "/folder_name/*.docx")
# docxFiles contain all docx files we have to read
# folder_name = language folder where docx is saved
for filenames in docxFiles:
    fileName = filenames.split('/')[-1].split('.')[0]
    # fileName contains folder names which are to created
    os.makedirs(os.getcwd() + '/' + 'folder_name_new' + '/' + fileName)
    # creates folders for each docxFiles according to the fileName data.
    S_filePath = glob.glob(os.getcwd() + '/' + 'folder_name_new' + '/' + fileName)
    # S_filePath is the path where md files are to saved.
    # folder_name_new = new folder to be created.
    document = Document(filenames)
    tables = document.tables
    for table in tables:
        # table is read from docx files
        rows = table.rows
        for row in rows:
            try:
                content = row.cells[0].text
                # content contains first column data
                search_filename = re.search(r'\w+\/.*?\/.*?.md',content)
                # search_filename checks for any name ending with .md in content to create md files with that name
                if search_filename:
                    title_name = search_filename.group(0)
                    split_tname = title_name.split('/')[-1].strip()
                    f = open(S_filePath[0]+'/'+ split_tname,'w+')
                    # f creates md files
                    f.close()
            except:
                pass
            try:
                content1 = row.cells[2].text
                # content1 contains all column 3 data which contains translation data
                search_title = re.search(r'\w+\/.*?\/.*?.md',content1)
                if content1 == "Translation":
                    pass
                elif search_title:
                    pass
                else:
                    f = open(S_filePath[0]+'/'+split_tname,'a')
                    f.write(content1 + '\n')
                    f.close()
                    # writes the text to md files.
            except:
                pass
