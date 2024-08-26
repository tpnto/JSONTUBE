import re
import urllib.parse
import json
import googleapiclient.discovery

class UPP:
    # Forced OOP B)
    def __init__(self, api_key):
        self.__api_key = api_key
        self.__service = "youtube"
        self.__version = "v3"
        self.youtube = googleapiclient.discovery.build(self.__service, self.__version, developerKey=self.__api_key)
    
    def extraerID(self, url):
        # extraer la ID de una URL de un video de youtube/youtu.be/shorts etc...
        url_data = urllib.parse.urlparse(url)
        # asignemos la variable a NADA PORQ NO HAY NADA.
        video_id = None
        
        if "shorts" in url_data.path:
            video_id = url_data.path.split("/")[-1]
        elif "youtu.be/" in url:
            video_id = url_data.path.lstrip('/')
        elif "youtube.com" in url:
            query = urllib.parse.parse_qs(url_data.query)
            if 'v' in query:
                video_id = query['v'][0]
        
        return video_id
        
    def vidstatus(self, url):
        
        self.video = url
        request = self.youtube.videos().list(
                    part='status',
                    id=url
                )
        try:
            response = request.execute()
            items = response.get('items', [])
            
            if not items:
                print(f"No se ha encontrado informacion sobre el estado actual de: {url}\n")
                return "Privado / Eliminado"
            
            status = items[0]['status']['privacyStatus']
            
            if status == "unlisted":
                print(f"status: {status}\n")
                return status
         
        except Exception as error:
            return None
            