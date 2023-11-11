""" Classify files in the current directory into folders using pathlib """
from pathlib import Path


def file_classing():
    """Classify files in the current directory into folders using pathlib"""
    # Dictionary for mapping extensions to folder names
    extension_paths = {
        ('.mp3', '.wav', '.flac'): 'Audio',
        ('.avi', '.mp4', '.gif', '.flv'): 'Videos',
        ('.bmp', '.png', '.jpg'): 'Images',
        ('.txt', '.ppt', '.pptx', '.csv', '.xlsx', '.xls', '.doc', '.docx', '.odp', '.pdf'): 'Documents',
        ('.py', '.c', '.cpp', '.java', '.html', '.css', '.js', '.php', '.json', '.xml', '.sql'): 'Code'
    }
    # Get the current directory
    current_dir = Path.cwd()
    # Get the script name
    current_script = Path(__file__).name
    # Get the list of files in the current directory, excluding the current script
    list_files = [f for f in current_dir.iterdir() if f.is_file()
                  and f.name != current_script]

    # Loop over each file to determine its destination directory
    for file in list_files:
        # Get the file extension
        file_extension = file.suffix
        # Initialize destination directory name default folder
        destination_dir_name = 'Divers'
        # Find the correct directory for the file extension
        for extensions, folder_name in extension_paths.items():
            if file_extension in extensions:
                destination_dir_name = folder_name
                break
        # Get the destination directory by joining  current directory with  destination directory
        destination_dir = current_dir / destination_dir_name
        # Create the directory if it does not exist
        destination_dir.mkdir(exist_ok=True)
        # Move the file
        file.rename(destination_dir / file.name)


def main():
    """Main function"""
    file_classing()


if __name__ == '__main__':
    main()
