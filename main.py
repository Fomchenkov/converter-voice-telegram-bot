#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import telebot

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command_handler(message):
	text = "Just send an audio message and i'll resend you as a voice message"
	bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['audio'])
def audio_handler(message):
	file_info = bot.get_file(message.audio.file_id)
	#print(f"message.audio.file_id: {message.audio.file_id}\nfile_info: {file_info}\n\n")
	downloaded_file = bot.download_file(file_info.file_path)
	#print(f"file_info.file_path: {file_info.file_path}\n")
	bot.send_voice(message.chat.id, downloaded_file)

bot.infinity_polling()
