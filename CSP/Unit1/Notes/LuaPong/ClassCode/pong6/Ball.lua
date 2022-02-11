Ball = Class{}

function Ball:init(x,y,width,height)
    self.x = x 
    self.y = y
    self.w = width
    self.h = height
    self.Dx = math.random(2) == 1 and 100 or -100
    self.Dy = math.random(50,-50)
end

function Ball:update(dt)
    self.x = self.x + self.Dx *dt
    self.y = self.y + self.Dy *dt
end

function Ball:reset()
    self.x = VIRTUAL_WIDTH/2-2
    self.y = VIRTUAL_HEIGHT/2-2
    self.Dx = math.random(2) == 1 and 100 or -100
    self.Dy = math.random(50,-50)
end

function Ball:render()
    love.graphics.rectangle('fill',self.x,self.y,self.w,self.h)
end