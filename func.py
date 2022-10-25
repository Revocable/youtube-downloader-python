import os
from pytube import YouTube
from pytube import Playlist

def percentage(n1,n2):
    n1 = n1+1
    return((n1/n2)*100)

def downloaderplaylist():
    playlist = Playlist(input("Insert the url of the playlist you want to download: "))
    path = input("Type the path to the folder where you want to save it. Hit <enter> if it's the same as the program: ")
    opc = int(input("1- Save as MP4 \n2- Save as MP3\n"))
    if opc > 0 and opc < 3:
        
        if opc == 1:
            for videos in playlist:
                yt = YouTube(videos)
                print(f"Downloading: {yt.streams[0].title}")
                ys = yt.streams.get_highest_resolution()
                ys.download(path)
                print(f"Progress:  {str(percentage(playlist.index(videos),len(playlist)))[0:3]}% ")

        else:
            for videos in playlist:
                yt = YouTube(videos)
                print(f"Downloading: {yt.streams[0].title}")
                ys = yt.streams.filter(only_audio=True).first()
                output = ys.download(path)
                name, ext = os.path.splitext(output)
                new_file = name + ".mp3"
                os.rename(output, new_file)
                print(f"Progress:  {str(percentage(playlist.index(videos),len(playlist)))[0:3]}% ")

    else:
        print("Please select an option")


    print(f"Downloading the palylist: {playlist.title}")

    
    print("Download finished!")
        

def downloadervideo():
    video = YouTube(input("Insert the url of the video you want to download: "))
    path = input("Type the path to the folder where you want to save it. Hit <enter> if it's the same as the program: ")
    opc = int(input("1- Save as MP4 \n2- Save as MP3\n"))
    if opc > 0 and opc < 3:
        if opc == 1:
            print(f"Downloading {video.streams[0].title}")
            ys = video.streams.get_highest_resolution()
            ys.download(path)

        else:
            yt = YouTube(video)
            print(f"Downloading: {yt.streams[0].title}")
            ys = yt.streams.filter(only_audio=True).first()
            output = ys.download(path)
            name, ext = os.path.splitext(output)
            new_file = name + ".mp3"
            os.rename(output, new_file)

   
    print("Download finished!")