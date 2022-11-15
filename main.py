from telethon import TelegramClient, sync
from PIL import Image, ImageDraw, ImageFont
import sys, datetime, os.path, re, time, config, hashlib
from datetime import timedelta
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest

telegram_client = ""

def ensure_cache_directory():
	if not os.path.exists(config.cache_directory):
		os.mkdir(config.cache_directory)

def generate_image(actual_datetime):
	img = Image.new('RGB', config.dimensions, color = config.color[0])
	img_draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(config.font[0], config.font[1])
	draw_text = actual_datetime.strftime(config.time_format)
	_, _, tw, th = img_draw.textbbox((0, 0), draw_text, font = font)
	img_draw.text(((config.dimensions[0]-tw)/2, (config.dimensions[1]-th)/2), draw_text, font=font, fill=config.color[1])
	ensure_cache_directory()
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

def connect_and_run():
	global telegram_client
	telegram_client = TelegramClient(config.api_sessions_dir+"/"config.api_session_name, config.api_id, config.api_hash)
	telegram_client.start()
	run_cycle()

if __name__ == "__main__":
	connect_and_run()
