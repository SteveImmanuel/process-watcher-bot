import psutil
import time
from bot import push_message

pid = input('PID (comma separated): ')
process_alias = input('Process alias (for bot to send, defaults to PID): ') or pid
chat_ids = input('Chat ID (comma separated): ')
sleep_interval = int(input('Sleep interval (5s): ') or 5)

assert pid, 'PID cannot be blank!'
assert chat_ids, 'Chat ID cannot be blank!'

pid = list(map(int, pid.split(',')))
chat_ids = list(map(int, chat_ids.split(',')))

pid_status = [ psutil.pid_exists(x) for x in pid ]
while any(pid_status):
    time.sleep(sleep_interval)
    print('Checking process')
    pid_status = [ psutil.pid_exists(x) for x in pid ]

for id in chat_ids:
    push_message(id, f'{process_alias} has finished executing')