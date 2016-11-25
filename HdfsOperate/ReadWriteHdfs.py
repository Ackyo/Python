from subprocess import Popen, PIPE, STDOUT
from utility import execute_shell_cmd

# Read From Hdfs
cat = Popen(["hadoop", "fs", "-cat", "/mengju/test/read.txt"],
            stdout=PIPE)

for line in cat.stdout:
    print line

cat.stdout.close()
cat.wait()

# Write To Hdfs
execute_shell_cmd('hadoop fs -rm /mengju/test/write.txt')

put = Popen(["hadoop", "fs", "-put", "-", "/mengju/test/write.txt"],
            stdin=PIPE)
put.stdin.write("put data into hdfs test, success!\n")
put.stdin.close()
put.wait()

