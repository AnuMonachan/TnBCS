# -*- coding: utf-8 -*-
import re
import os
import glob
import docx
from docx.shared import Cm

# for S_files run from both en_ta-v11 and en-ta-v10
S_files = glob.glob(os.getcwd() + '/' + "en_ta_10/translate")
# links are taken from this S_files
Target_files = glob.glob(os.getcwd() + '/' + "folder_name_new/**/*")
# where links are to be placed.


for files in Target_files:
    f = files.split("/")[-3:]
    n = "/".join(f)
    a = n[7:]
    open_Sfile = S_files[0] + a
    # open_Sfile contains filename and full path of file having links to opened 
    try:
        open_f_S = open(open_Sfile, "r")
        source_content = open_f_S.read()
        findlinks = re.findall(r'(../.*?\.md)', source_content)
        # checks for links.
    except:
        pass
    if findlinks:
        try:
            open_f_T = open(files,"r+")
            # contains files where links are to added from Sfiles
            target_content = open_f_T.read()
            edited_content = target_content
            for links in findlinks:
                edited_content = edited_content.replace("$", links, 1)
                # wherever $ is found it is replaced by links
            open_f_T.seek(0)
            open_f_T.truncate()
            open_f_T.write(edited_content)
            open_f_T.close()
        except:
            pass
