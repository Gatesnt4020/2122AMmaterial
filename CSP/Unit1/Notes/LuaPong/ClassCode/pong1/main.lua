WINDOW_WIDTH=1280
WINDOW_HEIGHT=720

--A function to start up the window that initialzes the game
function love.load()
    love.window.setMode(WINDOW_WIDTH,WINDOW_HEIGHT,{
        fullscreen = false,
        resizable = false,
        vsync = true
    })
end

--draw on the screen the letters
--update the screen with information:  draw anythong that is needed
function love.draw()
    love.graphics.printf(
        'Hello World!',      --text to render
        0,                   --starting X
        WINDOW_HEIGHT/2,     --starting Y
        WINDOW_WIDTH,        --number of pixels to center within
        'center'             --alignment                    
    )
end