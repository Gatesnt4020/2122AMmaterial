--var = import or require the file 'push'
push = require 'push'

PADDLE_SPEED = 250


WINDOW_WIDTH=1280
WINDOW_HEIGHT=720

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

--A function to start up the window that initialzes the game
function love.load()
     math.randomseed(os.time())
     --use nearest-neighbor filteing on upscaling and downscaling to prevent blurry
     love.graphics.setDefaultFilter('nearest','nearest')

     --var = love's grapics module.newFont('file',fontsize)
     smallFont = love.graphics.newFont('font.ttf',8)
     scoreFont = love.graphics.newFont('font.ttf',32)
     --set font for love
     love.graphics.setFont(smallFont)
     --this method changes the screen to our virtual resolution
     push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
          fullscreen=false,
          resizable=false,
          vsync=true
     })
     player1Y = VIRTUAL_HEIGHT / 2 - 10
     player2Y = VIRTUAL_HEIGHT / 2 - 10

     player1Score = 0
     player2Score = 0

     ballx = VIRTUAL_WIDTH/2-2
     bally = VIRTUAL_HEIGHT/2-2

     --determining a random dx and dy to move the ball
     ballDx = math.random(2) == 1 and 500 or -500
     ballDy = math.random(-500,500)

     gameState = 'start'
end

--this function is ran every frame, pass in dt
--dt is delta time or change in seconds since last frame
function love.update(dt)

     --ball movement
     if gameState == 'play' then
          --scale the velocity by dt so movement is framerate-independent
          ballx = ballx + ballDx * dt
          bally = bally + ballDy * dt          
     end
     if ballDx == -500 then
          if player1Y < bally then
               player1Y = player1Y + PADDLE_SPEED * dt
          elseif player1Y > bally then
               player1Y = player1Y + -PADDLE_SPEED * dt
          end
     end
     if ballDx == 500 then
          if player2Y < bally then
               player2Y = player2Y + PADDLE_SPEED * dt
          elseif player2Y > bally then
               player2Y = player2Y + -PADDLE_SPEED * dt
          end
     end


end

function love.keypressed(key)
     --keys can be access by string name
     if key=='escape' then
          love.event.quit() -- this will close the window
     elseif key == 'enter' or key == 'return' then
          if gameState == 'start' then
               gameState = 'play'
          elseif gameState == 'play' then
               gameState = 'start'
          end
     end
end
--draw on the screen the letters
--update the screen with information:  draw anything that is needed

function love.draw()
     --begin rendering at a virtual resolution
     push:apply('start')

     --clear the screen and reset the background color
     --love.graphics.clear(r,g,b,a)



     love.graphics.clear(40,45,52,255)
     love.graphics.setFont(smallFont)
     if gameState == 'start' then
          love.graphics.printf('Hello Start State!',0,20,VIRTUAL_WIDTH,'center')
     else
          love.graphics.printf('Hello Play State!',0,20,VIRTUAL_WIDTH,'center')
     end

     love.graphics.setFont(scoreFont)
     love.graphics.print(tostring(player1Score),VIRTUAL_WIDTH/2-70,VIRTUAL_HEIGHT-190)
     love.graphics.print(tostring(player2Score),VIRTUAL_WIDTH/2+50,VIRTUAL_HEIGHT-190)

     --draw our paddles

     --love.graphics.rectangle('filled or not', startx.starty.endx.endy)
     -- check if Y is too high or low
     if player1Y < 0 then
          player1Y = 0
     else
          love.graphics.rectangle('fill',10,player1Y,5,20)          
     end

     if player1Y > VIRTUAL_HEIGHT-20 then
          love.graphics.rectangle('fill',10,VIRTUAL_HEIGHT-20,5,20)
          player1Y = VIRTUAL_HEIGHT-20
     else
          love.graphics.rectangle('fill',10,player1Y,5,20)          
     end


     if player2Y < 0 then
          player2Y = 0
     else
          love.graphics.rectangle('fill',417,player2Y,5,20)          
     end

     if player2Y > VIRTUAL_HEIGHT-20 then
          love.graphics.rectangle('fill',417,VIRTUAL_HEIGHT-20,5,20)     
          player2Y = VIRTUAL_HEIGHT-20
     else
          love.graphics.rectangle('fill',417,player2Y,5,20)          
     end

     love.graphics.rectangle('fill',ballx,bally,4,4)

     if ballx < 0 then
          ballx = VIRTUAL_WIDTH/2-2
          bally = VIRTUAL_HEIGHT/2-2
          ballDx = math.random(2) == 1 and 500 or -500
          ballDy = math.random(-500,500)
          player2Score = player2Score + 1
     elseif ballx > VIRTUAL_WIDTH-4 then
          ballx = VIRTUAL_WIDTH/2-2
          bally = VIRTUAL_HEIGHT/2-2
          ballDx = math.random(2) == 1 and 500 or -500
          ballDy = math.random(-500,500)
          player1Score = player1Score + 1
     end

     if bally - player1Y < 20 and bally - player1Y > -5 then
          if ballx < 14 then
               ballDx = 500
               ballDy = math.random(-500,500)      
          end
     end

     if bally - player2Y < 20 and bally - player2Y > -5 then
          if ballx > 414 then
               ballDx = -500
               ballDy = math.random(-500,500)      
          end
     end

     if bally < 0 then
          ballDy = math.random(0,250)
     elseif bally > 239 then
          ballDy = math.random(-250,0)
     end







     love.graphics.print(tostring(player1Score),VIRTUAL_WIDTH/2-70,VIRTUAL_HEIGHT-190)
     love.graphics.print(tostring(player2Score),VIRTUAL_WIDTH/2+50,VIRTUAL_HEIGHT-190)


     displayFPS()


     --end virtual resolution?
     push:apply('end')
end

function displayFPS()
     love.graphics.setFont(smallFont)
     love.graphics.setColor(0,255,0,255)
     love.graphics.print('FPS: ' .. tostring(love.timer.getFPS()),10,10)
end