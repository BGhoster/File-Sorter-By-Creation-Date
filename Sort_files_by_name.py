# File sorter based off dates

import os
import shutil
import datetime

# Specify the source directory where the files are located
source_directory = r"PATH"

# Iterate over all files in the source directory
for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)
    
    # Check if the path is a file
    if os.path.isfile(file_path):
        
        # Get the creation date of the file
        creation_time = os.path.getctime(file_path)
        creation_date = datetime.datetime.fromtimestamp(creation_time).date()
        
        # Create the destination directory with the date if it doesn't exist
        destination_directory = os.path.join(source_directory, str(creation_date))
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
        
        # Move the file to the corresponding folder
        destination_path = os.path.join(destination_directory, filename)
        shutil.move(file_path, destination_path)
