import time

f = open('./pid_file','r')
f.seek(0)
top_queue = f.readline()
print(top_queue)
while True:
    time.sleep(0.5)
    f.seek(0)
    top_queue = f.readline()
    print(top_queue)
