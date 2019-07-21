# time on profile picture telegram
Automatically puts on your profile picture in the telegram the current time
## WHYYYY
**It is very interesting thing, especially when you are coder.**
## How to use it
### Requirements
* PIP
* Telethon
* Pillow
* Telegram
```
sudo pip3 install telethon Pillow
```
### Using
Open `Config.py` throw any text editor.
In front of `api_id` & `api_hash` enter corresponding values. You can get them by https://my.telegram.org/.
_P.S. open https://my.telegram.org/ , login there, click on `API development tools`, 
copy corresponding values, enter them in `Config.py` (brackets delete)_
Now open Terminal & enter:
```
python3 main.py
```
All done!
### Customizing
#### CLI-args
1. **--font=_myfont_** - setting your own font. Font must be in .ttf format & be placed in `font/` directory. Instead of ___myfont___ you must enter font name with relative path from `font/` without ending. For example: font is `fonts/abc/def/gh.ttf`, then your argument will be this: `--font=abc/def/gh`
2. **--text-color=_#RRGGBB_** - set color for text in hex format (only **#RRGGBB**)
3. **--bg-color=_#RRGGBB_** - set color for background in hex format (only **#RRGGBB**)
4. **--prefix=_text_** - text before time
5. **--postfix=_text_** - text after time
6. **--font-size=_number_** - size of text in pixels
#### by Config.py
All of listed above and dimensions of photo can be setted throw `Config.py`. But, color must be in decimal format. _P.S. first `color` is background color, second `color` is text color. Also, first `text_fixs` is prefix, second `text_fixs` is postfix._
