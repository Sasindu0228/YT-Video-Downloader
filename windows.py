import time
import sys
from pytube import YouTube
import threading
import os

def loading_animation(done):
    def animate():
        while not done[0]:
            sys.stdout.write('\rDownloading |')
            time.sleep(0.1)
            sys.stdout.write('\rDownloading /')
            time.sleep(0.1)
            sys.stdout.write('\rDownloading -')
            time.sleep(0.1)
            sys.stdout.write('\rDownloading \\')
            time.sleep(0.1)
        sys.stdout.write('\r')

    t = threading.Thread(target=animate)
    t.start()
    t.join()

def down():
    try:
        done = [False]  # Use a list to hold the done flag for thread safety
        link = input("Enter You Need Video URL : ")

        data = YouTube(link)
        video = data.streams.all()
        vid = list(enumerate(video))

        for i in vid:
            print(i)
        print("")

        cho = int(input("Enter No : "))
        print("")

        # Start the loading animation in a separate thread
        loading_thread = threading.Thread(target=loading_animation, args=(done,))
        loading_thread.start()

        video[cho].download()
        done[0] = True  # Stop the loading animation
        loading_thread.join()  # Wait for the loading animation thread to finish
        print("Successfully downloaded!")
    except:
        print("Check Your Connection!")

def main():
    print("")
    print("██╗   ██╗████████╗      ██████╗  █████╗  ██╗       ██╗███╗  ██╗██╗      █████╗  █████╗ ██████╗ ███████╗██████╗ ")
    print("╚██╗ ██╔╝╚══██╔══╝      ██╔  ██╗██╔══██╗ ██║  ██╗  ██║████╗ ██║██║     ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
    print(" ╚████╔╝    ██║   █████╗██║  ██║██║  ██║ ╚██╗████╗██╔╝██╔██╗██║██║     ██║  ██║███████║██║  ██║█████╗  ██████╔╝")
    print("  ╚██╔╝     ██║   ╚════╝██║  ██║██║  ██║  ████╔═████║ ██║╚████║██║     ██║  ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗")
    print("   ██║      ██║         ██████╔╝╚█████╔╝  ╚██╔╝ ╚██╔╝ ██║ ╚███║███████╗╚█████╔╝██║  ██║██████╔╝███████╗██║  ██║")
    print("   ╚═╝      ╚═╝         ╚═════╝  ╚════╝    ╚═╝   ╚═╝  ╚═╝  ╚══╝╚══════╝ ╚════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝")
    print("                                     Developer Sasindu Rashmika")
    bar = "\n_______________________________________________________________\n"
    print(bar)
    print("[1] START                    [2] Video Details")
    print("[3] Update Tool              [4] Help Video")
    print("[5] Exit  ")
    print("")
    ch = int(input("[*] Enter Your Choice : >>> "))
    print("")
    if ch == 1:
        down()
    elif ch == 2:
        pass
    elif ch == 3:
        pass
    elif ch == 4:
        pass
    elif ch == 5:
        pass
    else:
        print("Invalid Number!")

os.system('cls')
main()