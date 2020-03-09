import os
import csv
import glob

text = ''
verse_num = ''
chapter = ''
book = ''
os.chdir('/home/anu/test/csvbible')
list_files = sorted(glob.glob('/home/anu/test/' + folder_name + '/*.usfm'))

for files in list_files:
    file = open(files, 'r+', encoding='utf-8-sig')
    reader = file.readlines()
    file_write = open(file_name + '.csv', 'a')
    writer = csv.writer(file_write, delimiter='\t')
    output_list = []
    numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    tverse = ('\\v', '\\q','\\m ','\\f')
    for lines in reader:
        if lines.startswith('\\id '):
            b = lines.split(' ')
            book = b[1].strip('\n')
        if lines.startswith('\\c '):
            ch = lines.split(' ')
            chapter = ch[1].strip('\n')
        if lines.startswith(tverse):
            if lines.startswith('\\v'):
                v = lines.split(' ')
                verse_num = v[1].strip('\n')
                text = ' '.join(v[2:]).strip('\n')
            elif lines.startswith('\\f'):
                ff = lines.split(' ')
                fline = lines.strip('\n')
                if output_list == []:
                    pass
                else:
                    output_list.pop()
                text = text + ' ' + fline + ' '
            elif lines.startswith('\\q'):
                q = lines.split(' ')
                if len(q)==1:
                    continue
                if output_list == []:
                        pass
                else:
                    output_list.pop()
                line = lines.strip('\\q').strip('\n')
                if line.startswith(numbers):
                    text = text + line[1:]
                else:
                    text = text + line
            elif lines.startswith('\\m '):
                if output_list == []:
                    pass
                else:
                    output_list.pop()
                mline = lines.strip('\\m').strip('\n')
                text = text + mline
            output_list.append([book, chapter, verse_num, text.strip()])
        else:
            pass
    for lists in output_list:
      writer.writerow(lists)
    file.close()
    file_write.close()
