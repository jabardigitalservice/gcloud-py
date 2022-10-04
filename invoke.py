import subprocess
import sys

instace = ""
project = ""
zone = ""
cpu = "--cpu="+sys.argv[1]
memory = "--memory="+sys.argv[2]+"MiB"

process = subprocess.Popen(["sh", "./script.sh", instace, project, zone, cpu, memory], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result = process.communicate()
print(result)


# 0 6 * * 1-5 /usr/local/bin/python3 ~/Documents/Python/invoke.py 8 7424 >> ~/Documents/Python/cron.txt 2>&1
# 0 18 * * 1-5 /usr/local/bin/python3 ~/Documents/Python/invoke.py 2 3840 >> ~/Documents/Python/cron.txt 2>&1

# 0 6 * * 1-5 “At 06:00 on every day-of-week from Monday through Friday.”
# 0 18 * * 1-5 “At 18:00 on every day-of-week from Monday through Friday.”