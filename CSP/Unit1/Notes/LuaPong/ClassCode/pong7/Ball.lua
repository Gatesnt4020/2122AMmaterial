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

function Ball:collides(paddle)
    --first check to see if the left edge or either is farther to right
    --than the right edge of the other
    --check horizontally we've collided
    if self.x > paddle.x + paddle.w or paddle.x> self.x +self.w then
        return false
    end
    --check vertically if we've collided
    if self.y > paddle.y + paddle.h or paddle.y > self.y + self.w then
        return false
    end

    --if self.x >

    return true -- if neither of the ones above are true, then we have collision
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