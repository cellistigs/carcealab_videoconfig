import pytest 
import matplotlib.pyplot as plt
from configeditor.configeditor import ConfigEditor

testvideopath = "/Volumes/TOSHIBA EXT STO/TempTrial2.mpg"
testconfigpath = "/Users/taigaabe/Downloads/TempTrial27config.yaml"

class Test_ConfigEditor():
    def test_ConfigEditor(self):
        ConfigEditor(testvideopath,testconfigpath)
    def test_ConfigEditor_visualize_config(self):
        ce = ConfigEditor(testvideopath,testconfigpath)
        ce.visualize_config()
    def test_ConfigEditor_draw_rectangle(self):
        fig,ax = plt.subplots()
        ce = ConfigEditor(testvideopath,testconfigpath)
        ce.draw_rectangle(ax,(10,10),10,10,1,"red")
        ax.set_xlim(0,20)
        ax.set_ylim(0,20)
        plt.savefig("./test_ConfigEditor_visualize_config.png")


