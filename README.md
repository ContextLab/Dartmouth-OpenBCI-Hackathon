# Dartmouth OpenBCI Hackathon Extravaganza!!

## Hackathon 1: November 21, 2016
Goal: create a visualization of streaming OpenBCI data.

### To get set up, please do the following (ideally prior to 11/21):

1. Ensure that you have write access to the project's
[GitHub repository](https://github.com/ContextLab/Dartmouth-OpenBCI-Hackathon)
1. Join the [Brain Haxorz Slack group](https://brainhaxorz.slack.com/x-99951248852-99951418612/signup)
1. Subscribe to the project's [Trello board](https://trello.com/b/dwfqmMmQ/openbci-hack).  This is used for
   brainstorming and prioritising ideas.
1. Also check out the
   [GitHub project board](https://github.com/ContextLab/Dartmouth-OpenBCI-Hackathon/projects/1).
   This is used to keep track of implementation details and notes.
1. Install [Enthought Canopy](https://store.enthought.com/downloads/#default) or another
   Python 2.x distribution.
1. Run the install stript (sh install.sh).  This will download all
   dependencies and set up your Python path to include the relevant
   toolbox packages.
1. Install [PyCharm CE](https://www.jetbrains.com/pycharm/download/) or
   another Python IDE of your choise.  Set up your environment to use
   Enthought Canopy as your project's Python interpreter.

### Working notes
The project is divided into two primary tasks ([proposed API](http://tinyurl.com/hmolv53)):
1. Write streaming data to a file, using OpenBCI_Python
   ([PROJECT BOARD](https://github.com/ContextLab/Dartmouth-OpenBCI-Hackathon/projects/2);
   [SLACK CHANNEL](https://brainhaxorz.slack.com/archives/data-streaming); branch: *streamdata*)
1. Read streaming data from file and plot it using hyper-plot
   tools. ([PROJECT BOARD](https://github.com/ContextLab/Dartmouth-OpenBCI-Hackathon/projects/3);
   [SLACK CHANNEL](https://brainhaxorz.slack.com/archives/data-visualization); branch: *plotdata*)

If time, we will try to implement a third task:
1. Read a series of samples from the data stream and return a feature
vector comprising spectral freatures at each
electrode. ([PROJECT BOARD](https://github.com/ContextLab/Dartmouth-OpenBCI-Hackathon/projects/4);
[SLACK CHANNEL](https://brainhaxorz.slack.com/archives/data-transformation);
branch: *xformdata*)

Choose your project team (these can be fluid, but you should start
somewhere).  Make sure everyone on your team has checked out the
appropriate branch and is added to the Slack channel.  Decide as a
team how you want to organize yourselves.  For example, you might want
to code in pairs, as a group, separately, or something else.  Divide
your sub-project into a series of sub-tasks.

As you finish a task or get stuck, update the
[main project board](https://github.com/ContextLab/Dartmouth-OpenBCI-Hackathon/projects/1).
Also add any notes and/or usage examples to the [API](http://tinyurl.com/hmolv53).


# Implementation notes

## Modules:

1. [Hyper-plot tools](https://github.com/ContextLab/hyper-tools)
1. [OpenBCI_Python](https://github.com/OpenBCI/OpenBCI_Python)
1. [EEGrunt](https://github.com/curiositry/EEGrunt)

