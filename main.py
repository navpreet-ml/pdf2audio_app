from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import os
import pdfplumber
from gtts import gTTS

FONT_NAME = "Courier"
all_text = ""
files_location = ""
filename = ""


def UploadAction(event=None):
    global all_text
    global files_location
    global filename
    filename = filedialog.askopenfilename()
    pdf_label.config(text = os.path.basename(filename))
    files_location = os.path.basename(filename)
    with open(filename, 'rb') as pdf_file:
        pdf_text_all_pages = pdfplumber.open(pdf_file)
        for i in range(len(pdf_text_all_pages.pages)):
            all_text += pdf_text_all_pages.pages[i].extract_text()
    pdf_file.close()
    return all_text


def text_to_speech():
    global all_text, files_location, filename
    tts = gTTS(all_text)
    tts.save("%s.mp3" % os.path.join(files_location, filename))
    audio_label.config(text = "Conversion Completed")


window = Tk()

window.title("Audio Book Generator")
window.config(padx=10, pady=10)

title_label = Label(text="PDF to Audio Converter", fg="#B83B5E", font=(FONT_NAME, 20))
title_label.grid(column=1, row=0)

pdf_label = Label(text="")
pdf_label.grid(row=1, column=0)

audio_label = Label(text="")
audio_label.grid(row=1, column=2)

progress_label = Label(text="Audio file will be saved in the same directory as the PDF file")
progress_label.grid(row=1, column=1)

upload_pdf_btn = Button(text="Upload PDF", width = 20, command=UploadAction, highlightthickness=0)
upload_pdf_btn.grid(column=0, row=2, sticky="EW", padx=10, pady=10)

download_audio_btn = Button(text="Download Audio", width = 20, command=text_to_speech, highlightthickness=0)
download_audio_btn.grid(column=2, row=2, sticky="EW", padx=10, pady=10)

window.mainloop()





