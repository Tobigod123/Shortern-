#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#    Script Improved by Zylern


from . import *
from .config import *
from .worker import *
from .devtools import *
from .FastTelethon import *
from time import time
from bot.Shotren import *
LOGS.info("Starting...")

try:
    bot.start(bot_token=BOT_TOKEN)
except Exception as er:
    LOGS.info(er)


####### GENERAL CMDS ########

@bot.on(events.NewMessage(pattern="/start"))
async def start(_, message):
    if len(message.command) > 1:
        userid = message.from_user.id
        input_token = message.command[1]

        # Check if the user is registered
        if userid not in user_data:
            return await sendMessage(message, 'Who are you?')

        data = user_data[userid]

        # Check if the token is valid
        if 'token' not in data or data['token'] != input_token or is_token_expired(data['time']):
            return await sendMessage(message, 'This is a token already expired or invalid. Please generate a new one.')

        # Refresh the token and update the time
        data['token'] = str(uuid4())
        data['time'] = time()
        user_data[userid].update(data)

        return await sendMessage(message, 'Token refreshed successfully!')
    
    elif config_dict['DM_MODE']:
        start_string = 'Bot Started.\n' \
            'Now you can change settings and encode.\n'
    else:
        start_string = '🌹 Welcome To One Of A Modified zenith encode bot\n' \
            'This bot can encode your videos and you can change the FFMPEG settings !\n' \
            '👨🏽‍💻 Powered By: "https://t.me/AnimeZenith"'

    await sendMessage(message, start_string)

def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token

