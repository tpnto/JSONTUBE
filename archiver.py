import json
import re
from status import UPP
import makehtml
import os



api_key = open("ytapi.txt", "r").read()
upp = UPP(api_key)



def JSONproc(archivo, output_filename):
    # abrimos el JSON
    with open(archivo, "r", encoding="utf-8") as f:
        data = json.load(f)


    messages = data["messages"]
    output_filepath = os.path.join('templates', output_filename)
    with open(output_filepath, 'w', encoding='utf-8') as w:
        # empezamos a escribir nuestro HTML
        makehtml.HTMLintro(w) 
        
        # para mantener IDs unicas en nuestra lista
        lista_de_videos = set()
        # for a traves de todos los mensajes
        for message in messages:
            # busquemos cada URL que esta en el JSON. Messages -> content
            content = message.get("content", "")
            # Si alguna de estas URLs coinciden con lo que esta en content
            if "youtube.com" in content or "youtu.be" in content or "youtube.co" in content or "yt.be" in content:
                # Empecemos a recolectar todas las URLS
                videoID = re.findall(r'(https?://[^\s]+)', content)
                # para cada url en video ID
                for i in videoID:
                    # extraigamos la ID del video con la funcion en status.py
                    video_id = upp.extraerID(i)
                    # Si la ID del video es unica, procesamos el estatus del video y añademos el video a la lista
                    if video_id and video_id not in lista_de_videos:
                        status = upp.vidstatus(video_id)
                        if status:
                            lista_de_videos.add(video_id)  
                            # Si, el mensaje tiene embeds dentro del mensaje
                            # Osease metadata como titulo, descripcion, author etc
                            if "embeds" in message:
                                embeds = message["embeds"]
                                # Hay que iterar dentro del embed a sacar toda la metadata
                                # dentro del mensaje.
                                for j in embeds:
                                    if "title" in j:
                                        title = j["title"]
                                        description = j.get("description", "")
                                        authorvars = j.get("author", {})
                                        author = authorvars.get("name", "")
                                        channelID = authorvars.get("url", "")
                                        makehtml.vid2HTML(w, vidid=video_id, titulo=title, vidstatus=status, descripcion=description, autor=author, userID=channelID)
                                        
                                        # Salgamos del for una vez que ya este todo procesado y escrito
                                        break
                            
        makehtml.HTMLoutro(w)
    w.close()