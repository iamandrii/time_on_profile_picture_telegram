from telethon import TelegramClient, sync
from PIL import Image, ImageDraw, ImageFont
import sys, datetime, os.path, re, time, config, hashlib, argparse
from datetime import timedelta
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest

telegram_client = ""

def generate_image(actual_datetime):
	img = Image.new('RGB', config.dimensions, color = config.color[0])
	img_draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(config.font[0], config.font[1])
	draw_text = actual_datetime.strftime(config.time_format)
	_, _, tw, th = img_draw.textbbox((0, 0), draw_text, font = font)
	img_draw.text(((config.dimensions[0]-tw)/2, (config.dimensions[1]-th)/2), draw_text, font=font, fill=config.color[1])
	img.save(config.cache_directory+"/"+config.image_filename+".png", "PNG"); 

def delete_last_profile_picture():
	global telegram_client
	telegram_client(DeletePhotosRequest(telegram_client.get_profile_photos('me', limit=1)))

def update_profile_picture(actual_datetime):
	global telegram_client
	generate_image(actual_datetime)
	file = telegram_client.upload_file(f"{config.cache_directory}/{config.image_filename}.png")
	telegram_client(UploadProfilePhotoRequest(file))

def run_cycle():
	prev_datetime = None
	while True:
		try:
			actual_datetime = datetime.datetime.now()
			if actual_datetime.strftime(config.time_format) != prev_datetime:
				if prev_datetime != None:
					delete_last_profile_picture()
				prev_datetime = actual_datetime.strftime(config.time_format)
				update_profile_picture(actual_datetime)
				print("updating profile picture. text: "+actual_datetime.strftime(config.time_format))
			time.sleep(0.300)
		except KeyboardInterrupt:
			sys.exit()

def parse_hex(hex):
	if hex[0] == '#':
		hex = hex[1:]
	if (len(hex) != 3 and len(hex) != 6) or bool(re.compile(r'[^0-9A-Fa-f]+').search(hex)):
		raise ValueError("Given string is not valid hex-color string")
	if len(hex) == 3:
		return tuple(int(hex[i:i+1], 16) for i in range(0, 3))
	else:
		return tuple(int(hex[i:i+2], 16) for i in range(0, 6, 2))

def parse_arguments():
	parser = argparse.ArgumentParser(
		prog="python3 main.py",
		description="Automatically puts on your profile picture in Telegram the current time.\n\nAll of these arguments are recommended to be set in config.py.\nDetailed description of each option might be found in config.py",
		epilog="(c) 2022, Andrii Fylypiuk, the MIT License")
	parser.add_argument("--api-id", action="store", type=int, dest="api_id", help="Telegram API ID (required until set in config.py)")
	parser.add_argument("--api-hash", action="store", type=str, dest="api_hash", help="Telegram API Hash (required until set in config.py)")
	parser.add_argument("--api-sessions-dir", action="store", type=str, dest="api_sessions_dir", help="Path to directory where sessions should be stored, without / at the end")
	parser.add_argument("--api-session-name", action="store", type=str, dest="api_session_name", help="Session name")
	parser.add_argument("--font-family", action="store", type=str, dest="font_family", help="Path to the font file, should be in *.ttf format")
	parser.add_argument("--font-size", action="store", type=int, dest="font_size", help="Font size, in points (pt)")
	parser.add_argument("--background-color", action="store", type=str, dest="background_color", help="Background color, in hex (#RRGGBB) format, without # symbol")
	parser.add_argument("--text-color", action="store", type=str, dest="text_color", help="Text color, in hex (#RRGGBB) format, without # symbol")
	parser.add_argument("--photo-width", action="store", type=int, dest="photo_width", help="Generated photo width, in pixels (px)")
	parser.add_argument("--photo-height", action="store", type=int, dest="photo_height", help="Generated photo height, in pixels (px)")
	parser.add_argument("--time-format", action="store", type=str, dest="time_format", help="Time format (it is not recommended to set it using CLI-arguments)")
	parser.add_argument("--cache-directory", action="store", type=str, dest="cache_directory", help="Path to directory where cache should be stored, without / at the end")
	parser.add_argument("--image-filename", action="store", type=str, dest="image_filename", help="Filename of generated temporary photo")
	args = parser.parse_args()
	if args.api_id != None:
		config.api_id=args.api_id 
	if args.api_hash != None:
		config.api_hash=args.api_hash
	if args.api_sessions_dir != None:
		config.api_sessions_dir = args.api_sessions_dir
	if args.api_session_name != None:
		config.api_session_name = args.api_session_name
	if args.font_family != None:
		config.font[0] = args.font_family
	if args.font_size != None:
		config.font[1] = args.font_size
	if args.background_color != None:
		config.color[0] = parse_hex(args.background_color)
	if args.text_color != None:
		config.color[1] = parse_hex(args.text_color)
	if args.photo_width != None:
		config.dimensions[0] = args.photo_width
	if args.photo_height != None:
		config.dimensions[1] = args.photo_height
	if args.time_format != None:
		config.time_format = args.time_format
	if args.cache_directory != None:
		config.cache_directory = args.cache_directory
	if args.image_filename != None:
		config.image_filename = args.image_filename

def validate_config():
	if config.api_id == None or config.api_hash == None:
		raise ValueError("Telegram API ID and API Hash should be both declared either in config.py or CLI-arguments. Run program with -h flag for more information.")

def ensure_cache_directory():
	if not os.path.exists(config.cache_directory):
		os.mkdir(config.cache_directory)

def ensure_sessions_directory():
	if not os.path.exists(config.api_sessions_dir):
		os.mkdir(config.api_sessions_dir)

def connect_and_run():
	global telegram_client
	telegram_client = TelegramClient(config.api_sessions_dir+"/"+config.api_session_name, config.api_id, config.api_hash)
	telegram_client.start()
	run_cycle()

if __name__ == "__main__":
	parse_arguments()
	validate_config()
	ensure_sessions_directory()
	ensure_cache_directory()
	connect_and_run()
