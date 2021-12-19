from tkinter import *
from pytube import YouTube

try:

    def AudioDownload():
        choice2 = youtubeAttributes.streams.get_by_itag(139)
        location1 = locationInput1.get()
        choice2.download(location1)
        downloadSuccessLabel1 = Label(audioDownloadRoot, text="Downloaded Successfully!", fg='green')
        downloadSuccessLabel1.pack()

    def OnAudioDownload():
        onSubmitRoot.destroy()
        global audioDownloadRoot
        audioDownloadRoot = Tk()
        audioDownloadRoot.geometry("600x200")
        locationAskLabel1 = Label(audioDownloadRoot, text="Enter the path of where you'd like to download to:")
        locationAskLabel1.pack()
        global locationInput1
        locationInput1 = Entry(audioDownloadRoot, width=50)
        locationInput1.pack()
        locationInputButton1 = Button(audioDownloadRoot, text="Submit", command=AudioDownload)
        locationInputButton1.pack()


    def ExceptionCaught():
        exceptionRoot = Tk()
        exceptionRoot.geometry('300x100')
        exceptionLabel = Label(exceptionRoot, text="An error occurred. Please rerun the program.")
        exceptionLabel.pack()
        exceptionRoot.mainloop()



    def VideoDownload():
        location = locationInput.get()
        getHighestRes = youtubeAttributes.streams.get_highest_resolution()
        getHighestRes.download(location)
        downloadSuccessLabel = Label(videoDownloadRoot, text="Downloaded Successfully.", fg='green')
        downloadSuccessLabel.pack()


    def OnVideoDownload():
        onSubmitRoot.destroy()
        global videoDownloadRoot
        videoDownloadRoot = Tk()
        videoDownloadRoot.geometry("600x200")
        locationAskLabel = Label(videoDownloadRoot, text="Enter the path of where you'd like to download to:")
        locationAskLabel.pack()
        global locationInput
        locationInput = Entry(videoDownloadRoot, width=50)
        locationInput.pack()
        locationInputButton = Button(videoDownloadRoot, text="Submit", command=VideoDownload)
        locationInputButton.pack()


    def OnSubmit():
        global linkSubmitted
        linkSubmitted = enterLinkInput.get()
        print(len(linkSubmitted))
        if len(linkSubmitted) == 43:
            root.destroy()
            global onSubmitRoot
            onSubmitRoot = Tk()
            onSubmitRoot.geometry("600x200")
            onSubmitRoot.title("Video or Audio?")
            global youtubeAttributes
            youtubeAttributes = YouTube(linkSubmitted)
            title = youtubeAttributes.title
            titleLabel = Label(onSubmitRoot, text=title)
            titleLabel.pack()
            videoDownload = Button(onSubmitRoot, text="Video Download", command=OnVideoDownload)
            videoDownload.pack()
            audioDownload = Button(onSubmitRoot, text="Audio Download", command=OnAudioDownload)
            audioDownload.pack()

        else:
            failLabel = Label(root, text="please enter a YouTube link.", fg='red')
            failLabel.pack()







    def mainWindow():
        global root
        root = Tk()
        root.geometry("400x400")
        root.title("Youtube Downloader")
        linkLabel = Label(root, text="Enter the link of the video you want to download:")
        linkLabel.pack()
        global enterLinkInput
        enterLinkInput = Entry(root, width=45)
        enterLinkInput.pack()
        submitButton = Button(root, text="Submit", command=OnSubmit)
        submitButton.pack()



        root.mainloop()




    mainWindow()

except Exception as x:
    print(x)
    ExceptionCaught()

