import timer_clippy 
import time
import environ


env = environ.Env()
environ.Env.read_env('config.txt')
tc = timer_clippy.Clippy(env)
stop_time = int(env("STOP_TIME").replace(":", ""))


while True:
    now = time.strftime("%H%M", time.localtime())
    if env("NO_RUN_LIMIT") and int(now) >= stop_time:
        print(f"Time's up!\nSTOP_TIME: {env('STOP_TIME')}")
        time.sleep(3)
        break
    tc.run()
    if tc.close_status:
        print("Exiting.")
        break
    time.sleep(int(env("WAIT_TIME")))