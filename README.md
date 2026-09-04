# Enterprise Python Automation Capstone

An end-to-end production-style Python application that fetches public Bitcoin market data, processes it, generates a professional PDF report, logs execution, and supports automated scheduling through a CLI.

## Features

- Public API integration
- Data processing layer
- Automated PDF generation
- Command-line interface with `argparse`
- Scheduled execution
- Logging and exception handling
- Unit tests
- Modern Python packaging with `pyproject.toml`

## Architecture

```text
                    +----------------------+
                    |      CLI (argparse)  |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    |     Scheduler        |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    |      API Client      |
                    |   Public CoinDesk    |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    |    Data Processor    |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    |    PDF Generator     |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    |     reports/*.pdf    |
                    +----------------------+

                    Logging --> logs/application.log
```

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scriptsctivate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install the package itself:

```bash
pip install -e .
```

## Usage

Generate one report:

```bash
python -m report_generator.cli generate
```

After installation, the packaged CLI also works:

```bash
enterprise-report generate
```

Start scheduled execution:

```bash
python -m report_generator.cli schedule --minutes 60
```

For a quick demonstration, use a short interval:

```bash
python -m report_generator.cli schedule --minutes 1
```

Stop the scheduler with `Ctrl+C`.

## Output

A generated report is saved as:

```text
reports/bitcoin_automated_report.pdf
```

Application logs are stored in:

```text
logs/application.log
```

## Testing

Run:

```bash
pytest
```

## Production Considerations

For production deployment, API credentials (if a private API is used) should be stored in environment variables or a secrets manager. A process supervisor such as systemd, Docker, or a cloud scheduler can be used instead of keeping the scheduler in a terminal.

## Technologies

- Python
- Requests
- ReportLab
- Schedule
- Argparse
- Pytest
- Public REST API

## Capstone Proof

The repository should be submitted with:

1. Complete GitHub source code.
2. A video walkthrough showing installation, CLI execution, API retrieval, generated PDF, logs, and tests.

## License

MIT
