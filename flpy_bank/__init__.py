from typing import List

from flpy_bank.exporter.registry import construct_exporter_from_name
from flpy_bank.parser.registry import construct_parser_from_name
from flpy_bank.processor.registry import construct_processor_from_name


def run(input_file: str,
        parser_name: str,
        processor_names: List[str],
        exporter_name: str,
        export_path: str):
    print('Parsing input file {} using {} ...'.format(input_file, parser_name))
    parser = construct_parser_from_name(parser_name)
    records = parser.parse_file(input_file)

    print('Processing {} records using {} processors ...'.format(len(records), len(processor_names)))
    for processor_name in processor_names:
        print(' - Processing with {} ...'.format(processor_name))
        processor = construct_processor_from_name(processor_name)
        processor.process(records)

    print('Exporting to {} using {} ...'.format(export_path, exporter_name))
    exporter = construct_exporter_from_name(exporter_name, export_path)
    exporter.export_data(records)
