import pytube

url = 'https://www.youtube.com/watch?v=ZAfAud_M_mg'

youtube = pytube.YouTube(url)
'''
streams = youtube.streams
for i in streams
    print(i)
'''
v = youtube.streams.get_by_itag()
v.download()
