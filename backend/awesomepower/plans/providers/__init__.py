import importlib
import pkgutil

# import all provider modules
provider_modules = []
package = importlib.import_module(__name__)

for importer, name, is_pkg in pkgutil.walk_packages(package.__path__):
    module = importlib.import_module(f"{package.__name__}.{name}")
    provider_modules.append(module)
