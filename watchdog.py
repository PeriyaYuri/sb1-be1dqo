import time
from typing import List
from video_stream import VideoStream

class StreamWatchdog:
    def __init__(self, streams: List[VideoStream], check_interval: int = 5):
        self.streams = streams
        self.check_interval = check_interval
        self.last_check = time.time()
    
    def check_streams(self) -> None:
        """Проверка состояния видеопотоков"""
        current_time = time.time()
        if current_time - self.last_check >= self.check_interval:
            for stream in self.streams:
                if stream.stream is None or not stream.stream.isOpened():
                    print(f"Обнаружен сбой камеры {stream.camera_id}")
                    stream.reconnect()
            self.last_check = current_time