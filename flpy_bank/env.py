from argparse import Namespace

RUNTIME_ARGS: Namespace


def init_env(args: Namespace):
    global RUNTIME_ARGS
    RUNTIME_ARGS = args
