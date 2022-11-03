import argparse
import os

from codecarbon import EmissionsTracker

def main():
    """Wraps codecarbon tracking around any given shell command."""

    parser = argparse.ArgumentParser(description='Wraps codecarbon tracking '
                                                 'around any given shell command.')

    # positional arguments
    parser.add_argument(
        'command',
        type=str,
        help='The shell command to be executed.'
        )

    parser.add_argument(
        '--name', '-n',
        type=str,
        default=None,
        help='The name for the entry in the codecarbon spreadsheet. '
             'If no name is given, then defaults to the command provided.'
        )

    args = parser.parse_args()
    cmd = args.command
    name = args.name or cmd  # default to name of command if no name given
    print(args)

    tracker = EmissionsTracker(project_name=name)
    tracker.start()
    os.system(cmd)
    print(cmd)
    tracker.stop()


if __name__ == "__main__":
    main()