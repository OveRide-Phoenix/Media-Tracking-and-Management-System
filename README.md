# Media-Tracking-and-Management-System

## Project Overview:
This media management project extracts metadata from images and videos, storing it in a MySQL database. Utilizing Python and libraries like PIL, moviepy, and Flask, the system manages file details, including filename, path, type, dimensions, and editing status. The MySQL database, named "media," comprises two tables: media for general file information and tags for details about tags, including the editing status.

## Media File Processing:
The project employs Python and libraries such as os, time, mysql.connector, pathlib, PIL (Pillow), and moviepy for handling media files.

## MySQL Database:
A MySQL database named "media" serves as the storage hub for media file information and associated tags.

## Database Schema:
Structured storage for file and tag information is facilitated by two main tables: media and tags.

## Media File Insertion:
The script systematically processes media files in a specified directory, extracting file properties, taking user input for tags and editing status, and seamlessly inserting the gathered data into the MySQL database.

## Tag Assignment:
The tag_id foreign key in the media table is dynamically assigned the corresponding id from the tags table based on user-provided tags.

## Flask Web Application:
A user-friendly Flask web application acts as an interface for searching media files. Users can initiate searches based on file type, filename, tags, or editing status.

## Searching Capabilities:
Users benefit from robust search capabilities, allowing them to find media files with precision. The Flask web app enables searches based on file type, filename, dimensions, and user-assigned tags, enhancing the overall usability of the media management system.
