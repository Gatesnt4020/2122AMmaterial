--var = import require the file 'push' 
push = require 'push'

WINDOW_WIDTH=1280
WINDOW_HEIGHT=720

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

--A function to start up the window that initialzes the game
function love.load()
    -- use nearest-neighbor filtering on upscaling and downscaling to prevent blurry
    love.graphics.setDefaultFilter('nearest','nearest')

    -- var = love's graphics module.newFont('file',fontsize)
    smallFont= love.graphics.newFont('font.ttf',8)
    --set font for love
    love.graphics.setFont(smallFont)

    --this method changes the screen to out virtual resolution
    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
        fullscreen=false,
        resizable=false,
        vsync=true
    })
end

--Check for any keypressing
function love.keypressed(key)
    if key =='escape' then 
        love.event.quit()   --this will close the window
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


    love.graphics.printf('Hello Pong!',0,20,VIRTUAL_WIDTH,'center')


    -- Draw the paddles and the ball


    --love.graphics.rectangle('filled or not' ,x,y,width,height)
    -- render first paddle()
    love.graphics.rectangle('fill',10,30,5,20)
    
    -- render second paddle (right side)
    love.graphics.rectangle('fill',VIRTUAL_WIDTH-10,VIRTUAL_HEIGHT-50,5,20)
    
    -- render ball (center)
    love.graphics.rectangle('fill',VIRTUAL_WIDTH/2-2,VIRTUAL_HEIGHT/2-2,4,4)

    --end virtual resolution
    push:apply('end')
end