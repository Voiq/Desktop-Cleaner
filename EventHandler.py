import shutil
from datetime import date
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from extensions import extensions_to_track

def add_date_to_path(path:Path):
    dated_path = path.with_name(f"{path.stem}_{date.today()}{path.suffix}")
    dated_path.mkdir(parents=True, exist_ok=True)
    return dated_path


def rename_file(source:Path, destination:Path):
    if Path(destination/source.name).exists():
        i=0
        while True:
            i+=1
            new_name = destination/f"{source.stem}_{i}{source.suffix}"
            if not new_name.exists():
                return new_name
    else:
        return destination/source.name



class EventHandler(FileSystemEventHandler):
    def __init__(self,watch_path:Path , destination_root:Path):
        self.watch_path = watch_path.resolve()
        self.destination_root = destination_root.resolve()

    def on_modified(self, event):
        for child in self.watch_path.iterdir():
            if child.is_file() and child.suffix.lower() in extensions_to_track:
                destination = self.destination_root/ extensions_to_track[child.suffix.lower()]
                destination = add_date_to_path(path=destination)
                destination = rename_file(source=child, destination=destination)
                shutil.move(child,destination)    