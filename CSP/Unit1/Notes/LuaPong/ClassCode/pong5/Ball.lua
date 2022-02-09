Ball = Class{}

function Ball:init(x,y)
    self.x = x 
    self.y = y
    self.h = height
    self.w = width
    self.Dx = math.random(2) == 1 and 100 or -100
    self.Dy = math.random(50,-50)
end

function Ball:update(dt)
    self.x = self.x + self.Dx *dt
    self.y = self.y + self.Dy *dt
end

function Ball:render()
    love.graphics.rectange('fill',self.x,self.y,self.w,self.h)