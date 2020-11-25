import os
import datetime
import yaml
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from .paths import repo_path
from moviepy.editor import VideoFileClip

class ConfigEditor():
    """Object class to hold configuration data. Assumes a video that we want to analyze, and can be initalized from a file. Will assume yaml format. 
    """
    def __init__(self,videopath,configpath,savepath = "./"):
        """Initialize objects with the paths: videopath, configpath. 

        """
        ## First clean the videopath:
        assert os.path.exists(videopath),"No file can be found at location {}".format(videopath)
        try:
            self.clip = VideoFileClip(videopath)
        except Exception:
            print("This file could not be loaded as a video.")
            raise
        self.videopath = videopath
        self.videoname = os.path.basename(videopath)

        ## Now clean the yaml path:
        assert os.path.exists(configpath),"No file can be found at location {}".format(configpath)
        try:
            with open(configpath) as f:
                config = yaml.full_load(f)
                self.config = config 
        except Exception:
            print("This file could not be loaded as a config file.")
            raise
        self.configpath = configpath
        self.configname = os.path.basename(configpath)

        ## Get some parameters for easy access: 
        self.nb_boxes = len(self.config["coordinates"])
        self.nb_nests = len(self.config["nests"])
        assert self.nb_boxes >= self.nb_nests,"Must specify a box for each nest."

        assert os.path.isdir(savepath),"This location is not a directory where images can be saved."
        self.savepath = savepath

        


    def initialize_subplot_fig(self):
        """Creates a figure and axes for each of the boxes specified in the config file. 

        :return: returns a fig,ax pair initialized for each specified box. 
        """
        fig,ax = plt.subplots(self.nb_boxes,1,figsize = (10,10))
        for bi,box in enumerate(self.config["coordinates"]):
            ax[bi].set_title(box)
        return fig,ax

    def reload_config(self):
        """Reloads the config file into memory in case edits have been made. 

        """
        assert os.path.exists(self.configpath),"No file can be found at location {}".format(self.configpath)
        try:
            with open(self.configpath) as f:
                config = yaml.full_load(f)
                self.config = config 
        except Exception:
            print("This file could not be loaded as a config file.")
            raise

    def draw_rectangle(self,ax,xy,width,height,linewidth,color):
        """Draws a rectangle on provided axis. 

        :param ax: the axes on which to plot. 
        :param xy: the xy location of the lower left hand corner. 
        :param width: the width in x space.
        :param height: the height in y space.
        :param linewidth: the width of the lines. 
        :param color: the color to plot. 
        """
        rect = patches.Rectangle(xy,width,height,linewidth=linewidth,edgecolor = color,fill = False) 
        ax.add_patch(rect)

    def parse_coordinates(self):
        """Takes in the coordinates in the config file and converts them to matplotlib friendly form. 

        """
        coords = self.config["coordinates"]
        boxrects = {}
        for box,coord in coords.items():
            xy = (coord["x0"],coord["y0"])
            width = coord["x1"] - coord["x0"]
            height = coord["y1"] - coord["y0"]
            boxrect = {"xy":xy,"width":width,"height":height}
            boxrects[box] = boxrect
        return boxrects

    def parse_nests(self):
        """Takes in the nests in the config file and converts them to matplotlib friendly form. 

        """
        nests = self.config["nests"]
        boxrects = {}
        for box,nest in nests.items():
            xy = (nest["xn0"],nest["yn0"])
            width = nest["xn1"] - nest["xn0"]
            height = nest["yn1"] - nest["yn0"]
            boxrect = {"xy":xy,"width":width,"height":height}
            boxrects[box] = boxrect
        return boxrects

    ## Visualize functions

    def visualize_config(self,frame = 0,name = None):
        """Takes a frame from the given clip, and then plots the boxes and nests given by the config file. 

        :param frame: a floating point value giving the time point which we want to visualize in seconds.  
        """
        self.reload_config()
        image = self.clip.get_frame(frame) 
        ## Initialize subplots:  
        fig,ax = self.initialize_subplot_fig()
        for axi in ax:
            axi.imshow(image)

        coords = self.parse_coordinates()
        for cind,(c,cinfo) in enumerate(coords.items()):
            self.draw_rectangle(ax[cind],cinfo["xy"],cinfo["width"],cinfo["height"],1,"red")
        nests = self.parse_nests()
        for nind,(n,ninfo) in enumerate(nests.items()):
            self.draw_rectangle(ax[nind],ninfo["xy"],ninfo["width"],ninfo["height"],1,"blue")

        imagename = "visualize_config_{}_{}.png".format(self.videoname,self.configname)
        imagepath = os.path.join(self.savepath,imagename)
        plt.savefig(imagepath)
        plt.close()
        print("image saved at {}".format(imagepath))

        

        






