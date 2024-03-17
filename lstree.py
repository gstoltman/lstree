import os

def list_tree(directory, prefix=""):
    if not os.path.isdir(directory):
        print("Invalid directory: ", directory)
        return

    sort_paths = sorted(os.listdir(directory))
    for count, item in enumerate(sort_paths):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            connector = "├──" if count < len(sort_paths) - 1 else "└──"
            print(f"{prefix}{connector} {item}/")
        else:
            connector = "├──" if count < len(sort_paths) - 1 else "└──"
            print(f"{prefix}{connector} {item}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        root_directory = sys.argv[1]
    else:
        print("Input: python lstree.py [DIRECTORY]")
        sys.exit(1)

    list_tree(root_directory)
