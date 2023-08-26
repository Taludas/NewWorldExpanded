import os

def create_links(start_folder, x):
    parent_dir_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
    script_filename = os.path.basename(__file__)
    
    for root, dirs, files in os.walk(start_folder):
        for filename in files:
            if filename != script_filename:  # Skip copying the script itself
                filepath = os.path.join(root, filename)
                y = os.path.basename(root)
                z = os.path.splitext(filename)[0]
                file_extension = os.path.splitext(filename)[1]
                
                link_filename = filename + ".lnk"
                link_filepath = os.path.join(root, link_filename)
                
                link_text = f'data/sessions/islands/pool/moderate/{x}/_gamedata/{x}_river_01/{parent_dir_name}/{y}/{z}{file_extension}'
                
                with open(link_filepath, 'w') as link_file:
                    link_file.write(link_text)
                
                os.remove(filepath)  # Remove the original file

if __name__ == "__main__":
    start_folder = input("Enter the start folder path: ")
    x = input("Enter the value for x: ")
    create_links(start_folder, x)
    print("Link files created and original files (except script) deleted successfully!")
