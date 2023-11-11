import os


def file_classing():
    """Classify files in the current directory into folders"""
    # Dictionary for mapping extensions to folder names
    extension_paths = {
        ('.mp3', '.wav', '.flac'): 'Audio',
        ('.avi', '.mp4', '.gif', '.flv'): 'Videos',
        ('.bmp', '.png', '.jpg'): 'Images',
        ('.txt', '.ppt', '.pptx', '.csv', '.xlsx', '.xls', '.doc', '.docx', '.odp', '.pdf'): 'Documents',
        ('.py', '.c', '.cpp', '.java', '.html', '.css', '.js', '.php', '.json', '.xml', '.sql'): 'Code'
    }
    # Get the current directory
    current_dir = os.getcwd()
    # Get the script name
    cuurent_script = os.path.basename(__file__)
    # Get the list of files and directories in the current directory
    list_files = os.listdir(current_dir)
    # Filter out only files from the list exept the current script
    list_files = [f for f in list_files if os.path.isfile(
        f) and f != cuurent_script]
    # Loop over each file to determine its destination directory
    for file in list_files:
        # Get the file extension
        file_extension = os.path.splitext(file)[1]
        # Initialize destination directory name defaut folder
        destination_dir_name = 'Divers'
        # Find the correct directory for the file extension
        for exetensions, folder_name in extension_paths.items():
            if file_extension in exetensions:
                destination_dir_name = folder_name
                break
        # Create the directory if it does not exist
        destination_dir = os.path.join(current_dir, destination_dir_name)
        os.makedirs(destination_dir, exist_ok=True)
        os.rename(os.path.join(current_dir, file), os.path.join(
            destination_dir, file))


def main():
    """Main function"""
    file_classing()


if __name__ == '__main__':
    main()
