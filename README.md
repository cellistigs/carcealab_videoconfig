# Config File Editing Tool for Carcea Lab NeuroCAAS Pipeline 

This repo contains a python package (configeditor) and scripts to edit the config files used by the Carcea Lab to set up jobs on their custom NeuroCAAS pipeline. 

## Installation:
To install this tool, you will need a working installation of [Anaconda](https://docs.anaconda.com/anaconda/install/) or [Miniconda](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/) to manage your python environment.  

Once you have an anaconda or miniconda installation, follow these steps: 
#### 1. Clone this repository 

Run the following command in your shell:

`git clone https://github.com/cellistigs/carcealab_videoconfig`

If this step is successful, you should see the following message:

`Unpacking objects: 100% (70/70), done.`

#### 2. Go to the repo that you cloned: 

`cd path-to-your-directory/carcealab_videoconfig`

#### 3. Create a conda environment:

`conda env create -f install/env.yml`

If this step is successful, you should see the following code block: 

```
#                                                                                                                                       
# To activate this environment, use                                                                                                    
#                                                                                                                                       
#     $ conda activate carcealab_videoconfig                                                                                            
#                                                                                                                                      
# To deactivate an active environment, use                                                                                              
#                                                                                                                                       
#     $ conda deactivate
```

#### 4. Activate the conda environment:

`conda activate carcealab_videoconfig`

After successful activation, you should see the expression (carcealab\_videoconfig) to the left of the command prompt.

#### 5. Install this repository:

`pip install src/`

After successful installation, you should see the message `Successfully installed configeditor-0.0.1`. 

#### 6. Incorporating updates:

This repository will periodically be updated with new features or bug fixes. If you want to be safe, please run the following before using again:

First, pull the newest version of the repo by running the following from the top level of the directory:

`git pull`

Additionally, please rerun step 5, (`pip install src/`) once again from the top level directory.

## Using this tool (Script Mode)
In script mode, we will use the shell to call python scripts. We will assume that you have a video accessible at location "videopath", and a config file accessible at location "configpath"- the style of this path will vary depending on your operating system, but be sure to use absolute paths ("/Users/home/..." as opposed to "~/"). Once you have a video and config you want to work with and you know where they are located, move into the scripts directory: 

`cd path-to-your-directory/carcealab_videoconfig/scripts`

Make sure to activate the conda environment if you are coming back to this step from other work:

`conda activate carcealab_videoconfig`

### Check an existing config and video pair
If you are fairly confident about a config and video pair and just want to check the results, run the following command: 

`python check_config.py "videopath" "configpath" "."`

Where "videopath" and "configpath" are the paths to your video and config file. This will save an image (the shell will tell you where) with the box locations outlined in red, and the nest location outlined in blue for each pair of mice indicated in the config file. Note that the last argument (\".\") in the above describes the location where we should save the resulting image. Feel free to change this to suit your needs.  

### Edit a config and video pair
If you would like to edit a config and video pair, run the following command instead from that same directory:  

`python edit_config.py "videopath" "configpath" "."`

Where "videopath" and "configpath" are the paths to your video and config file. This script will create an image as before, but also set up an interactive loop so that you can edit the config and observe the results.You should see this message, with a blank space underneath: 

`Update image? (edit/done)`

 After examining the results in the initial, generated image, open your config file and change some values, and re-save it. After doing so, you can come back to the shell command prompt and type 'edit' (no quotes), and the image will be refreshed. You can repeat this until each of the box locations looks good. Once you're finished, type 'done' in the shell command prompt, and the script will exit.   




