from PIL import Image, ImageSequence
from moviepy.editor import *
from utils import files


def mp4_to_gif(mp4_file: str) -> str:
    ''' Convert an mp4 to gif

    Args:
        mp4_file (str): path of mp4 file

    Returns:
        str: path of gif file
    '''

    clip = VideoFileClip(mp4_file, audio=False,)
    outfile = files(f'{mp4_file}.gif')
    clip.write_gif(outfile, program='ffmpeg')
    return outfile


def watermark_gif(bg: str, fg: str, xoff: int = 0, yoff: int = 0) -> str:
    ''' Apply watermark on an GIF

    Args:
        bg (str): background gif
        fg (str): the watermark
        xoff (int, optional): x-offset (Defaults to 0)
        yoff (int, optional): y-offset (Defaults to 0)

    Returns:
        str: the name of generated file
    '''

    def addOverlay(frame):
        watermark = Image.open(fg).convert('RGBA')
        frame.convert('RGBA')
        frame.paste(watermark, (xoff, yoff), watermark)
        return frame

    gif = Image.open(bg)
    frames = ImageSequence.all_frames(gif, addOverlay)

    outfile = files(f'{bg}_watermarked.gif')

    frames[0].save(outfile, save_all=True,
                   append_images=frames[1:], quality=60)

    return outfile


def watermark(video_file: str):
    outf = f'watered_{video_file}'
    command = f'ffmpeg -i {video_file} -i image.png -filter_complex "overlay=10:10" {outf}'
    print(command)
    os.system(command)
    return outf
