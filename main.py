from func import *

opc = 1

while opc > 0 and opc < 3:
    print("Options: ")
    print("1 - Download an Youtube Playlist")
    print("2 - Download an Youtube Video")
    print("3 - Exit")
    opc = int(input())

    if opc == 1:
        downloaderplaylist()
    
    if opc == 2:
        downloadervideo()