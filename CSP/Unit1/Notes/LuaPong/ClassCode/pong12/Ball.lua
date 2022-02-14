Ball = Class()
function Ball:init(x,y)
    self.x = x
    self.y = y
    self.dx = math.random(2) == 1 and 100 or -100
    self.dy = math.random(-50,50)
end
function Ball:update(dt)
    self.y = self.y+self.dy*dt
    self.x = self.x+self.dx*dt
end
function Ball:reset()
    self.x = VIRTUAL_WIDTH/2 - 2
    self.y = VIRTUAL_HEIGHT/2 - 2
    self.dx = math.random(2) == 1 and 100 or -100
    self.dy = math.random(-50,50)
end
function Ball:render()
    love.graphics.rectangle("fill",self.x,self.y,4,4)
end
function Ball:collide(pad)
   --check to see if left edge of ball is farther to the right
   --check the right edge of the other
   --check horizontally we've collected
   if self.x >pad.x + pad.w or pad.x > self.x + 4 then
       return false
   end
   --check vertically if we've collided
   if self.y > pad.y + pad.h or pad.y > self.y + 4 then
      return false 
   end
   return true
end
function Ball:bounce()
    if self.y < 0 then
        self.y = self.y + 5
        self.dy = -self.dy
        sounds['wall_hit']:play()
    elseif self.y > VIRTUAL_HEIGHT then
    self.y = self.y - 5
    self.dy = -self.dy
    sounds['wall_hit']:play()
    end
end