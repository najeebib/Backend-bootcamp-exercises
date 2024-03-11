import os
from importlib import import_module
# fn loads all sub python files from roads dir

# load file names
operation_files = [f.replace(".py","") for f in os.listdir('roads') if f.endswith('.py') and not f.startswith("__")]

def load_roads():
    roads = {}
    for name in operation_files:
        module = import_module(f"roads.{name}")
        fn = getattr(module,name)
        if callable(fn):
            roads[name] = fn
    return roads

