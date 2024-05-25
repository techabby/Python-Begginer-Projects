from pytube import YouTube

url = input("Enter the url of the video: ")
file_name = input("Enter the name of file: ")

yt = YouTube(url)

stream = yt.streams.first()


if stream.download(filename=file_name):
    print("\nVideo Downloaded Successfuly!")
else:
    print("An Error Occured!")
