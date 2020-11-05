from flpy_bank.processor import RecordProcessor
from flpy_bank.processor.tagging import TagProcessor

PROCESSOR_REGISTRY = {
    'tag': TagProcessor
}


def construct_processor_from_name(name: str) -> RecordProcessor:
    return PROCESSOR_REGISTRY[name]()
