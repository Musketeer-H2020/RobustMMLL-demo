import subprocess
import os
import signal


NUM_PARTICIPANTS = 5

try:
    flask_server = subprocess.Popen(["python ../../local_flask_server.py"], shell=True)
    print("Started the flask server")

    aggregator = subprocess.Popen(["python aggregator.py"], shell=True)
    print("Started the aggregator")

    participants = []
    for i in range(5):
        participants.append(subprocess.Popen(["python participant.py --id {}".format(i)],
                                  shell=True))
        print("Started participant {}".format(i))

    while True:
        print("Type 'exit' and press 'enter' OR press CTRL+C to quit: ")
        in_str = input().strip().lower()
        if in_str == 'q' or in_str == 'exit':
            print('Shutting down all servers...')
            os.killpg(os.getpgid(flask_server.pid), signal.SIGTERM)
            os.killpg(os.getpgid(aggregator.pid), signal.SIGTERM)
            for i in range(NUM_PARTICIPANTS):
                os.killpg(os.getpgid(participants[i].pid), signal.SIGTERM)
            print('Servers successfully shutdown!')
            break
        else:
            continue

except KeyboardInterrupt:
    print('Shutting down all servers...')
    os.killpg(os.getpgid(flask_server.pid), signal.SIGTERM)
    os.killpg(os.getpgid(aggregator.pid), signal.SIGTERM)
    for i in range(5):
        os.killpg(os.getpgid(participants[i].pid), signal.SIGTERM)
    print('Servers successfully shutdown!')