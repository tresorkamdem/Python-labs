import os
import logging

logging.basicConfig(
    filename="file_audit.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def audit_directory(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError("Directory not found")

        files = os.listdir(path)

        with open("audit_report.txt", "w") as report:
            report.write("FILE AUDIT REPORT\n")
            report.write("=" * 40 + "\n")

            for file in files:
                full_path = os.path.join(path, file)

                if os.path.isfile(full_path):
                    size = os.path.getsize(full_path)
                    report.write(f"{file} - {size} bytes\n")

            report.write("=" * 40 + "\n")
            report.write(f"Total files: {len(files)}\n")

        logging.info("Audit completed successfully.")
        print("Audit report generated.")

    except FileNotFoundError as e:
        logging.error(str(e))
        print("Error:", e)

    except PermissionError:
        logging.error("Permission denied.")
        print("Permission denied.")


if __name__ == "__main__":
    directory = input("Enter directory path to audit: ")
    audit_directory(directory)