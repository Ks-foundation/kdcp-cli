import subprocess
import os
import shutil

class KDPC:
    def __init__(self):
        self.commands = {
            'run': self.run_command,
            'write': self.write_file,
            'delete': self.delete_file,
            'list': self.list_files,
            'view': self.view_file,
            'copy': self.copy_file,
            'move': self.move_file,
            'search': self.search_files,
            'compress': self.compress_file,
            'extract': self.extract_file,
            'change_permissions': self.change_permissions,
            'file_size': self.get_file_size,
            'compare': self.compare_files,
            'log': self.log_execution
        }

    def run_command(self, args):
        try:
            subprocess.run(args, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

    def write_file(self, args):
        if len(args) < 3:
            print("Usage: write <file_name> <content>")
            return
        file_name = args[1]
        content = ' '.join(args[2:])
        try:
            with open(file_name, 'w') as f:
                f.write(content)
            print(f"File '{file_name}' written successfully.")
        except Exception as e:
            print(f"Error writing to file: {e}")

    def delete_file(self, args):
        if len(args) < 2:
            print("Usage: delete <file_name>")
            return
        file_name = args[1]
        try:
            os.remove(file_name)
            print(f"File '{file_name}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting file: {e}")

    def list_files(self, args):
        files = os.listdir()
        print("Files in current directory:")
        for file in files:
            print(file)

    def view_file(self, args):
        if len(args) < 2:
            print("Usage: view <file_name>")
            return
        file_name = args[1]
        try:
            with open(file_name, 'r') as f:
                content = f.read()
            print(f"Contents of '{file_name}':")
            print(content)
        except Exception as e:
            print(f"Error viewing file: {e}")

    def copy_file(self, args):
        if len(args) < 3:
            print("Usage: copy <source_file> <destination_file>")
            return
        source_file = args[1]
        destination_file = args[2]
        try:
            shutil.copy2(source_file, destination_file)
            print(f"File '{source_file}' copied to '{destination_file}' successfully.")
        except Exception as e:
            print(f"Error copying file: {e}")

    def move_file(self, args):
        if len(args) < 3:
            print("Usage: move <source_file> <destination_file>")
            return
        source_file = args[1]
        destination_file = args[2]
        try:
            shutil.move(source_file, destination_file)
            print(f"File '{source_file}' moved to '{destination_file}' successfully.")
        except Exception as e:
            print(f"Error moving file: {e}")

    def search_files(self, args):
        if len(args) < 2:
            print("Usage: search <pattern>")
            return
        pattern = args[1]
        matches = []
        for root, dirs, files in os.walk('.'):
            for file in files:
                if pattern in file:
                    matches.append(os.path.join(root, file))
        if matches:
            print("Matching files found:")
            for match in matches:
                print(match)
        else:
            print("No matching files found.")

    def compress_file(self, args):
        if len(args) < 3:
            print("Usage: compress <source> <destination>")
            return
        source = args[1]
        destination = args[2]
        try:
            shutil.make_archive(destination, 'zip', source)
            print(f"Directory '{source}' compressed to '{destination}.zip' successfully.")
        except Exception as e:
            print(f"Error compressing directory: {e}")

    def extract_file(self, args):
        if len(args) < 2:
            print("Usage: extract <archive>")
            return
        archive = args[1]
        try:
            shutil.unpack_archive(archive)
            print(f"Archive '{archive}' extracted successfully.")
        except Exception as e:
            print(f"Error extracting archive: {e}")

    def change_permissions(self, args):
        if len(args) < 3:
            print("Usage: change_permissions <file_name> <permissions>")
            return
        file_name = args[1]
        permissions = args[2]
        try:
            os.chmod(file_name, int(permissions, 8))
            print(f"Permissions of '{file_name}' changed to '{permissions}' successfully.")
        except Exception as e:
            print(f"Error changing permissions: {e}")

    def get_file_size(self, args):
        if len(args) < 2:
            print("Usage: file_size <file_name>")
            return
        file_name = args[1]
        try:
            size = os.path.getsize(file_name)
            print(f"Size of '{file_name}': {size} bytes")
        except Exception as e:
            print(f"Error getting file size: {e}")

    def compare_files(self, args):
        if len(args) < 3:
            print("Usage: compare <file1> <file2>")
            return
        file1 = args[1]
        file2 = args[2]
        try:
            with open(file1, 'r') as f1, open(file2, 'r') as f2:
                if f1.read() == f2.read():
                    print("Files are identical.")
                else:
                    print("Files are different.")
        except Exception as e:
            print(f"Error comparing files: {e}")

    def log_execution(self, args):
        if len(args) < 2:
            print("Usage: log <file_name>")
            return
        file_name = args[1]
        try:
            with open(file_name, 'a') as f:
                f.write("File executed\n")
            print(f"Execution logged to '{file_name}' successfully.")
        except Exception as e:
            print(f"Error logging execution: {e}")

    def start(self):
        while True:
            user_input = input("kdpc> ").strip().split()
            if not user_input:
                continue
            command = user_input[0]
            args = user_input[1:]
            if command == 'exit':
                break
            elif command in self.commands:
                self.commands[command](args)
            else:
                print("Invalid command. Available commands: run, write, delete, list, view, copy, move, search, compress, extract, change_permissions, file_size, compare, log, exit")

if __name__ == "__main__":
    kdpc = KDPC()
    kdpc.start()
