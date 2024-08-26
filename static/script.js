$(document).ready(function (){
    $(".open").click(function (){
        
        $(this).siblings(".pop-outer").fadeIn("fast");
        $("body").addClass("popup-open"); 
    });

    $(".close").click(function (){
        
        $(this).closest(".pop-outer").fadeOut("fast");
        $("body").removeClass("popup-open"); 
    });

    
    $(document).mouseup(function (e) {
        var popup = $(".pop-inner");
        if (!popup.is(e.target) && popup.has(e.target).length === 0) {
            $(".pop-outer").fadeOut("fast");
            $("body").removeClass("popup-open");
        }
    });
	
});


$(document).ready(function (){
    $(".aboutopen").click(function (){
        
        $(this).siblings(".ABOUT-outer").fadeIn("fast");
        $("body").addClass("popup-open"); 
    });

    $(".close").click(function (){
        
        $(this).closest(".ABOUT-outer").fadeOut("fast");
        $("body").removeClass("popup-open"); 
    });

    
    $(document).mouseup(function (e) {
        var popup = $(".ABOUT-inner");
        if (!popup.is(e.target) && popup.has(e.target).length === 0) {
            $(".ABOUT-outer").fadeOut("fast");
            $("body").removeClass("popup-open");
        }
    });
	
});


// funcion para hacer el cambio de fonts cada segudno 
$(document).ready(function (){
    const fonts = [
        "Arial",
        "Cambria",
        "Candara",
        "Century",
        "Lato",
        "Segoe UI",
        "Times New Roman",
        "Georgia"
    ];

    let i = 0;

    function fontchange() {
        document.getElementById('texto').style.fontFamily = fonts[i];
        i = (i + 1) % fonts.length;
    }   

    fontchange();
    setInterval(fontchange, 200);
});




// funcion para hacer el cambio de frases cada 3 segundos
$(document).ready(function (){

	const msjs = [
		"Recolectando videos no listados de Discord...",
		"JSONTube, el peor nombre del universe.",
		"Videos malisimos.",
		"Pense que no volveria a ver ese video.",
		"Has click en el texto que se mueve chistoso.",
		"Creo que esto esta corriendo en una RaspBerry pi 3.",
		"Pagina escrita por un pelotudo.",
		"No he descargado ni un video de aqui."
	];    
    let i = 0;
    function changeText() {
      document.getElementById('mensajito').textContent = msjs[i];
      i = (i + 1) % msjs.length;
    }   
    changeText();
    setInterval(changeText, 3000);

});

