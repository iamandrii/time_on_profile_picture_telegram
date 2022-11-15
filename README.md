# Time on Profile Picture in Telegram
Automatically puts on your profile picture in Telegram the current time.

## Requirements
* telethon
* Pillow (version >= 8.0.0)

The project uses Python3, all libraries are expected to be installed using `pip3`, with the following command:
```bash
sudo pip3 install -r requirements.txt
```
## Configuration and Usage

### Telegram API
At first you should generate your Telegram Application API ID and API Hash. They are expected to be secret, so store them in secure place. 
1. Open https://my.telegram.org and authorize there.
2. Open "API development tools" section.
3. Create application if you have not done this before. While creating application you have to enter "App title" and "Short name" (you can enter anything you want), the others fields might be empty.
4. Your API ID and API Hash should be generated right now.

_more information about this [here](https://core.telegram.org/api/obtaining_api_id)_

### Standard Usage
After all mandatory things with Telegram API was done, you can finally run the project using the following command (do not forget to replace `API_ID` and `API_HASH` with yours):
```bash
python3 main.py --api_id API_ID --api_hash API_HASH
```

### Docker without saving session
In order to build image, write the following command:
```bash
docker build -t time-on-profile-picture-telegram
```
In order to run image, write the following command (do not forget to replace `API_ID` and `API_HASH` with yours):
```bash
docker run -i -t time-on-profile-picture-telegram --api-id API_ID --api-hash API_HASH
```

### Docker with saving session 
In order to build image, write the following command:
```bash
docker build -t time-on-profile-picture-telegram
```
By the next step, you should generate session, so you need to run container with open _stdin_. Run it with the following command (do not forget to replace `API_ID` and `API_HASH` with yours):
```bash
docker run -i -t -v /path/to/sessions/storage:/usr/src/app/sessions time-on-profile-picture-telegram --api-id API_ID --api-hash API_HASH
```
Please, replace _/path/to/sessions/storage_ with some existing directory on the host, which is secure enough. During the next run, you won't be promted for phone number, code, and password, so you can run container in detached mode:
```bash
docker run -d -t -v /path/to/sessions/storage:/usr/src/app/sessions time-on-profile-picture-telegram --api-id API_ID --api-hash API_HASH
```

## Customizing
All changes are recommended to be made in `config.py` instead of using CLI-arguments. Short explanations of the fields are given using comments in the file. Short cheatsheet about CLI-arguments might be received by running with `--help` flag. 

**It is also strongly recommended to add your API ID and API Hash to `config.py` and as a result get rid of `--api-id` and `--api-hash` CLI-arguments.**

## Default Font
Font, that is used as a default one, is ["DS-Digital" by Dusit Supasawat](https://www.dafont.com/ds-digital.font).
