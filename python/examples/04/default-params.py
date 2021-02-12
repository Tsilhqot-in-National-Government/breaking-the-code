def getPathForFileExport(fileDirectory,fileName,filetype=".wav"):
    filePath = fileDirectory + "/" + fileName + filetype
    return filePath

fileDirectory = "aaronsJams"
fileName = "slowgroove"
mp3Extension = ".mp3"
print("Without specifying file extension: ")
print(getPathForFileExport(fileDirectory,fileName))

print("With specifying mp3 extension: ")
print(getPathForFileExport(fileDirectory,fileName,filetype=mp3Extension))

getPathForFileExport()
# what would happen here?
## getPathForFileExport(fileDirectory=fileDirectory,filetype=mp3Extension)