let text = document.querySelector('.text')

let htmlSpans = text.innerText.split('').map((letter, i) => {
  return `
    <span 
     style='animation-duration: ${Math.random() * 5};
            filter: hue-rotate(${i * 50}deg;'
    >
      ${letter}
    </span>
  `
}).join('')

text.innerHTML = htmlSpans