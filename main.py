import os
import re

# Chemin du répertoire contenant les fichiers musicaux
chemin_repertoire = "../The_file_path_for_the_music_files_to_be_modified"

# motifs à rechercher dans les noms dans playlists
motifs_a_supprimer = [
    r'\[Bonne qualité\]',
    r'\(official video\)',
    r'\(official music video\)',
    r'\(official lyrics video\)',
    r'\(official_music_video\)',
    r'\(128k\)',
    r'\(256k\)',
    r'\(256kbps\)',
    r'\(Video lyrics\)',
    r'\(official 4k music video\)',
    r'\(Tonon_kira Video\)',
    r'\(VIDEO COMPILATION\)',
    r'\(720p\)',
    r'\(Lyric-Video\)',
    r'\(360p)',
    r'\(CLIP VIDEO\)',
    r'\(Official video 2021\)',
    r'\(Official video 2022\)',
    r'\(Video Oficial\)',
    r'\(Official_Lyrics_Video\)',
    r'\(Clip Officiel\)',
    r'\[Clip OFFICIEL\]',
    r'\(official clip \)',
    r'\(Clip_officiel\)',
    r'\(Clip\)',
    r'\(clip officiel \)',
    r'\(Official video music\)',
    # autres motifs
]

for nom_fichier in os.listdir(chemin_repertoire):
    chemin_complet = os.path.join(chemin_repertoire, nom_fichier)

    # Vérification  du fichier
    if os.path.isfile(chemin_complet):
        for motif in motifs_a_supprimer:
            try:
                nom_fichier = re.sub(motif, '', nom_fichier, flags=re.IGNORECASE).strip()
            except re.error as e:
                print(f"Erreur dans le repertoire : '{motif}': {e}")
                continue

        # modification avant et apres
        print(f"Avant : {os.path.basename(chemin_complet)}")
        print(f"Après : {nom_fichier}")

        # Renommer le fichier
        nouvel_chemin_complet = os.path.join(chemin_repertoire, nom_fichier)
        os.rename(chemin_complet, nouvel_chemin_complet)

print("Renommage des fichiers terminé")