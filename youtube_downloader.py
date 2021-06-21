from selenium import webdriver
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
import pytube
from moviepy.editor import *
import os

def Convertisseur(video_default_name, video_name):
        video = VideoFileClip(os.path.join(folder_case.get()+'/', "", video_default_name))
        video.audio.write_audiofile(os.path.join(folder_case.get()+'/', "", video_name+".mp3"))
        video.close()
        os.remove(folder_case.get()+ '/'+video_default_name)

def playlist_downloader(link, folder, extension):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.set_window_size(1024,800)
        driver.get(link)
        driver.find_element_by_xpath("//div[@class='lssxud']/div[@class='VfPpkd-dgl2Hf-ppHlrf-sM5MNb']/button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc IIdkle']").click()

        videos=driver.find_elements_by_xpath(
                "//div[@id='contents']/ytd-playlist-video-renderer[@class='style-scope ytd-playlist-vdja deo-list-renderer']")

        url = driver.find_elements_by_id("video-title")
        urls = []
        for i in range(len(url)):
                urls.append(url[i].get_attribute("href"))
                link = urls[i]
                lien_vid = pytube.YouTube(link)
                video = lien_vid.streams.get_highest_resolution()
                video.download(folder)
                if extension == 0:
                        Convertisseur(video.default_filename, video.title)
        driver.quit()
        showinfo('Succès du téléchargement', 'Téléchargement réalisé avec succès!')

def video_downloader(link, folder, extension):
            lien_vid = pytube.YouTube(link)
            video = lien_vid.streams.get_highest_resolution()
            video.download(folder)
            if extension == 0:
                    Convertisseur(video.default_filename, video.title)
            showinfo('Succès du téléchargement', 'Téléchargement réalisé avec succès!')

def valid():
        v_or_p = choix.get()
        if v_or_p==0:
                video_downloader(url_case.get(), folder_case.get(), format.get())
        elif v_or_p ==1 :
                playlist_downloader(url_case.get(), folder_case.get(), format.get())

def Recherche():
    download_Directory = filedialog.askdirectory(initialdir="Votre dossier de sauvegarde")
    folder_entry.set(download_Directory)

def playlist_prevention():
        if choix.get() == 1:
                label_plt['text'] = "Attention, votre playlist doit être publique !\nEn clickant sur ' Valider ', vous allez ouvrir le navigateur Chrome!\nQuand Chrome se refermera, le téléchargement des vidéos sera fini!"
                label_plt['bg'] = "#02afff"
        else:
                label_plt['text'] = ""
                label_plt['bg'] = "#FFFFFF"

mainapp = Tk()
mainapp.title("Télécharger des vidéos youtube")  # Titre du programme
mainapp.geometry("600x200")  # Déclaration de la taille de la fenêtre

folder_entry = StringVar()
choix = IntVar()  # Initialisation de la variable "choix"
format = IntVar()

label_bvn = Label(mainapp, text="Bienvenue sur l'outil qui télécharge des vidéos et des playlists YouTube!\n")  # Texte de bienvenue

label_plt = Label(mainapp, text="")

label_url = Label(mainapp, text="adresse url: ")
url_case = Entry(mainapp, width=50)

label_dossier = Label(mainapp, text="dossier de téléchargement: ")
folder_case = Entry(mainapp, width=50, textvariable=folder_entry)
folder_case.insert(END, 'd:/telechargements/e')

folder_button = Button(mainapp, text="Recherche", command=Recherche)

# Choix video ou playlist
choix_widget = Radiobutton(mainapp, text="video", value=0, variable=choix, command = playlist_prevention)
choix_widget2 = Radiobutton(mainapp, text="playlist", value=1, variable=choix, command = playlist_prevention)

mp3_widget = Radiobutton(mainapp, text="mp3", value=0, variable=format)
mp4_widget = Radiobutton(mainapp, text="mp4", value=1, variable=format)

mainapp.bind_class('Entry', '<Return>', valid)
btn_valid = Button(mainapp, text="valider", command=valid)


# Arrangement des objects Tkinter (Grille)
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