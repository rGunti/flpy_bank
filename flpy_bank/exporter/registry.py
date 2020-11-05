from flpy_bank.exporter import DataExporter
from flpy_bank.exporter.json import JsonExporter
from flpy_bank.exporter.yaml import YamlExporter

EXPORTER_REGISTRY = {
    'json': JsonExporter,
    'yaml': YamlExporter
}


def construct_exporter_from_name(name: str, path: str) -> DataExporter:
    return EXPORTER_REGISTRY[name](path)
