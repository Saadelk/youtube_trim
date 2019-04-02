import youtube_dl
from moviepy.editor import *

youtube_folder = './Youtube Downloads/'
trimmed_folder = './Trimmed Downloads/'
if not os.path.exists(youtube_folder):
    os.makedirs(youtube_folder)
    os.makedirs(trimmed_folder)
    


def download(song_url, song_title):
    outtmpl = song_title + '.%(ext)s'
    ydl = youtube_dl.YoutubeDL(
        {
            'outtmpl': outtmpl
        })

    with ydl:
        result = ydl.extract_info(
            song_url,
            download=True  # We just want to extract the info
        )
    return result

#Inputs
Youtube_Link = input("Enter youtube link :")
video_title = input("Enter video title :")
start_time = input("Enter start time in this format hh:min:ss  ")
start_time = sum(int(x) * 60 ** i for i, x in enumerate(reversed(start_time.split(":"))))

end_time = input("Enter end time in this format hh:min:ss")
end_time = sum(int(x) * 60 ** i for i, x in enumerate(reversed(end_time.split(":"))))

#Dowloading original video

download(Youtube_Link, '{0}{1}'.format(youtube_folder, video_title))

#Dowloading trimmed video
video = VideoFileClip('{0}{1}.mp4'.format(youtube_folder, video_title)).subclip(start_time, end_time)
video.write_videofile('{0}{1}.mp4'.format(trimmed_folder, video_title))
