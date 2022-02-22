import time
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


class StudyClockError(Exception):
    """"""


class StudyClock:
    pygame.mixer.init()
    pygame.mixer.music.load('../assets/bell.mp3')

    def __init__(self):
        self.start_time = None
        self.paused_time = None
        self.stop_time = None

    def start(self):
        if self.start_time is not None:
            raise StudyClockError(f'Clock is already running')
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            raise StudyClockError

    def pause(self):
        pass

    def get_time(self):
        return self.final_time - self.init_time

    # Controlar valores de entrada
    def pomodoro(self, study_time, rest_time, iterations):
        self.start_time()
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

    """
    Estructura del json, fecha, hora inicio, hora final, tiempo, materia
    """

    def json_storage(self):
        pass


def main():
    my_clock = Clock()
    my_clock.pomodoro(0.5, 0.125, 2)


if __name__ == '__main__':
    main()
