# try_prefect.py 
# basics for prefect 
import prefect
from prefect import task, Flow
from datetime import datetime, timedelta
from time import sleep

def timestamper(task, old_state, new_state):
    new_state.timestamp=datetime.utcnow()
    if hasattr(old_state,"timestamp"):
        duration = (new_state.timestamp - old_state.timestamp).seconds
        task.logger.info(f"task took {duration} seconds")
@task(state_handlers=[timestamper],
      max_retries=2,
      retry_delay=timedelta(seconds=60),
      nout=1,
      )
def hello_world():
    print("Hello, World!")
    sleep(1) # 1 seonds
    

@task(state_handlers=[timestamper],
      max_retries=2,
      retry_delay=timedelta(seconds=60),
      nout=1,
      )
def print_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Time: {current_time}")
    sleep(2) # 5 seonds
    print(f"Current Time: {current_time}")
# Define a Prefect Flow
with Flow("My-First-Flow") as flow:
    hw = hello_world()
    pct = print_current_time()

# Run the Prefect Flow
flow.run()
