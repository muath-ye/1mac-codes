import os
def renameFiles():
   fileList = os.listdir(r"D:\alphabet")
   print(fileList)
   savedPath=os.getcwd()
   print(savedPath)
   os.chdir(r"D:\alphabet")
   # time to rename the files
   for fileName in fileList:
      os.rename(fileName,fileName.translate(None,"0123456789"))
renameFiles()