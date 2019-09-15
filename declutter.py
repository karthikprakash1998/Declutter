import sys
import glob
import os.path
import ntpath


def createFolder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


folderPath = sys.argv[1]
allFiles = glob.glob(folderPath+"/*.*")

audioFiles = ['.aif', '.cda', '.mid', '.midi',
              '.mp3', '.mpa', '.ogg', '.wav', '.wma', '.wpl']
compressedFiles = ['.7z', '.arj', '.deb', '.pkg',
                   '.rar', '.rpm', '.tar', '.gz', '.z', '.zip']
mediaFiles = ['.bin', '.dmg', '.iso', '.toast', '.vcd']
dbFiles = ['.csv', '.dat', '.log', '.mdb', '.sav', '.sql', '.tar', '.xml']
executableFiles = ['.apk', '.bat', '.cgi', '.pl',
                   '.com', '.exe', '.gadget', '.jar', '.py', '.wsf']
fontFiles = ['.fnt', '.fon', '.otf', '.ttf']
imageFiles = ['.ai', '.bmp', '.gif', '.ico', '.jpeg',
              '.jpg', '.png', '.ps', '.psd', '.svg', '.tif', '.tiff']
internetFiles = ['.asp', '.aspx', '.cer', '.cfm', '.cgi', '.pl', '.css',
                 '.htm', '.html', '.js', '.jsp', '.part', '.php', '.py', '.rss', '.xhtml']
presentationFiles = ['.key', '.odp', '.pps', '.ppt', '.pptx']
programmingFiles = ['.c', '.class', '.cpp',
                    '.cs', '.h', '.java', '.sh', '.swift', '.vb']
spreadsheetFiles = ['.ods', '.xlr', '.xls', '.xlsx']
systemFiles = ['.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp',
               '.drv', '.icns', '.ico', '.ini', '.lnk', '.msi', '.sys', '.tmp']
videoFiles = ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv',
              '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv']
wordFiles = ['.doc', '.docx', '.odt', '.pdf',
             '.rtf', '.tex', '.txt', '.wks', '.wps', '.wpd']

for file in allFiles:
    
    fileName=ntpath.basename(file)
    extension = os.path.splitext(file)[1]
    
    if extension in audioFiles:
        folder = folderPath+'\Audio Files'
        newFile=folder+"\\"+fileName
        createFolder(folder)
        os.rename(file,newFile)
        
    elif extension in compressedFiles:
        folder = folderPath+'\Compressed Files'
        newFile=folder+"\\"+fileName
        createFolder(folder)
        os.rename(file,newFile)
        
    elif extension in mediaFiles:
        folder = folderPath+'\Media Files'
        newFile=folder+"\\"+fileName
        createFolder(folder)
        os.rename(file,newFile)
        
    elif extension in dbFiles:
        folder = folderPath+'\DB Files'
        newFile=folder+"\\"+fileName
        createFolder(folder)
        os.rename(file,newFile)
        
    elif extension in executableFiles:
        folder = folderPath+'\Executable Files'
        newFile=folder+"\\"+fileName
        createFolder(folder)
        os.rename(file,newFile)
        
    elif extension in fontFiles:
        folder = folderPath+'\Font Files'
        newFile=folder+"\\"+fileName
        createFolder(folder)
        os.rename(file,newFile)
        
    elif extension in imageFiles:
        folder = folderPath+'\Image Files'
        newFile=folder+"\\"+fileName
        createFolder(folder)
        os.rename(file,newFile)
        
    elif extension in internetFiles:
        folder = folderPath+'\Internet Files'
        newFile=folder+"\\"+fileName
        createFolder(folder)
        os.rename(file,newFile)
        
    elif extension in presentationFiles:
        folder = folderPath+'\Presentation Files'
        newFile=folder+"\\"+fileName
        createFolder(folder)
        os.rename(file,newFile)
        
    elif extension in programmingFiles:
        folder = folderPath+'\Programming Files'
        newFile=folder+"\\"+fileName
        createFolder(folder)
        os.rename(file,newFile)
        
    elif extension in spreadsheetFiles:
        folder = folderPath+'\SpreadSheet Files'
        newFile=folder+"\\"+fileName
        createFolder(folder)
        os.rename(file,newFile)
        
    elif extension in systemFiles:
        folder = folderPath+'\System Files'
        newFile=folder+"\\"+fileName
        createFolder(folder)
        os.rename(file,newFile)
        
    elif extension in videoFiles:
        folder = folderPath+'\Video Files'
        newFile=folder+"\\"+fileName
        createFolder(folder)
        os.rename(file,newFile)
        
    elif extension in wordFiles:
        folder = folderPath+'\Word Files'
        newFile=folder+"\\"+fileName
        createFolder(folder)
        os.rename(file,newFile)
        
    else:
        folder = folderPath+'\Other Files'
        newFile=folder+"\\"+fileName
        createFolder(folder)
        os.rename(file,newFile)
