#!/usr/bin/env python
# coding: utf-8

# Q1. Explain the difference between greedy and non-greedy syntax with visual terms in as few words as possible. What is the bare minimum effort required to transform a greedy pattern into a non-greedy one? What characters or characters can you introduce or change?
# 

# Greedy syntax matches as much as possible, while non-greedy syntax matches as little as possible. To transform a greedy pattern into a non-greedy one, you can introduce the "?" character after the quantifier.

# Q2. When exactly does greedy versus non-greedy make a difference?  What if you're looking for a non-greedy match but the only one available is greedy?
# 

# If you need a non-greedy match but only a greedy match is available, you can modify the quantifier by adding a "?" directly after it. This minimal change will transform the pattern into a non-greedy one.
# 

# Q3. In a simple match of a string, which looks only for one match and does not do any replacement, is the use of a nontagged group likely to make any practical difference?
# 

# In a simple string match without capturing specific groups, using a non-tagged group does not make any practical difference.

# Q4. Describe a scenario in which using a nontagged category would have a significant impact on the program's outcomes.
# 

# Using a non-tagged group (non-capturing group) can have a significant impact on program outcomes when using regular expressions with backreferences, as it can affect the numbering of capturing groups and potentially cause unexpected behavior.

# Q5. Unlike a normal regex pattern, a look-ahead condition does not consume the characters it examines. Describe a situation in which this could make a difference in the results of your programme.
# 

# A look-ahead condition in a regex pattern can make a difference in program results by allowing you to check for the presence of a pattern without consuming it, enabling more complex matching logic without affecting the overall result or subsequent matches.

# Q6. In standard expressions, what is the difference between positive look-ahead and negative look-ahead?
# 

# 
# Positive look-ahead (?=pattern) checks if a match is followed by a specific pattern, while negative look-ahead (?!pattern) checks if a match is not followed by a specific pattern.

# Q7. What is the benefit of referring to groups by name rather than by number in a standard expression?
# 

# Using named groups in a regular expression improves readability, maintainability, self-documentation, flexibility, and integration with programming languages.

# Q8. Can you identify repeated items within a target string using named groups, as in "The cow jumped over the moon"?
# 

# In[ ]:


import re

string = "The cow jumped over the moon"

