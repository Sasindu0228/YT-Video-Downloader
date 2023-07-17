from pytube import YouTube

def down():
    link= input("Enter You Need Video URL : ")
    
    data = YouTube(link)

    video = data.streams.all()
    vid=list(enumerate(video))

    for i in vid:
        print(i)
    print("")

    cho=int(input("Enter No : "))
    print("")
    print("Downloading Your Video...")

    video[cho].download()
    print("Successfull")

def main():    
    print("")
    print("\033[1;31m██╗   ██╗████████╗      \033[1;36m██████╗  █████╗  ██╗       ██╗███╗  ██╗")
    print("\033[1;31m╚██╗ ██╔╝╚══██╔══╝      \033[1;36m██╔  ██╗██╔══██╗ ██║  ██╗  ██║████╗ ██║")
    print("\033[1;31m ╚████╔╝    ██║   █████╗\033[1;36m██║  ██║██║  ██║ ╚██╗████╗██╔╝██╔██╗██║")
    print("\033[1;31m  ╚██╔╝     ██║   ╚════╝\033[1;36m██║  ██║██║  ██║  ████╔═████║ ██║╚████║")
    print("\033[1;31m   ██║      ██║         \033[1;36m██████╔╝╚█████╔╝  ╚██╔╝ ╚██╔╝ ██║ ╚███║")
    print("\033[1;31m   ╚═╝      ╚═╝         \033[1;36m╚═════╝  ╚════╝    ╚═╝   ╚═╝  ╚═╝  ╚══╝")
    print("                                                               ")
    bar = "\n__________________________________________________________________________________\n"
    print(bar)
    print("\033[1;33m      [1] START                    [2] Video Details")
    print("\033[1;33m      [3] Update Tool              [4] Help Video")
    print("\033[1;33m      [5] Exit  ")
    print("")
    ch=int(input(      "[*] Enter Your Choice : >>> "))
    print("")
    if (ch==1):
        down()
    elif(ch==2):
        pass
    elif(ch==3):
        pass
    elif(ch==4):
        pass
    elif(ch==5):
        pass
    else:
        print("Invalid Number!")
    

main()

