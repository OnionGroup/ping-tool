import subprocess
import os

# A class to schedule a daily task over Windows' Task Scheduler
class SchedulerTask:

    SCHTASKS = "schtasks"

    def __init__(self, task_name, run_exe, run_arguments):
        self.task_name = task_name
        self.run_exe = run_exe
        self.run_arguments = run_arguments

    def schedule_at(self, start_time, frequency):
        args = [self.SCHTASKS, "/Create",
              "/TN", self.task_name, # Task name
              "/SC", frequency, # Schedule frequency
              "/ST", start_time, # Start time
              "/TR", self.run_exe + " " + self.run_arguments, # Program to run
              "/F"] # Overwrite existing task if needed

        with open(os.devnull, 'w') as devnull:
            p = subprocess.Popen(args, stdout=devnull, stderr=subprocess.PIPE)
            p.wait()

        if p.returncode != 0:
            stderr_string = p.stderr.read()
            err_string = "Error scheduling task! stderr={}".format(stderr_string)
            raise RuntimeError(err_string)