import os
import time
import mysql.connector
from pathlib import Path
from PIL import Image
from moviepy.editor import VideoFileClip

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="media"
)
db_cursor = db_connection.cursor()

# Variable to keep track of the incremental value for media and tags tables
media_id_counter = 1
tags_id_counter = 1


def get_tag_id(tag_name):
    # Execute a SELECT query to get the corresponding id from the tags table
    select_query = "SELECT id FROM tags WHERE tag_name = %s LIMIT 1"
    db_cursor.execute(select_query, (tag_name,))
    row = db_cursor.fetchone()

    if row:
        return row[0]
    else:
        # If the tag doesn't exist, insert a new tag and return its id
        insert_query = "INSERT INTO tags (id, tag_name) VALUES (%s, %s)"
        db_cursor.execute(insert_query, (tags_id_counter, tag_name))
        db_connection.commit()
        return tags_id_counter


def get_file_properties(file_path):
    try:
        file_path_str = str(file_path)
        file_extension = file_path_str.split('.')[-1].lower()

        if file_extension in ['jpg', 'jpeg', 'png', 'gif', 'cr2', 'heic', 'nef']:
            with Image.open(file_path) as img:
                file_type = img.format
                width, height = img.size
                quality = img.info.get('quality', None)
        elif file_extension in ['mp4', 'avi', 'mkv', 'mov']:
            with VideoFileClip(file_path) as video:
                file_type = video.fmt
                quality = video.reader.infos.get('video_size', None)
                width, height = video.size
        else:
            # Handle other file types or skip them
            return None

        file_properties = (file_extension, file_type, width, height, quality)
        return file_properties

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None


def check_edit():
    edited = input("Edited? (Y or N) : ")
    if edited.lower() == 'y':
        return True
    elif edited.lower() == 'n':
        return False
    else:
        print("Invalid input")
        return check_edit()


# Directory containing your media files
media_directory = r'C:\Users\User\Downloads\pics to try'

# Iterate through files in the directory
for file_path in Path(media_directory).rglob('*'):
    if file_path.is_file():
        # Get file properties
        file_name = file_path.name
        absolute_path = file_path.resolve()
        file_properties = get_file_properties(file_path)
        if file_properties is None:
            print("File not supported, yet :) Skipping for now")
            continue
        file_extension, file_type, width, height, quality = file_properties
        print(file_name)
        tag_name = input("Tags (Separated by comma): ")
        edited = check_edit()

        # Convert modification time to a human-readable format
        modification_time_formatted = time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        # Get the corresponding tag_id from the tags table
        tag_id = get_tag_id(tag_name)

        # Insert file information into the media table
        insert_query1 = """
            INSERT INTO media (id, filename, file_path, tag_id)
            VALUES (%s, %s, %s, %s)
        """
        values1 = (media_id_counter, file_name, str(absolute_path), tag_id)

        # Execute the query
        db_cursor.execute(insert_query1, values1)

        # Increment the counters
        media_id_counter += 1
        tags_id_counter += 1

# Commit changes and close the database connection
db_connection.commit()
print("All files in the given Path are updated to the Database")
db_connection.close()
