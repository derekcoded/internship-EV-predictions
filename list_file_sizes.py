import os

def list_files_with_sizes(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                size = os.path.getsize(filepath)
                print(f"{filepath}: {size} bytes")
            except Exception as e:
                print(f"Error getting size for {filepath}: {e}")

if __name__ == "__main__":
    list_files_with_sizes(".")
