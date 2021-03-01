import imageio
import os

def convertVideoToGifFile(inputFile):

    outputFile = os.path.splitext(inputFile)[0] + ".gif"

    print("Converting {0} to {1}".format(inputFile, outputFile))

    reader = imageio.get_reader(inputFile)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputFile, fps=fps)

    for i,im in enumerate(reader):
        writer.append_data(im)

    writer.close()

    print("\r\nConversion done.")
    return outputFile

