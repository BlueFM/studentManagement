from loguru import logger
import os
import shutil
import schedule
import time
from datetime import datetime

# 配置日志记录
log_directory = "log"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logger.add(f"{log_directory}/app.log", rotation="1 week", retention="4 weeks", compression="zip")

# 定义每周压缩日志的函数
def compress_logs():
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archive_name = f"{log_directory}/logs_{current_time}.zip"
    shutil.make_archive(archive_name.replace('.zip', ''), 'zip', log_directory)
    logger.info(f"Logs compressed into {archive_name}")

# 使用 schedule 每周执行一次压缩
schedule.every().week.do(compress_logs)

# 运行调度器
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1) 