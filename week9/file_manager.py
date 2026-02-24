import os


def file_manager_demo():
    print("Current Directory:", os.getcwd())

    folder_name = "lab_files"

    # Create folder
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print("Created folder:", folder_name)

    # Create files
    file_names = ["file1.txt", "file2.txt", "file3.txt"]

    for name in file_names:
        path = os.path.join(folder_name, name)
        with open(path, "w") as f:
            f.write("Test file")
        print("Created:", name)

    # List files
    print("\nFiles:")
    for file in os.listdir(folder_name):
        print("-", file)

    # Rename file
    os.rename(
        os.path.join(folder_name, "file2.txt"),
        os.path.join(folder_name, "renamed_file.txt")
    )
    print("\nRenamed file2.txt")

    # Cleanup
    print("\nCleaning up...")
    for file in os.listdir(folder_name):
        os.remove(os.path.join(folder_name, file))
    os.rmdir(folder_name)

    print("Cleanup complete!")


if __name__ == "__main__":
    file_manager_demo()