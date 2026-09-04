import argparse
from .scheduler import generate_report, run_scheduler

def main():
    parser = argparse.ArgumentParser(
        description="Enterprise automated PDF report generator"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("generate", help="Generate one PDF report")

    schedule_parser = subparsers.add_parser(
        "schedule", help="Run report generation automatically"
    )
    schedule_parser.add_argument(
        "--minutes", type=int, default=60,
        help="Minutes between reports (default: 60)"
    )

    args = parser.parse_args()

    if args.command == "generate":
        generate_report()
    elif args.command == "schedule":
        run_scheduler(args.minutes)

if __name__ == "__main__":
    main()
