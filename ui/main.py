from scheduling.scheduler_task import SchedulerTask

my_scheduler = SchedulerTask("my-task", "C:\msgbox.vbs", '"your scheduler is working idiot.. now get rid of this annoying message"')
my_scheduler.schedule_at("15:33", "daily")