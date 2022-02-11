Paddle = Class{}

function Paddle:init(x,y,width,height)
    self.x=x
    self.y=y
    self.w=width
    self.h=height
    self.dy=0
end

--Paddle will update and do some updating
function Paddle:update(dt)
    if self.dy<0 then
        self.y = math.max(0,self.y + self.dy * dt) -- add means down
    else
        self.y = math.min(VIRTUAL_HEIGHT-self.h,self.y - self.dy * dt) -- subtract means up
    end
end

--Paddle will need to be drawn or render
function Paddle:render()
    love.graphics.rectangle('fill',self.x,self.y,self.w,self.h)