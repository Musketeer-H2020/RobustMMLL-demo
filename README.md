# RobustMMLL-demo

Demonstrations of the [Robust Musketeer Machine Learning Library (RobustMMLL)](https://github.com/Musketeer-H2020/RobustMMLL) using [Musketeer's pycloudmessenger](https://github.com/IBM/pycloudmessenger/)

## Linux installation

Use one of the following options:

### Installation creating a virtual environment:
```
./create_env.sh
source venv/bin/activate
```

### Installation without virtual environment:

`pip install -r requirements.txt`

Or if you only require pycloudmessenger, then:

`pip install https://github.com/IBM/pycloudmessenger/archive/v0.4.1.tar.gz`


**IMPORTANT NOTE**: The pycloudmessenger package requires a credentials file to access the cloud service. Please, place the `musketeer.json` credentials at the `demos/demo_pycloudmessenger/`folder.

## Content (available demos):

### POM1:

* **NeuralNetworks**: Multiclass Classification demo on the MNIST dataset


The output files are stored in the corresponding `results/` folder.

## Usage

Please visit every subfolder in `demo/demo_pycloudmessenger/` for a detailed explanation about how to run the demos.

## Input data

The datasets needed to run these demos are located at [IBM Box](https://ibm.box.com/s/l8yzdbdb40j499o513hygx5q85xyoz6v). Please, download and place them in your local `input_data/` folder. 

**IMPORTANT NOTE**: These datasets have been modified with respect to their original versions and are only intended to be used in these demos. Use them for other purposes under your own responsability.


This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 824988. https://musketeer.eu/
