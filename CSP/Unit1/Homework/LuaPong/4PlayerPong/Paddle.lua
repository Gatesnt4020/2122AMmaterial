-- class Paddle: for python
Paddle = Class{}

-- 'init' function or Constructor
-- def __init__(self,x,y,width,height):
    --self.x = x
function Paddle:init(x,y,width,height,type)
    self.x = x
    self.y = y
    self.w = width
    self.h = height
    self.dx = 0
    self.dy = 0
    self.type = type
end

-- Paddle will update and do some updating
function Paddle:update(dt)
    --check to see if we are going up or down
    if self.type == "vert" then        
        if self.dy < 0 then
            self.y = math.max(0, self.y + self.dy * dt)
        else
            self.y = math.min(VIRTUAL_HEIGHT-self.h,self.y + self.dy * dt)
        end
    else
        if self.dx < 0 then
            self.x = math.max(0, self.x + self.dx * dt)
        else
            self.x = math.min(VIRTUAL_WIDTH-self.w,self.x + self.dx * dt)
        end 
    end
end

-- Paddle will need to be drawn or render
function Paddle:render()
    love.graphics.rectangle('fill',self.x,self.y,self.w,self.h)
end