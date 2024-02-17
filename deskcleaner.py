from pathlib import Path
from time import sleep
from watchdog.observers import Observer
from EventHandler import EventHandler



if __name__ == "__main__":
    folder_to_track = "C:/Users/Ahmed Yasser/Downloads"
    folder_destination = "E:/Memez"
    watch_path = Path(folder_to_track)
    destination_root = Path(folder_destination)
    event_handler = EventHandler(watch_path=watch_path, destination_root=destination_root)
    observer = Observer()
    observer.schedule(event_handler, watch_path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(40)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()








