# Time on Profile Picture in Telegram
Automatically puts on your profile picture in Telegram the current time.

## Requirements
* telethon
* Pillow
The project uses Python3, all libraries are expected to be installed using `pip3`, with the following command:
```
sudo pip3 install -r requirements.txt
```
## Configuration and Usage

### Telegram API
At first you should generate your Telegram Application API ID and API Hash. They are expected to be secret, so store them in secure place. 
1. Open https://my.telegram.org and authorize there.
2. Open "API development tools" section.
3. Create application if you have not done this before. While creating application you have to enter "App title" and "Short name" (you can enter anything you want), the others fields might be empty.
4. Copy api_id and api_hash into the corresponding fields in `config.py`

### First run
After all mandatory things with Telegram API was done, you can finally run the project using command `python3 main.py`

### Customizing
All changes should be made in `config.py`. Short explanations of the fields are given using comments in the file

## Default Font
Font, that is used as a default one, is "DS-Digital" by Dusit Supasawat, you can find it here: https://www.dafont.com/ds-digital.font
