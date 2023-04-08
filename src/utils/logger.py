import inspect
import logging


class MyLogger:
    def __init__(self):
        self.logger = logging.getLogger(self._get_caller_filename())
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def _get_caller_filename(self):
        # Get the filename of the calling module
        caller_frame = inspect.stack()[2]
        caller_filename = caller_frame.filename
        return caller_filename
