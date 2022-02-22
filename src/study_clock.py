import time
import os
from clock_exception import StudyClockError

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


class StudyClock:
    pygame.mixer.init()
    pygame.mixer.music.load('../assets/bell.mp3')

    def __init__(self):
        self.start_time = None
        self.paused_time = None
        self.stop_time = None
        self.elapsed_time = None
        self.paused = False

    def start(self):
        if self.start_time is not None:
            raise StudyClockError.ERROR_STARTED
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            raise StudyClockError.ERROR_STOPPED
        self.stop_time = time.time()
        self.elapsed_time = self.stop_time - self.start_time

    def pause(self):
        if self.start_time is None:
            raise StudyClockError.ERROR_NOT_STARTED
        if self.paused:
            raise StudyClockError.ERROR_PAUSED
        self.paused_time = time.time()
        self.paused = True

    def resume(self):
        if self.start_time is None:
            raise StudyClockError.ERROR_NOT_STARTED
        if not self.paused:
            raise StudyClockError.ERROR_NOT_PAUSED
        pause_time = time.time() - self.paused_time
        self.start_time = self.start_time + pause_time
        self.paused = False

    def get_time(self):
        return self.elapsed_time

    def pomodoro(self, study_time, rest_time, iterations):
        self.start()
        print(f'Starting Pomodoro, {study_time} min.')
        pygame.mixer.music.play()
        for i in range(iterations):
            time.sleep(study_time * 60)
            pygame.mixer.music.play()
            print(f'Resting, {rest_time} min.')
            time.sleep(rest_time * 60)
            pygame.mixer.music.play()
            print(f'Starting study cycle {i + 2}, {iterations - 1 - i} cycles remaining.')
        print(f'Study completed!')


def main():
    my_clock = StudyClock()
    my_clock.pomodoro(0.5, 0.125, 2)


if __name__ == '__main__':
    main()
