import os
import random
from change_wallpaper import change_wallpaper
from apscheduler.schedulers.background import BackgroundScheduler


class WallpaperChanger:
    def __init__(self, work_dir, output_cb=None):
        self.work_dir = work_dir
        self.flag_disorder = False
        self.index = 0
        self.files = []
        self.flag_run = False
        self.duration = 60
        self._update_files()
        self.scheduler = BackgroundScheduler()
        self.output_cb = output_cb

    def __output_msg(self, msg, color):
        if self.output_cb is not None:
            self.output_cb(msg, color)

    def __create_job(self):
        self.scheduler.add_job(
            self.__run,
            "interval",
            minutes=self.duration
        )
        print("create job, duration:", self.duration)

    def _update_files(self):
        if self.valid() == 0:
            self.files = os.listdir(self.work_dir)
        else:
            self.files = []

    def valid(self):
        if not os.path.exists(self.work_dir):
            return 1
        files = os.listdir(self.work_dir)
        if len(files) == 0:
            return 2
        return 0

    def stop(self):
        self.scheduler.shutdown()
        print("stop")

    def is_running(self):
        return self.scheduler.running

    def previous(self):
        new_index = self.index - 1
        if new_index < 0:
            self.index = len(self.files) - 1
        else:
            self.index = new_index
        file = self.files[self.index]
        self._set_wallpaper(file)
        print(self.index)

    def next(self):
        new_index = self.index + 1
        if new_index >= len(self.files):
            self.index = 0
        else:
            self.index = new_index
        file = self.files[self.index]
        self._set_wallpaper(file)
        print(self.index)

    def disorder(self):
        file = random.choice(self.files)
        self.index = self.files.index(file)
        self._set_wallpaper(file)
        print(self.index)

    def _set_wallpaper(self, file):
        path = os.path.join(self.work_dir, file)
        if os.path.exists(path):
            change_wallpaper(path)

    def set_disorder(self, b_disorder):
        self.flag_disorder = b_disorder
        # self.index = 0

    def set_duration(self, duration):
        self.duration = duration

    def __run(self) -> None:
        print("run triggered")
        if self.flag_disorder is True:
            self.disorder()
        else:
            self.next()

    def run(self):
        self.__create_job()
        self.__run()
        self.scheduler.start()