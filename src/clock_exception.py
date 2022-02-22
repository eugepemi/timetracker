class StudyClockError(Exception):
    ERROR_START_CLOCK = '[ERROR] Clock is already running.'
    ERROR_STOP_CLOCK = '[ERROR] Clock is already stopped.'
    ERROR_PAUSE_CLOCK = '[ERROR] Clock is already paused.'
