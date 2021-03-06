from settings import X_OFF, Y_OFF
import os


def watermark(video_file: str):
    outf = f'watered_{video_file}'
    command = f'ffmpeg -i {video_file} -i image.png -an -dn -sn -r 10 -preset ultrafast  -tune zerolatency  -tune fastdecode -filter_complex "overlay={X_OFF}:{Y_OFF}" {outf}'
    print(command)
    os.system(command)
    return outf

