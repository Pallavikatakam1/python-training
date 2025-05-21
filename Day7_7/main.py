import importlib

def load_and_run(module_name, function_name):
    try:
        module = importlib.import_module(module_name)
        func = getattr(module, function_name)
        func()
    except ModuleNotFoundError:
        print("Module '" + module_name + "' not found.")
    except AttributeError:
        print("Function '" + function_name + "' not found in module '" + module_name + "'")


if __name__ == "__main__":
    mod_name = input("Enter module name: ")
    func_name = input("Enter function to call: ")
    load_and_run(mod_name, func_name)
