# RobustMMLL-demo

Demonstrations of the [Robust Musketeer Machine Learning Library (RobustMMLL)](https://github.com/Musketeer-H2020/RobustMMLL) using [Musketeer's pycloudmessenger](https://github.com/IBM/pycloudmessenger/)

## Installation

You may install pycloudmessenger and other library dependencies as follows:

`pip install -r requirements.txt`

Or if you only require pycloudmessenger, then:

`pip install  https://github.com/IBM/pycloudmessenger/archive/v0.4.0.tar.gz`

The pycloudmessenger package requires a credentials file to access the cloud service. Please, place the `musketeer.json` credentials at the `demos/demo_pycloudmessenger/`folder.

## Content (available demos):

### POM1:

* **NeuralNetworks**: Multiclass Classification demo on the MNIST dataset


The output files are stored in the corresponding `results/` folder.

## Usage

You need to install the [RobustMMLL library](https://github.com/Musketeer-H2020/RobustMMLL):

`pip install git+https://github.com/Musketeer-H2020/RobustMMLL.git`

Please visit every subfolder in `demo/demo_pycloudmessenger/` for a detailed explanation about how to run the demos.

If you encounter any difficulties in the installation of some of the dependencies, please refer to the `install` instructions in this repository.

* Requirements Note: if you do not use conda to install and use pip instead, you may need to run `pip install requirements.txt` 

## Input data

The datasets needed to run these demos are located at [IBM Box](https://ibm.box.com/s/l8yzdbdb40j499o513hygx5q85xyoz6v). Please, download and place them in your local `input_data/` folder. 

**IMPORTANT NOTE**: These datasets have been modified with respect to their original versions and are only intended to be used in these demos. Use them for other purposes under your own responsability.


This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 824988. https://musketeer.eu/
