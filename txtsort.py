unsortedFile = open('textample.txt','r')
sortedFile = open('sortedText.txt','w')
filelist = unsortedFile.read()
filelist = filelist.split()
sortedlist = sorted(filelist,key = str.lower)
sortedFileStr = ' '.join(sortedlist)
sortedFile.write(sortedFileStr)
unsortedFile.close()
sortedFile.close()