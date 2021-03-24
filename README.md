# Python-Challenge

My attempts at the challenges from www.pythonchallenge.com

I am making each challenge its own module for ease of access

Challenge 1:

My first idea was to use the ord() function and do ascii level changes to convert back to chr, it worked but it wasn't very efficient. I then followed the recommendation to use the .maketrans function, then generalised it to any input shift.

Challenge 2:

I started off by making a method to differentiate between new and repeated characters, I then used that to determine whether to ammend or delete a character from the 'Unique' string. For some reason python doesn't have a funciton to remove an individual character so I had to find an appropriate proxy for it, I ended up using a dictionary method like last time to shift the value from containing a letter to containing nothing.
