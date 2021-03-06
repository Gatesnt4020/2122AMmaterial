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

    love.graphics.printf(
        'Hello Pong!',      --text to render
        0,                   --starting X
        VIRTUAL_HEIGHT/2,     --starting Y
        VIRTUAL_WIDTH,        --number of pixels to center within
        'center'             --alignment                    
    )

    --end virtual resolution
    push:apply('end')
end