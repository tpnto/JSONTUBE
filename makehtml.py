HTMLstart = '''
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{{ url_for('static', filename='diseno.css') }}">
    <meta charset="UTF-8">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <title>unlistedvids</title>
    <script src="{{ url_for('static', filename='script.js') }}"></script>
</head>
<body>

 <div class="header">
		
  <h1>JSONTube</h1>
  <button class="aboutopen">x</button>
        <div style="display: none;" class="ABOUT-outer">
            <div class="ABOUT-inner">
                <h2>About</h2>
                <p>JSONTube es un compilado de videos ocultos de YouTube que fueron analizados con la ayuda de un programa escrito en python.</p>
                
				<p>Si deseas ver la Metadata de algun video, solamente presiona sobre el, de ahi saldra cualquier informacion que se encontro dentro de el JSON.</p>
				<p>Si quieres ver si el video esta disponible en archive.org, presiona sobre "Archive", te redirijira a un sitio de archive.org en donde se guardan los videos de manera directa. AKA: "https://web.archive.org/web/2oe_/http://wayback-fakeurl.archive.org/yt/[id del video]"</p>
				
				<h3 style=font-size:16px;>Sobre el Autor: </h3>
                <a  href="https://github.com/tpnto" target="_blank"><img id="fotito" src="{{ url_for('static', filename='autor.png') }}" alt="el gran autor de esta mierda mal escrita" style="width:128px;height:128px;"></img></a>
				<p id="mensaje"><--- el ql imbecil que escribio esto<p>
            </div>
        </div>
	</div> 


<body>
	
  <span id="mensajito" class="textodinamico"></span>
  <script>
    
	const msjs = [
		"Recolectando videos no listados de Discord...",
		"JSONTube, esta bueno el nombre no?",
		"oohh ese video! si, si lo recuerdo!",
		"Pense que no volveria a ver ese video",
		"Has click en el texto que se mueve chistoso",
		"Creo que esto esta corriendo en una RaspBerry pi 3",
		"Pagina escrita por un pelotudo",
		"No he descargado ni un video de aqui"
	];    
    let index = 0;
    function changeText() {
      document.getElementById('mensajito').textContent = msjs[index];
      index = (index + 1) % msjs.length;
    }   
    changeText();
    setInterval(changeText, 3000);
  </script>

  
</body>

<div class="videoblock">
'''

HTMLend = '''
</div>
</body>
</html>
'''

def vid2HTML(file, vidid, titulo, vidstatus, descripcion, autor, userID):
    escribiraHTML = f'''
    <div class="video">
        <p><a href="https://www.youtube.com/watch?v={vidid}" target="_blank">
            <img src="https://i.ytimg.com/vi/{vidid}/hqdefault.jpg" alt="miniatura" width="480" height="360"></a></p>
        <p class=titulo>{titulo}</p>
        <p>Estatus: {vidstatus}</p>
        <button class="open">Metadata</button>
        <div style="display: none;" class="pop-outer">
            <div class="pop-inner">
                <h2>Metadata</h2>
                <p>Titulo: {titulo}</p>
                <p>Descripcion: {descripcion}</p>
                <p>VideoID: {vidid}</p>
                <p><a href="{userID}" target="_blank"> Autor: {autor}</a></p>
                <p><a href="https://web.archive.org/web/2oe_/http://wayback-fakeurl.archive.org/yt/{vidid}" target="_blank">Archive.org</p></a>
            </div>
        </div>
    </div>
    '''
    file.write(escribiraHTML)
    
def HTMLintro(file):
    file.write(HTMLstart)


def HTMLoutro(file):
    file.write(HTMLend)
