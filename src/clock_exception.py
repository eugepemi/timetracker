class StudyClockError(Exception):
    ERROR_STARTED = '[ERROR] Clock is already running.'
    ERROR_NOT_STARTED = '[ERROR] Clock is already running.'
    ERROR_STOPPED = '[ERROR] Clock is already stopped.'
    ERROR_PAUSED = '[ERROR] Clock is already paused.'
    ERROR_NOT_PAUSED = '[ERROR] Clock is not paused.'
