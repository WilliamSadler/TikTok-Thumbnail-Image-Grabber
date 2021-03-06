from tkinter import *
from tkinter import filedialog
import json
import os

def grabFrame(video_path, frame):
    """Function that grabs an image of a video at a specific frame and returns the path of the generated image.

    Parameters
    ----------
    video_path : str,
        The path to the video from which the frame will be grabbed

    frame : int,
        The frame of the video that will be converted to an image"""

    print("Grabbing video frame")

def generateFolders(path):
    """Generates folders in the thumbnail source folder path if they don't exit"""
    folders = ["left", "center", "right"]

    for folder in folders:
        if (os.path.exists(path + "/" + folder) == False):
            os.mkdir(path + "/" + folder)


if __name__ == "__main__":
    root = Tk()
    root.withdraw()

    config_path = filedialog.askopenfilename(initialdir = "D:\YouTube\TikToks\CHANNEL CONFIG FILES", 
        title="Select Channel Config File",
        filetypes = (("json files","*.json"),("all files","*.*")))

    channel_config = json.load(open(config_path))
    thumbnail_source_path = channel_config["thumbnails"]["source_folder"]

    generateFolders(thumbnail_source_path)