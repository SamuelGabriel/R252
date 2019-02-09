import subprocess
import sys

# usage: python coda.py <name> <other args>

cmd ="python3 language_model/train.py {} trained_models/ corpus/train corpus/valid".format(' '.join(
    "'{}'".format(e) if e[0]=='{' else e for e in sys.argv[1:]))
subprocess.run(['cl', 'run', ':corpus', ':language_model', cmd, '--request-gpus', '1', '--request-docker-image', 'samgmuller/tf1.12base:0.3', "--name", sys.argv[0]])