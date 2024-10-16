from pytube import YouTube


def download_youtube_video(url, download_path=""):
    

    yt = YouTube(url)
        
    
    stream = yt.streams.get_highest_resolution()
        
    
    stream.download(download_path)
    print(f"Downloaded: {yt.title}")
    
Urls = ["https://www.youtube.com/watch?v=g_pkrMjN79M" , "https://www.youtube.com/watch?v=y5UngDqMaXQ"
        , "https://www.youtube.com/watch?v=emqrtL53X0I" , "https://www.youtube.com/watch?v=-2c3ZfAoAfU"
        , "https://www.youtube.com/watch?v=1i4piFhpnm8&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=94"]

for i , url in enumerate(Urls , start = 1):
    download_Path = f"D:\PYTHON\Downloaded Videos\Video {i}"
    download_youtube_video(url , download_Path)
    print ("Video Downloaded : ", download_Path)