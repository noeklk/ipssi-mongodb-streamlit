from crontab import CronTab



with CronTab(tab="""* * * * * py C:\\Users\\DarkArrow\\Workbench\\ipssi\\python\\mongodb\\api_fetch_migration_exec.py""") as cron:
    job = cron.new()
    job.minute.every(1)

    cron.write("test.txt")