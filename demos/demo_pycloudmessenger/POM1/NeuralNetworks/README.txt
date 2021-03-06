==================================================================
 Demo execution instructions using pycloudmessenger under Linux OS
==================================================================

Open three bash terminals and execute any of the following scripts to see the corresponding demo.

Every terminal represents one participant, they can be in different machines.

-------------------------------------------
Execute these lines, one at every terminal. Start launching the master, and wait until it is ready to receive workers before launching the workers.

Once the training is completed, these demo scripts produce the output files in the results/ folder (models, figures, logs)
-------------------------------------------

Parameters:
    - user: String with the name of the user. If the user does not exist in the pycloudmessenger platform a new one will be created.
    - password: String with the password.
    - task_name: String with the name of the task. If the task already exists, an error will be displayed.
    - id: Integer representing the partition of data to be used by the worker. Each worker should use a different partition, possible values are 0 to 4.

Important notes:
    - The task_name should be the same for all terminals. Each time we launch a new demo a new name has to be given to the task.
    - Each user should have a different id, otherwise they will be training using the same dataset partition.
    - The architecture of the Keras model to use is defined inside this folder. If you want to try a different architecture use the script model_definition_keras.py and define a new architecture using the sequential or functional API provided by Keras. This new filename should be updated at the beginning of aggregator.py in order for the changes to take place.
-------------------------------------------


==================================================================
 Robust aggregation with model averaging without normalization
==================================================================
python aggregator.py --user <user> --password <password> --task_name <task_name> --credentials <filename> --iterations 5 --workers 2 --robustmethod average
python participant.py --user <user> --password <password> --task_name <task_name> --id 0 --credentials <filename>
python participant.py --user <user> --password <password> --task_name <task_name> --id 1 --credentials <filename>
