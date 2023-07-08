from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
import pytube
from moviepy.editor import *
import os



def Converter(video_default_name):
        """
        transform a video mp4 in a audio file mp3
        Use os and
        :param video_default_filename:
        :param video-title:
        :return:
        """
        name_mp3 = video_default_name.replace('.mp4','.mp3')

        print("Convert: ", video_default_name)
        print("Name of the file: ", name_mp3)
        video = VideoFileClip(os.path.join(folder_case.get()+'/', "", video_default_name))
        video.audio.write_audiofile(os.path.join(folder_case.get()+'/', "", name_mp3))
        video.close()
        os.remove(folder_case.get()+ '/'+video_default_name)

def PlaylistDownloader(link, folder, extension):
        """
        Download all videos from a public youtube playlist
        Use pytube and Converter (the first function of this file)
        :param link:
        :param folder:
        :param extension:
        :return:
        """

        playlist = pytube.Playlist(link)
        for video in playlist.videos:
                print("Downloading: ", video.title)
                vid_d = video.streams.get_highest_resolution()
                vid_d.download(folder)
                if extension == 0:
                        Converter(vid_d.default_filename)
        showinfo('Succès du téléchargement', 'Téléchargement réalisé avec succès!')

def VideoDownloader(link, folder, extension):
        """
        Download video/audio from a youtube video
        :param link:
        :param folder:
        :param extension:
        :return:
        """
        lien_vid = pytube.YouTube(link)
        video = lien_vid.streams.get_highest_resolution()
        print("Downloading: ", video.title)
        video.download(folder)
        if extension == 0:
                Converter(video.default_filename)
        showinfo('Succès du téléchargement', 'Téléchargement réalisé avec succès!')

def Valid():
        """
        Function for the valid button, lauch the right function
        :return:
        """
        v_or_p = choix.get()
        if v_or_p==0:
                VideoDownloader(url_case.get(), folder_case.get(), format.get())
        elif v_or_p ==1 :
                PlaylistDownloader(url_case.get(), folder_case.get(), format.get())

def Search():
        """
        Function for the search button to have the right file directory
        :return:
        """
        download_Directory = filedialog.askdirectory(initialdir="Votre dossier de sauvegarde")
        folder_entry.set(download_Directory)

def PlaylistPrevention():
        """
        Print a label on the screen when we click on "playlist"
        :return:
        """
        if choix.get() == 1:
                label_plt['text'] = "Attention, votre playlist doit être publique !"
                label_plt['bg'] = "#02afff"
        else:
                label_plt['text'] = ""
                label_plt['bg'] = "#FFFFFF"

mainapp = Tk() # create the window
mainapp.title("Télécharger des vidéos youtube")  # title of the programm
mainapp.geometry("600x200")  # size of the window

# Initialisation of the variables
folder_entry = StringVar()
choix = IntVar()
format = IntVar()

# creation of the labels and Entry
label_bvn = Label(mainapp, text="Bienvenue sur l'outil qui télécharge des vidéos et des playlists YouTube!\n")  # Texte de bienvenue
label_plt = Label(mainapp, text="")

label_url = Label(mainapp, text="adresse url: ")
url_case = Entry(mainapp, width=50)

label_dossier = Label(mainapp, text="dossier de téléchargement: ")
folder_case = Entry(mainapp, width=50, textvariable=folder_entry)

# remove the "#" of the next line and replace "PATH" by you're path to create a default path for the downloads
#folder_case.insert(END, 'PATH')

# Create the buttons
folder_button = Button(mainapp, text="Recherche", command=Search)

choix_widget = Radiobutton(mainapp, text="video", value=0, variable=choix, command = PlaylistPrevention)
choix_widget2 = Radiobutton(mainapp, text="playlist", value=1, variable=choix, command = PlaylistPrevention)

mp3_widget = Radiobutton(mainapp, text="mp3", value=0, variable=format)
mp4_widget = Radiobutton(mainapp, text="mp4", value=1, variable=format)

btn_valid = Button(mainapp, text="valider", command=Valid)

# add the shortcut, when we press Enter it's the same as click on the valid button
mainapp.bind_class('Entry', '<Return>', Valid)

# Put all on the window on the right place
label_bvn.grid(row=0, column=2)
label_url.grid(row=1, column=1)
url_case.grid(row=1, column=2)
label_dossier.grid(row=2, column=1)
folder_case.grid(row=2, column=2)
folder_button.grid(row = 2, column=3)
choix_widget.grid(row=4, column=1)
choix_widget2.grid(row=6, column=1)
mp3_widget.grid(row=4, column=2)
mp4_widget.grid(row=6, column=2)
btn_valid.grid(row=4, column=3)
label_plt.grid(row=8, column=2)

mainapp.mainloop()  # Boucle de Tkinter
