<img src="./images/tree.png"
     width="150" height="100"
     style="float: left; margin-right: 5px;" />
***

# Machine Learning Algorithms
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/EmanuelFontelles/machineLearning.git/master?urlpath=lab/tree/Index.ipynb)

> This repo is developed by [Emanuel Fontelles](https://github.com/emanuelfontelles).*
> 
> Theses notebooks contained here are machine learning algorithms and some Python libraries useful notebooks as Scikit-Learn [continue...]
> 

## Algorithms:
* Linear Regression

## Installation Notes
This tutorial requires the following packages:

- Python version 2.6-2.7 or 3.3+
- `numpy` version 1.5 or later: http://www.numpy.org/
- `scipy` version 0.10 or later: http://www.scipy.org/
- `matplotlib` version 1.3 or later: http://matplotlib.org/
- `scikit-learn` version 0.14 or later: http://scikit-learn.org
- `ipython` version 2.0 or later, with notebook support: http://ipython.org
- `seaborn` version 0.5 or later

For a local installation, you will need [git], [Python]. If you don't know how to install those on your platform, I recommend to install [Miniconda], a distribution of the [conda] package and environment manager. Please follow the below instructions
to install it and create an environment for the course.

1. Download the Python 3.x installer for Windows, macOS, or Linux from
   <https://conda.io/miniconda.html> and install with default settings. Skip
   this step if you have conda already installed (from [Miniconda] or
   [Anaconda]). Linux users may prefer to use their package manager.
   * Windows: Double-click on the `.exe` file.
   * macOS: Run `bash Miniconda3-latest-MacOSX-x86_64.sh` in your terminal.
   * Linux: Run `bash Miniconda3-latest-Linux-x86_64.sh` in your terminal.
1. Open a terminal. Windows: open the Anaconda Prompt from the Start menu.

Once this is installed, the following command will install all required packages in your Python environment:
```bash 
$ conda install numpy scipy matplotlib scikit-learn ipython-notebook seaborn
```

> *Alternatively, you can download and install the (very large) [Anaconda] software distribution.*

Every time you want to work, do the following:

1. Open a terminal. Windows: open the Anaconda Prompt from the Start menu.
1. Start Jupyter with `jupyter notebook` or `jupyter lab`. The command should
   open a new tab in your web browser.
1. Edit and run the notebooks from your browser.

## Downloading the Tutorial Materials
I would highly recommend using git, not only for this tutorial, but for the
general betterment of your life.  Once git is installed, you can clone the
material in this tutorial by using the git address shown above:

    git clone git://github.com/emanuelfontelles/machinelearning.git

If you can't or don't want to install git, there is a link above to download
the contents of this repository as a zip file.  I may make minor changes to
the repository in the days before the tutorial, however, so cloning the
repository is a much better option.


## Usage and Notebook Listing
You can view the tutorial materials using the excellent service from [Binder]. Click in the Binder bagde [![Binder](https://mybinder.org/badge.svg)][binder_lab] to play with the notebooks from your
browser without installing anything.

> [Binder] lets you easily host interactive Jupyter notebooks and let anyone on the internet use them interactively immediately!

[Binder] creates executable environment making your code immediately reproducible by anyone, anywhere.

## External Repositories

Our `invoke demofiles` clones repos from other authors.  The details of these repos are as follows:

| Name  | Author |License |
|---|---|---|
| PythonDataScienceHandbook/LICENSE-CODE  | Jake Vanderplas  | [MIT](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/LICENSE-CODE)|
| PythonDataScienceHandbook/LICENSE-TEXT   |  Jake Vanderplas | [CC-BY-NC-ND-3.0](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/LICENSE-TEXT) |
| TensorFlow-Examples   |  Aymeric Damien | [MIT](https://github.com/aymericdamien/TensorFlow-Examples/blob/master/LICENSE) |

## Disclaimer
This is a personal repository that is not meant for public use at this time. It is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. No installation or technical support will be provided.

[git]: https://git-scm.com
[python]: https://www.python.org
[scipy]: https://www.scipy.org
[anaconda]: https://www.anaconda.com/download/
[miniconda]: http://conda.pydata.org/miniconda.html
[conda]: https://conda.io
[conda-forge]: https://conda-forge.org
[Binder]: https://mybinder.org/
[binder_lab]: https://mybinder.org/v2/gh/EmanuelFontelles/machineLearning.git/master?urlpath=lab/tree/Index.ipynb