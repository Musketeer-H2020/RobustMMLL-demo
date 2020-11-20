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

`pip install https://github.com/IBM/pycloudmessenger/archive/v0.6.0.tar.gz`


**IMPORTANT NOTE**: The pycloudmessenger package requires a credentials file to access the cloud service. Please, place the `hackathon.json` credentials at the `demos/demo_pycloudmessenger/`folder.

## Content (available demos):

### POM1:

* **NeuralNetworks**: Multiclass Classification demo on the MNIST dataset

The output files are stored in the corresponding `results/` folder.

## Usage

Please visit every subfolder in `demo/demo_pycloudmessenger/` for a detailed explanation about how to run the demos.

## Adding robust aggregtion schemes

The code stubs for robust aggregation can be added [here](https://github.com/Musketeer-H2020/RobustMMLL-demo/blob/main/demos/demo_pycloudmessenger/POM1/NeuralNetworks/robust.py) with a new string-tag depicting the method. This method can then be called while executing the `aggregator.py` script.

This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 824988. https://musketeer.eu/
