# Default configuration for the project.


api_id = None # Your API ID from Telegram API Settings, as an integer

api_hash = None # Your API HASH from Telegram API Settings, as a string

api_sessions_dir = "./sessions" # Absolute or relative path to the directory, where sessions would be stored, do not write / at the end, if it is possible, do not change this parameter

api_session_name = "default" # Session name, should be as a valid filename in your system

font = ("./font/defaults/digit.ttf", 128) # Font settings, tuple consists of:
# - Path to file with the font, allowed only TrueType fonts, as a string
# - Font size, in points (pt), as an integer

color = ((0, 0, 0), (255, 255, 255)) # Color settings, tuple consists of:
# - Background color in numerical RGB format (each number is 0..255)
# - Text color in numerical RGB format (each number is 0..255)

dimensions = (512, 512) # Photo dimensions settings, tuple consists of:
# - Width, as an integer
# - Height, as an integer
# It is hightly recommended to make width equal to height

time_format = "%H:%M" # String, a Python date format (described at https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes), which will be used in order to generate image

cache_directory = "./cache" # Directory name used for the project's cache, do not write / at the end, if it is possible, do not change this parameter

image_filename = "image" # Filename of generated image, please don't use pathes and file extensions, if it is possible, do not change this parameter
