def Captionfunc(update, context):
    if update.message.reply_to_message is not None:
        fileCaption = update.message.text
        fileType = update.message.reply_to_message
        if fileType.document != None:
            update.message.reply_document(
                update.message.reply_to_message.document.file_id, caption=fileCaption)
        elif fileType.video != None:
            update.message.reply_video(
                update.message.reply_to_message.video.file_id, caption=fileCaption)
        elif fileType.audio != None:
            update.message.reply_audio(
                update.message.reply_to_message.audio.file_id, caption=fileCaption)
        elif fileType.voice != None:
            update.message.reply_voice(
                update.message.reply_to_message.voice.file_id, caption=fileCaption)
        elif fileType.photo != None:
            update.message.reply_photo(
                update.message.reply_to_message.photo[-1].file_id, caption=fileCaption)
    else:
        update.message.reply_text(update.message.text)


def Filefunc(update, context):
    try:
        update.message.reply_document(update.message.document.file_id)
    except Exception as e:
        update.message.reply_text("Something went wrong.. ref: ", e)


def Mediafunc(update, context):
    try:
        update.message.reply_video(update.message.video.file_id)
    except Exception as e:
        update.message.reply_text("Something went wrong... ref: ", e)


def Photofunc(update, context):
    try:
        update.message.reply_photo(update.message.photo[-1].file_id)
    except Exception as e:
        update.message.reply_text("Something went Wrong... ref: ", e)


def Stickerfunc(update, context):
    try:
        update.message.reply_sticker(update.message.sticker.file_id)
    except Exception as e:
        update.message.reply_text("Something wrong..", e)


def Voicefunc(update, context):
    try:
        update.message.reply_voice(update.message.voice.file_id)
    except Exception as e:
        update.message.reply_voice("Something Went... ", e)


def Audiofunc(update, context):
    try:
        update.message.reply_audio(update.message.audio.file_id)
    except Exception as e:
        update.message.reply_text(e)


# disPatch.add_handler(MessageHandler(Filters.audio, Audiofunc))
