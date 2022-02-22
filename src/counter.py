import time
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame



class Clock:
    pygame.mixer.init()
    pygame.mixer.music.load('../assets/bell.mp3')

    def __init__(self):
        pass

    def start_time(self):
        self.init_time = time.time()
        return self.init_time

    def stop_time(self):
        self.final_time = time.time()
        return self.final_time

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
