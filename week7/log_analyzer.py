import re
from collections import Counter


class LogAnalyzer:
    def __init__(self, logfile):
        self.logfile = logfile

        self.total_requests = 0
        self.security_incidents = []
        self.errors = []
        self.warning_counter = Counter()

        # Pattern for WARNING lines
        self.warning_pattern = re.compile(
            r"\d{4}-\d{2}-\d{2} .* - WARNING - (.*)"
        )

        # Pattern for ERROR lines
        self.error_pattern = re.compile(
            r"\d{4}-\d{2}-\d{2} .* - ERROR - (.*)"
        )

    def process_logs(self):
        try:
            with open(self.logfile, "r") as f:
                for line in f:
                    line = line.strip()

                    # Count total processed log lines
                    if " - INFO - " in line or " - WARNING - " in line or " - ERROR - " in line:
                        self.total_requests += 1

                    # Capture warnings
                    warning_match = self.warning_pattern.match(line)
                    if warning_match:
                        message = warning_match.group(1)
                        self.security_incidents.append(message)

                        if "Forbidden access" in message:
                            self.warning_counter["Forbidden"] += 1
                        elif "SQL injection" in message:
                            self.warning_counter["SQL Injection"] += 1
                        elif "Brute force" in message:
                            self.warning_counter["Brute Force"] += 1

                    # Capture errors
                    error_match = self.error_pattern.match(line)
                    if error_match:
                        self.errors.append(error_match.group(1))

        except FileNotFoundError:
            print("Log file not found.")
            return

    def generate_reports(self):

        # Summary report
        with open("summary_report.txt", "w") as f:
            f.write("SERVER LOG SUMMARY\n")
            f.write("=" * 40 + "\n")
            f.write(f"Total log entries: {self.total_requests}\n\n")

            f.write("Security Incident Breakdown:\n")
            for key, value in self.warning_counter.items():
                f.write(f"{key}: {value}\n")

            f.write(f"\nTotal Errors: {len(self.errors)}\n")

        # Security incidents file
        with open("security_incidents.txt", "w") as f:
            f.write("SECURITY INCIDENTS\n")
            f.write("=" * 40 + "\n")
            for incident in self.security_incidents:
                f.write(incident + "\n")

        # Error log file
        with open("error_log.txt", "w") as f:
            f.write("ERROR LOGS\n")
            f.write("=" * 40 + "\n")
            for error in self.errors:
                f.write(error + "\n")

    def print_console_summary(self):
        print("\nAnalysis Complete")
        print(f"Total log entries: {self.total_requests}")
        print(f"Security incidents: {len(self.security_incidents)}")
        print(f"Errors found: {len(self.errors)}")


def main():
    analyzer = LogAnalyzer("server.log")
    analyzer.process_logs()
    analyzer.generate_reports()
    analyzer.print_console_summary()


if __name__ == "__main__":
    main()