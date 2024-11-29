const paddle = document.getElementById('paddle')
const ball = document.getElementById('ball')
let paddleX = 250
const paddleWidth = 100 
const gameWidth = 600
let ballX = 290
let ballY = 50 
let ballSpeedX = 2 
let ballSpeedY = 2 

document.addEventListener('keydown', (event) => { 
  if (event.key === 'ArrowLeft' && paddleX > 0) { 
    paddleX -= 20; 
  } else if (event.key === 'ArrowRight' && paddleX < gameWidth - paddleWidth) { 
    paddleX += 20; 
  } 
  paddle.style.left = paddleX + 'px' 
})

const updateBall = () => { 
  ballX += ballSpeedX 
  ballY += ballSpeedY
  
  if (ballX <= 0 || ballX >= gameWidth - 20) ballSpeedX = -ballSpeedX 
  if (ballY <= 0) ballSpeedY = -ballSpeedY  
  if (ballY >= 360 && 
      ballX >= paddleX && 
      ballX <= paddleX + paddleWidth
  ) ballSpeedY = -ballSpeedY  
  if (ballY > 400) { 
    alert('Game Over!')
    resetGame()
  } 
  ball.style.left = ballX + 'px' 
  ball.style.top = ballY + 'px' 
} 

const resetGame = () => { 
  ballX = 290; 
  ballY = 50 
  ballSpeedX = 2
  ballSpeedY = 2 
} 

setInterval(updateBall, 20)