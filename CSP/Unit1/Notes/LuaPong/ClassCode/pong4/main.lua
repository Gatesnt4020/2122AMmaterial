--var = import require the file 'push' 
push = require 'push'

WINDOW_WIDTH=1280
WINDOW_HEIGHT=720

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

PADDLE_SPEED = 200

--A function to start up the window that initialzes the game
function love.load()
    
    --"seed" the RNG so that calls to random are always random
    -- use the current time, since that will vary on startup every time
    math.randomseed(os.time())
    -- use nearest-neighbor filtering on upscaling and downscaling to prevent blurry
    love.graphics.setDefaultFilter('nearest','nearest')

    -- var = love's graphics module.newFont('file',fontsize)
    smallFont= love.graphics.newFont('font.ttf',8)
    scoreFont = love.graphics.newFont('font.ttf',32)

    --this method changes the screen to out virtual resolution
    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
        fullscreen=false,
        resizable=false,
        vsync=true
    })

    player1Score=0
    player2Score=0

    player1Y = 30
    player2Y = VIRTUAL_HEIGHT-50

    ballx = VIRTUAL_WIDTH/2-2
    bally = VIRTUAL_HEIGHT/2-2

    --determining a radnom dx and dy to move the ball
    ballDx = math.random(2) == 1 and 100 or -100
    ballDy = math.random(50,-50)

    --this var will help determine what is going on in the game
    --in the beginning, menu, main game, high score, etc
    gameState = 'start'

end

--this f(x) is ran every frame, pass in dt.
--dt is delta time or change in seconds since the last frame
function love.update(dt)
    --player 1 movement
    if love.keyboard.isDown('w') then
        -- move up by add a negative paddle speed to the y scaled by dt
        player1Y = player1Y + -PADDLE_SPEED * dt
    elseif love.keyboard.isDown('s') then
        -- move up by add a negative paddle speed to the y scaled by dt
        player1Y = player1Y + PADDLE_SPEED * dt
    end
    
    --player 2 movement
    if love.keyboard.isDown('up') then
        -- move up by add a negative paddle speed to the y scaled by dt
        player2Y = player2Y + -PADDLE_SPEED * dt
    elseif love.keyboard.isDown('down') then
        -- move up by add a negative paddle speed to the y scaled by dt
        player2Y = player2Y + PADDLE_SPEED * dt
    end

    --ball movement
    if gameState == 'play' then 
        --scale the velocity by dt so movement is framerate-independent
        ballx = ballx + ballDx *dt
        bally = bally + ballDy *dt
    end

end

--Check for any keypressing
function love.keypressed(key)
    if key =='escape' then 
        love.event.quit()   --this will close the window
    elseif key == 'enter' or key == 'return' then
        if gameState == 'start' then 
            gameState='play'
        else
            gameState='start'
            ballx = VIRTUAL_WIDTH/2-2
            bally = VIRTUAL_HEIGHT/2-2
            --and/or pattern here is Lua's way of accomplishing a ternary operation
            --very common in other programming languages like C
            ballDx = math.random(2) == 1 and 100 or -100
            ballDy = math.random(50,-50)
        end
    end
end

--draw on the screen the letters
--update the screen with information:  draw anythong that is needed
function love.draw()
    --begin redering at a virtual resolution
    push:apply('start')

    --clear the screen and reset the background color
    --love.graphics.clear(r,g,b,a)
    love.graphics.clear(40,45,52,255)
    --set font for love
    love.graphics.setFont(smallFont)

    if gameState == 'start' then
        love.graphics.printf('Hello Start State!',0,20,VIRTUAL_WIDTH,'center')
    else
        love.graphics.printf('Hello Play State!',0,20,VIRTUAL_WIDTH,'center')
    end

    love.graphics.setFont(scoreFont)
    love.graphics.print(tostring(player1Score),VIRTUAL_WIDTH/2-50,VIRTUAL_HEIGHT/3)
    love.graphics.print(tostring(player2Score),VIRTUAL_WIDTH/2+50,VIRTUAL_HEIGHT/3)

    -- Draw the paddles and the ball


    --love.graphics.rectangle('filled or not' ,x,y,width,height)
    -- render first paddle()
    love.graphics.rectangle('fill',10,player1Y,5,20)
    
    -- render second paddle (right side)
    love.graphics.rectangle('fill',VIRTUAL_WIDTH-10,player2Y,5,20)
    
    -- render ball (center)
    love.graphics.rectangle('fill',ballx,bally,4,4)
    
    

    --end virtual resolution
    push:apply('end')
end