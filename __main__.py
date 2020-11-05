import argparse

from flpy_bank import run
from flpy_bank.env import init_env
from flpy_bank.exporter.registry import EXPORTER_REGISTRY
from flpy_bank.processor.registry import PROCESSOR_REGISTRY
from flpy_bank.parser.registry import PARSER_REGISTRY

p = argparse.ArgumentParser(description='BankStatementParser')
p.add_argument('-i',
               dest='input',
               help='A file to process',
               required=True)
p.add_argument('-p',
               dest='parser',
               help='The name for a supported file parser',
               choices=PARSER_REGISTRY.keys(),
               required=True)
p.add_argument('-f',
               dest='output_format',
               help='The name of a supported output format',
               choices=EXPORTER_REGISTRY.keys(),
               required=False,
               default='json')
p.add_argument('-o',
               dest='output',
               help='A path to the output file',
               required=True)
p.add_argument('-P',
               dest='processors',
               action='extend',
               nargs='+',
               help='One or more processors to run before exporting the data',
               choices=PROCESSOR_REGISTRY.keys(),
               default=['tag'])
p.add_argument('--tagrules',
               dest='tag_rules',
               help='A YAML file containing tagging rules',
               default='rules.yml')

args = p.parse_args()
init_env(args)
run(args.input,
    args.parser,
    args.processors,
    args.output_format,
    args.output)
