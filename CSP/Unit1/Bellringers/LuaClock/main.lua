WINDOW_WIDTH=1280
WINDOW_HEIGHT=720
time = 0

function love.load()
    scoreFont = love.graphics.newFont('font.ttf',32)
    love.window.setMode(WINDOW_WIDTH,WINDOW_HEIGHT,{
        fullscreen = false,
        resizable = false,
        vsync = true
    })
end

function love.update(dt)
    time = os.date('%H:%M:%S')
end

function love.draw()
    love.graphics.setFont(scoreFont)
    love.graphics.printf(
        time,      --text to render
        0,                   --starting X
        WINDOW_HEIGHT/2,     --starting Y
        WINDOW_WIDTH,        --number of pixels to center within
        'center'             --alignment                    
    )
end