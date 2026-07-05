from importlib import import_module
from pathlib import Path
import pkgutil

from fastapi import FastAPI


def register_routers(app: FastAPI):

    package = __name__

    package_path = Path(__file__).parent

    for _, module_name, _ in pkgutil.iter_modules([str(package_path)]):

        module = import_module(f"{package}.{module_name}")

        if hasattr(module, "router"):
            app.include_router(module.router)