from PIL import Image, ImageSequence
from moviepy.editor import *

def watermark(background: str, foreground: str, xoff: int = 0, yoff: int = 0):
    ''' Apply watermark on an GIF

    Args:
        background (str): the GIF image on which the watermark will be applied
        foreground (str): the watermark
        xoff (int, optional): x-offset Defaults to 0
        yoff (int, optional): y-offset Defaults to 0
    '''

    def addOverlay(frame: Image):
        watermark = Image.open(foreground)
        watermark.convert('RGBA')
        frame.paste(watermark, (xoff, yoff), watermark)
        return frame

    gif = Image.open(background)
    frames = ImageSequence.all_frames(gif, addOverlay)
    frames[0].save('out.gif', save_all=True,
                   append_images=frames[1:], quality=85)


def watermark_mp4(video_file:str,watermark_text:str):


    # The video file with audio enabled
    my_clip = VideoFileClip(video_file, audio=True)

    w, h = my_clip.size  # size of the clip

    # A CLIP WITH A TEXT AND A BLACK SEMI-OPAQUE BACKGROUND

    txt = TextClip(watermark_text, font='Amiri-regular',
                   color='red', fontsize=24)

    txt_col = txt.on_color(size=(my_clip.w + txt.w, txt.h-10),
                           color=(0, 0, 0), pos=(6, 'center'), col_opacity=0.6)

    # This example demonstrates a moving text effect where the position is a function of time(t, in seconds).
    # You can fix the position of the text manually, of course. Remember, you can use strings,
    # like 'top', 'left' to specify the position
    txt_mov = txt_col.set_pos(lambda t: (max(w/30, int(w-0.5*w*t)),
                                         max(5*h/6, int(100*t))))

    # Write the file to disk
    final = CompositeVideoClip([my_clip, txt_mov])
    final.duration = my_clip.duration
    out_file = f'OUT_{video_file}'
    final.write_videofile(out_file, fps=24, codec='libx264')
    return out_file
