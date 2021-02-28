from PIL import Image, ImageSequence

def watermark(background:str,foreground:str,xoff:int=0,yoff:int=0):
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
        frame.paste(watermark, (xoff,yoff),watermark)
        return frame

    gif = Image.open(background)
    frames = ImageSequence.all_frames(gif, addOverlay)
    frames[0].save('out.gif', save_all=True, append_images=frames[1:], quality=85)
