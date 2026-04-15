import pkgutil
import importlib
from pathlib import Path 

folder_path = Path(__file__).parent 

for a,module_name,b in pkgutil.iter_modules([str(folder_path)]):
    importlib.import_module(f".{module_name}",package=__name__)