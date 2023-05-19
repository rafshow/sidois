function tocaSom(seletorAudio) {
    const audio = new Audio(seletorAudio);
    audio.play();
  }
  
  const listadeTeclas = document.querySelectorAll('.image-button');
  
  for (let i = 0; i < listadeTeclas.length; i++) {
    const tecla = listadeTeclas[i];
    
    tecla.onclick = function(event) {
      
      tocaSom('./static/assets/barulho urna.mp3');
      console.log('Obrigado por ter votado!');
    }
    
  }