@bot.on(events.NewMessage(pattern="/setcode"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!**")
    await coding(e)
def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token

@bot.on(events.NewMessage(pattern="/getcode"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!**")
    await getcode(e)

def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token

@bot.on(events.NewMessage(pattern="/showthumb"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!**")
    await getthumb(e)

def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token

@bot.on(events.NewMessage(pattern="/logs"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!**")
    await getlogs(e)

def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token

@bot.on(events.NewMessage(pattern="/cmds"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!**")
    await zylern(e)
    
def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token


@bot.on(events.NewMessage(pattern="/ping"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!**")
    await up(e)
    
def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token

@bot.on(events.NewMessage(pattern="/sysinfo"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!**")
    await sysinfo(e)

def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token

@bot.on(events.NewMessage(pattern="/leech"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!**")
    await dl_link(e)

def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token

@bot.on(events.NewMessage(pattern="/help"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!**")
    await ihelp(e)
    
def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token


@bot.on(events.NewMessage(pattern="/renew"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!**")
    await renew(e)
    
def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token


@bot.on(events.NewMessage(pattern="/clear"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!**")
    await clearqueue(e)

def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token

@bot.on(events.NewMessage(pattern="/speed"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!**")
    await test(e)
    
def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token
  

########## Direct ###########

@bot.on(events.NewMessage(pattern="/eval"))
async def _(e):
    await eval(e)
    
def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token

@bot.on(events.NewMessage(pattern="/bash"))
async def _(e):
    await bash(e)

def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token

######## Callbacks #########

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stats(.*)")))
async def _(e):
    await stats(e)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"skip(.*)")))
async def _(e):
    await skip(e)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile("help")))
async def _(e):
    await help(e)

########## AUTO ###########

@bot.on(events.NewMessage(incoming=True))
async def _(event):
        if str(event.sender_id) not in OWNER and event.sender_id !=DEV:
            return await event.reply_text("**Sorry You're not An Authorised User!**")
        if not event.photo:
            return
        os.system("rm thumb.jpg")
        await event.client.download_media(event.media, file="/bot/thumb.jpg")
        await event.reply("**Thumbnail Saved Successfully.**")
    
def is_token_expired(expire_time):
    config_dict = {
        'TOKEN_TIMEOUT': 3600  # Assuming TOKEN_TIMEOUT is set to 1 hour (3600 seconds)
    }
    # Check if TOKEN_TIMEOUT is not set, indicating that tokens never expire
    if not config_dict['TOKEN_TIMEOUT']:
        return False

    # Calculate the time elapsed in seconds since the token's expiration time
    elapsed_time = time() - expire_time

    # Compare the elapsed time with the TOKEN_TIMEOUT value
    if elapsed_time > config_dict['TOKEN_TIMEOUT']:
        return True  # Token has expired
    else:
        return False  # Token is still valid
        
def is_valid_token_user(user_id):
    if user_id in user_data:
        # Retrieve the user's data from user_data dictionary
        data = user_data[user_id]

        # Check if the user has a token and if it is not expired
        if 'token' in data and not is_token_expired(data.get('time', 0)):
            return True  # User has a valid token

    return False  # User does not have a valid token


@bot.on(events.NewMessage(incoming=True))
async def _(e):
    await encod(e)


async def something():
    for i in itertools.count():
        try:
            if not WORKING and QUEUE:
                user = int(OWNER.split()[0])
                e = await bot.send_message(user, "**📥 Downloading Queue Files...**")
                s = dt.now()
                try:
                    if isinstance(QUEUE[list(QUEUE.keys())[0]], str):
                        dl = await fast_download(
                            e, list(QUEUE.keys())[0], QUEUE[list(QUEUE.keys())[0]]
                        )
                    else:
                        dl, file = QUEUE[list(QUEUE.keys())[0]]
                        tt = time.time()
                        dl = "downloads/" + dl
                        with open(dl, "wb") as f:
                            ok = await download_file(
                                client=bot,
                                location=file,
                                out=f,
                                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                                    progress(
                                        d,
                                        t,
                                        e,
                                        tt,
                                        f"**📥 Downloading**\n__{dl.replace(f'downloads/', '')}__",
                                    )
                                ),
                            )
                except Exception as r:
                    LOGS.info(r)
                    WORKING.clear()
                    QUEUE.pop(list(QUEUE.keys())[0])
                es = dt.now()
                kk = dl.split("/")[-1]
                aa = kk.split(".")[-1]
                newFile = dl.replace(f"downloads/", "").replace(f"_", " ")
                rr = "encode"
                bb = kk.replace(f".{aa}", ".mkv")
                out = f"{rr}/{bb}"
                thum = "thumb.jpg"
                dtime = ts(int((es - s).seconds) * 1000)
                hehe = f"{out};{dl};{list(QUEUE.keys())[0]}"
                wah = code(hehe)
                nn = await e.edit(
                    "**🗜 Compressing...**",
                    buttons=[
                        [Button.inline("STATS", data=f"stats{wah}")],
                        [Button.inline("CANCEL", data=f"skip{wah}")],
                    ],
                )
                cmd = f"""ffmpeg -i "{dl}" {ffmpegcode[0]} "{out}" -y"""
                process = await asyncio.create_subprocess_shell(
                    cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
                )
                stdout, stderr = await process.communicate()
                er = stderr.decode()
                try:
                    if er:
                        await e.edit(str(er) + "\n\n**ERROR**")
                        QUEUE.pop(list(QUEUE.keys())[0])
                        os.remove(dl)
                        os.remove(out)
                        continue
                except BaseException:
                    pass
                ees = dt.now()
                ttt = time.time()
                await nn.delete()
                nnn = await e.client.send_message(e.chat_id, "**📤 Uploading...**")
                with open(out, "rb") as f:
                    ok = await upload_file(
                        client=e.client,
                        file=f,
                        name=out,
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(d, t, nnn, ttt, f"**📤 Uploading**\n__{out.replace(f'encode/', '')}__")
                        ),
                    )
                await nnn.delete()
                org = int(Path(dl).stat().st_size)
                com = int(Path(out).stat().st_size)
                pe = 100 - ((com / org) * 100)
                per = str(f"{pe:.2f}") + "%"
                eees = dt.now()
                x = dtime
                xx = ts(int((ees - es).seconds) * 1000)
                xxx = ts(int((eees - ees).seconds) * 1000)
                a1 = await info(dl, e)
                a2 = await info(out, e)
                dk = f"<b>File Name:</b> {newFile}\n\n<b>Original File Size:</b> {hbs(org)}\n<b>Encoded File Size:</b> {hbs(com)}\n<b>Encoded Percentage:</b> {per}\n\n<b>Get Mediainfo Here:</b> <a href='{a1}'>Before</a>/<a href='{a2}'>After</a>\n\n<i>Downloaded in {x}\nEncoded in {xx}\nUploaded in {xxx}</i>"
                ds = await e.client.send_file(
                    e.chat_id, file=ok, force_document=True, caption=dk, link_preview=False, thumb=thum, parse_mode="html"
                )
                QUEUE.pop(list(QUEUE.keys())[0])
                os.remove(dl)
                os.remove(out)
            else:
                await asyncio.sleep(3)
        except Exception as err:
            LOGS.info(err)


########### Start ############

LOGS.info("Bot has started.")
with bot:
    bot.loop.run_until_complete(something())
    bot.loop.run_forever()
