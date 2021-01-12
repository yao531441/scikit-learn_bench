import signal
import subprocess
import os

if __name__ == "__main__":
    cmd_str = 'python --version'
    cmd_str = 'python /tmp/gitspace/scikit-learn_bench/runner.py  --configs /tmp/gitspace/scikit-learn_bench/configs/skl_config.json'
    # print(os.popen(cmd_str).read())
    p = subprocess.Popen(cmd_str, shell=True)
    try:
        p.communicate()
    except KeyboardInterrupt:
        os.killpg(os.getpgid(p.pid), signal.SIGKILL)
