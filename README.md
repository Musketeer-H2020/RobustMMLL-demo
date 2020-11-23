## RobustMMLL-demo for Musketeer Hackathon

This repository consists of code that participants will modify as part of the [hackathon](https://www.eventbrite.com/e/hackathon-shielding-federated-learning-against-attacks-tickets-126189703801).

## Recommended Installation Methods

#### Using `virtualenv`
The developed code within this repositpry is compatible with **python 3.6** and **3.7**. 
We recommend that you check your python version before proceeding to the next steps.

```
python --version
```

The repository can be easily setup using `virtualenv` and `pip`. 
We provide a bash script to help with the installation. 
This script will install the required dependencies and generate the data files of `mnist_hackathon_data.pkl` in the `input_folder`. 

```
./create_env.sh
source venv/bin/activate
```

#### Using `conda`

Alternatively, one can use `conda` with the following commands

```
conda create -n <environment name> python=3.7
conda activate <environment name>
```

Run the following command to install dependencies:
```
pip install -r requirements.txt
python generate_data.py
```

#### Credentials

To use pycloudmessenger it is essential that a credentials file is obtained.
For the purpose of the hackathon, a `hackathon.json` has been made available on the [#musketeer-hackathon](mlhackathonmusketeer.slack.com) slack channel.
 
All concerned scripts for the hackathon are present in the subfolder in `demo/demo_pycloudmessenger/POM1/NeuralNetwork`.
These scripts will require the use of a `user_id` and `password` which is made available offline. 
 
## Adding robust aggregtion schemes

The code stubs for robust aggregation can be added [here](https://github.com/Musketeer-H2020/RobustMMLL-demo/blob/main/demos/demo_pycloudmessenger/POM1/NeuralNetworks/robust.py) with a new string-tag depicting the method. This method can then be called while executing the `aggregator.py` script. 

## FAQs

- What if tensorflow is not installing?

    A: Please check the python version, it must be 3.6 or 3.7. Version tf 1.14 has been found to be incompatible with with python 3.8.

- What if the task already shows existing participants?

    A: It is advised that every time the aggregator is launched, a new `task_name` is chosen. 

- I am getting Error 403/404. What do I do?

    A: Most likely this is due to an incorrect user/password combination.

- The script fails to locate the hackathon.json file. 

    A: Please provide the relative path to the json file rather then just the name itself.

This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 824988. https://musketeer.eu/
