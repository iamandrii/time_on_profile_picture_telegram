from telethon import TelegramClient, sync
from PIL import Image, ImageDraw, ImageFont
import sys, datetime, os.path, re, time, Config
from datetime import timedelta
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest

W, H = Config.dimens

__color__bg, __color__text, __font, __client = ("", "", "", "")
__prefix, __postfix = Config.text_fixs
__font_size = 0
def hash_parameters():
	global __color__bg, __color__text, __font, __prefix, __postfix, __font_size
	return (color_to_hex(__color__bg)+color_to_hex(__color__text)+str(__font_size)+__font.replace("/", "_")+str(hash(__prefix+__postfix)));
def generate_image(mtime):
	global __color__bg, __color__text, __font, W, H, __prefix, __postfix, __font_size
	img = Image.new('RGB', (W,H), color = __color__bg)
	img_draw = ImageDraw.Draw(img)
	fnt = ImageFont.truetype("font/"+__font+".ttf", __font_size);
	draw_text = __prefix + mtime + __postfix
	tw, th = img_draw.textsize(draw_text, font = fnt)
	img_draw.text(((W-tw)/2, (H-th)/2), draw_text, font=fnt, fill=__color__text);
	img.save("photos/"+mtime.replace(":", "_")+"___"+hash_parameters()+".png", "PNG"); 
def check_image(Date):
	flnm = Date.strftime('%H_%M')
	if not os.path.exists("photos/"+flnm+"___"+hash_parameters()+".png"):
		generate_image(Date.strftime('%H:%M'))
def update_profile_picture(Date):
	global __client
	check_image(Date)
	__client(DeletePhotosRequest(__client.get_profile_photos('me')))
	flnm = Date.strftime('%H_%M')+"___"+hash_parameters()+".png"
	file = __client.upload_file(f"photos/{flnm}")
	__client(UploadProfilePhotoRequest(file))
def run():
	prev_date = '-1'
	time_format = '%H %M'
	while True:
		try:
			Date = datetime.datetime.now()
			if(Date.strftime(time_format) != prev_date):
				prev_date = Date.strftime(time_format)
				update_profile_picture(Date)
				print("updating profile picture. Time: "+Date.strftime('%H:%M'))
			time.sleep(0.300)
		except KeyboardInterrupt:
			sys.exit()

def ishex(strg, search=re.compile(r'[^0-9A-Fa-f]+').search):
	return not bool(search(strg))
def color_to_hex(color):
	return '%02x%02x%02x' % color
def change_font(arg):
	global __font
	font_path = arg
	if not os.path.exists("font/"+font_path+".ttf"):
		print("Error. Font not found\nNotice that font must be placed in 'font' directory, ending with .ttf and have no spaces in name\n -D//font: " + font_path)
		sys.exit()
	__font = font_path
def change_text(arg):
	global __color__text
	color = arg.lstrip('#')
	if not (len(color) == 6 and ishex(color)):
		print("Error. Color must be entered with hex-format (#RRGGBB)\n -D//color: #"+color)
		sys.exit()
	__color__text = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
def change_bg(arg):
	global __color__bg
	color = arg.lstrip('#')
	if not (len(color) == 6 and ishex(color)):
		print("Error. Color must be entered with hex-format (#RRGGBB)\n -D//color: #"+color)
		sys.exit()
	__color__bg = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
def change_font_size(arg):
	global __font_size
	val = int(arg)
	if val < 0:
		print("Error. Font size is NaN\n -D//font_size: "+val)
		sys.exit()
	__font_size = val
def change_prefix(arg):
	global __prefix
	__prefix = arg
def change_postfix(arg):
	global __postfix
	__postfix = arg
arguments = dict([("--font=", change_font), ("--text-color=", change_text), ("--bg-color=", change_bg), ("--prefix=", change_prefix), ("--postfix=", change_postfix), ("--font-size=", change_font_size)])
def load():
	global __client
	change_font(Config.font[0])
	change_bg("#"+color_to_hex(Config.color[0]))
	change_text("#"+color_to_hex(Config.color[1]))
	change_font_size(Config.font[1])
	__client = TelegramClient(Config.api_sessionname, Config.api_id, Config.api_hash)
	__client.start()
	for i in sys.argv:
		for k, v in arguments.items():
			if i.startswith(k):
				v(i.split('=', 1)[1]);
	run()
load()