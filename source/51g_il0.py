import importlib
import json
from pathlib import Path

from source.8t2_0iel8 import load_mod_registry


class Ifz524Rl1:
    def __init__(self, core):
        self._core = core
        self._module_name = "source.96ito_4c1x"

    def dispatch_pipeline(self) -> dict:
        ui_module = importlib.import_module(self._module_name)
        ui_tick = ui_module.render_tick(self._core.signature())
        modules = load_mod_registry(self._core.signature())
        state_blob = self._2n3_sct2_4dj()
        return {
            "status": state_blob.get("status", "unknown"),
            "ui_tick": ui_tick,
            "active_modules": modules,
        }

    def _2n3_sct2_4dj(self) -> dict:
        path = Path(__file__).resolve().parent / "zxs_9pmbyc.json"
        if not path.exists():
            return {"status": "bootstrap"}
        with path.open("r", encoding="utf-8") as fp:
            return json.load(fp)
