#para cortar el video
import ffmpeg
import os

print('How many seconds of video do you want: ')
N = int(input())
name = 'BigBuckBunny_512kb.mp4'



def video_cut(seconds,name):

    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    command = 'ffmpeg -i {} -ss 00:00:00 -to {}:{}:{} -c:v copy -c:a copy video_cortado.mp4'.format(name, str(hour),
                                                                                                    str(minutes),
                                                                                                    str(seconds))
    print(command)
    os.system(command)
    print('DONE')


video_cut(N, name)