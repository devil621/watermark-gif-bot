from settings import X_OFF, Y_OFF
import os
# import ffmpeg


def watermark(video_file: str):
    outf = f'watered_{video_file}'
    command = f'ffmpeg -i {video_file} -i image.png -an -r 5 -preset ultrafast  -tune zerolatency  -tune fastdecode -filter_complex "overlay={X_OFF}:{Y_OFF}" {outf}'
    print(command)
    os.system(command)
    return outf

# def watermark(video_file:str):
#     stream = ffmpeg.input(video_file)
#     ffmpeg.overlay()
