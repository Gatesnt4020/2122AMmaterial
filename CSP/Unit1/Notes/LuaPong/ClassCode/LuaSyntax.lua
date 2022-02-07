-- comments
--[[
    Multi
        Line
        Comments
]]
hello = 'hello'         --global
num = 0

-- local var for this file
local world = 'world!'

-- Functions
function say(text)
    print(text)\
end
say(hello .. world)       -- .. is concatenation

-- concatenation in python is the +
--[[
        def say(text):
        print(text)

    function say(text){
        console.log(text)
    }
]]

-- conditionals!
if world == 'world' then
    print('world!')
else
    print('hello!')
end

--while loop
local i = 10
while i>0 do
    i = i-1     ----notice the lack of -= and +=
    print(i)
end

--for loop
for j=10,0,-1 do
    print(j)
end

--repeat (do-while) loop
i = 10
repeat
    i=i-1
    print(i)
until i==0

-- Tables
-- Glorified list where instead of an index number, you use keys
-- Java and C call this Hash Map
-- Python calls it a Dictionary
local person = {}
person.name = "Bander"
person.age = 75
person.height = 7.0

print(person['name'])

-- iterate trhough a table
for key,value in pairs(person) do 
    print(key,value)            --print out "name" "bander"
end