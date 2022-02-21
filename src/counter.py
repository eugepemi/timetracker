import time


# Buscar lib para reproducir sonidos


class Clock:
    init_time = 0
    final_time = 0

    # Falta static variable con el mp3 de ../assets/

    def __init__(self):
        pass

    def start_time(self):
        self.init_time = time.time()
        return time.time()

    def stop_time(self):
        self.final_time = time.time()
        return self.final_time

    def get_time(self):
        return self.final_time - self.init_time

    # Controlar valores de entrada
    def pomodoro(self, study_time, rest_time, iterations):
        self.start_time()
        print(f'Starting Pomodoro, {study_time} min.')
        # Falta sonido campana
        for i in range(iterations):
            time.sleep(study_time * 60)
            print(f'Resting, {rest_time} min.')
            time.sleep(rest_time * 60)
            print(f'Starting study cycle {i + 2}, {iterations - 1 - i} cycles remaining.')
        print(f'Study completed!')


def main():
    my_clock = Clock()
    my_clock.pomodoro(0.5, 0.125, 2)


if __name__ == '__main__':
    main()
