import subprocess
import os
import sys
import pikepdf
import hachoir

def meta():
    choice = input("""
    What is the file type you would like to know about? 
    Enter 'i' for image or 'p' for PDF
    """)
    if(choice =='i' or choice =='I'):
            fname = input('Enter the path of PDF to analyze > ')

            if os.path.exists(fname):
                print('')
            else:
                print('The specified file does NOT exist')

            infoDict = {}
            exeProcess = "hachoir-metadata"
            process = subprocess.Popen([exeProcess,fname], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

            for tag in process.stdout:
                    line = tag.strip().split(':')
                    infoDict[line[0].strip()] = line[-1].strip()

            for k,v in infoDict.items():
                print(k,':', v)
    elif(choice == 'p' or choice == 'P'):
            fname = input('Enter the path of PDF to analyze > ')

            pdf = pikepdf.Pdf.open(fname)
            docinfo = pdf.docinfo
            print("Date is in the format YYYYMMDD+HourMinuteSecond")
            for key, value in docinfo.items():
                print(key, "->", value)
if __name__=="__main__":
   meta()
