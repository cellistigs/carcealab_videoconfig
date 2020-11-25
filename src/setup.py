import setuptools

setuptools.setup(
        name = "configeditor",
        version = "0.0.1",
        author = "Taiga Abe",
        author_email = "ta2507@columbia.edu",
        description = "Package for editing of carcea lab NeuroCAAS config files.", 
        long_description = "Lightweight package to work with config files designed for NeuroCAAS. Allows users to visualize the bounding boxes specified by a given config file on a given video, and edit these bounding boxes with simple interactivity.",
        long_description_content_type = "test/markdown", 
        url = "https://github.com/cellistigs/carcealab_videoconfig",
        packages = setuptools.find_packages(),
        classifiers = [
            "License :: OSI Approved :: MIT License"],
        python_requires=">3.6",
        )


