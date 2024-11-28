function createStarField() { 
  const starField = document.createElement('div'); 
  
  starField.className = 'star-field'; 
  document.body.appendChild(starField); 
  for (let i = 0; i < 100; i++) { 
    const star = document.createElement('div')
    star.style.position = 'absolute' 
    star.style.width = '2px' 
    star.style.height = '2px'
    star.style.background = '#fff'
    star.style.top = `${Math.random() * 100}vh`
    star.style.left = `${Math.random() * 100}vw` 
    starField.appendChild(star)
  } 
} 

createStarField()
