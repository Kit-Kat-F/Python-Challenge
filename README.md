# Python-Challenge

My attempts at the challenges from www.pythonchallenge.com

I am making each challenge its own module for ease of access

Challenge 1:

My first idea was to use the ord() function and do ascii level changes to convert back to chr, it worked but it wasn't very efficient. I then followed the recommendation to use the .maketrans function, then generalised it to any input shift.

Challenge 2:

I started off by making a method to differentiate between new and repeated characters, I then used that to determine whether to ammend or delete a character from the 'Unique' string. For some reason python doesn't have a funciton to remove an individual character so I had to find an appropriate proxy for it, I ended up using a dictionary method like last time to shift the value from containing a letter to containing nothing.

Challenge 3:

This one took me a moment to figure out what was going on, but my shortcomings were rooted in not understanding the hint rather than not doing the right thing. I had developed the right search criteria, but I had assumed that there would only be one section that it would apply to. Instead, the multiple outputs joined to make the new url. This one turned out to be a fun puzzle even if it was badly worded.
