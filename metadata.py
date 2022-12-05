import subprocess
import os

file_path = input('Enter a file path: ')

if os.path.exists(file_path):
    print('')
else:
    print('The specified file does NOT exist')

infoDict = {}
exeProcess = "hachoir-metadata"
process = subprocess.Popen([exeProcess,file_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

for tag in process.stdout:
        line = tag.strip().split(':')
        infoDict[line[0].strip()] = line[-1].strip()

for k,v in infoDict.items():
    print(k,':', v)
