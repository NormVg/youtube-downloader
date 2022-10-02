import scrapetube , os 
from pytube import YouTube
from termcolor import cprint

cprint("<-SEARCH-THE-VIDEO->","red")
i = input("#: ")
videos = scrapetube.get_search(i)

for video in videos:
    title = video['title']['runs'][0]['text']
    cprint(title,"red")
    cprint("<-CHEAK-THE-TITLE-FOR-THE-CORRECT-VIDEO-TO-DOWNLOAD-<y/n>-->","red")
    inp = input("#: ")
    if "y" in inp:
        id = video['videoId']
        yt = YouTube("https://youtube.com/watch?v="+str(id))
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download()
        
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        cprint(yt.title + " <-has-been-successfully-downloaded->".upper(),"red")
        break
    
    

    
    