import os

def write_tree_and_contents(start_path, output_file):
    with open(output_file, 'w') as f_out:
        for root, dirs, files in os.walk(start_path):
            level = root.replace(start_path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            f_out.write(f"{indent}{os.path.basename(root)}/\n")
            print(f"{indent}{os.path.basename(root)}/")  # Debug print for the directory
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                f_out.write(f"{subindent}{file}\n")
                print(f"{subindent}{file}")  # Debug print for the file
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f_in:
                        content = f_in.read()
                        f_out.write(f"{content}\n")
                        f_out.write("-----\n")
                except Exception as e:
                    print(f"Could not read file {file_path}: {e}")

if __name__ == "__main__":
    # Assuming the script is placed in the same directory as the project folder
    project_folder = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(project_folder, 'output.txt')
    write_tree_and_contents(project_folder, output_file)
    print(f"Output written to {output_file}")
