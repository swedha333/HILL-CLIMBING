#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string
def generate_random_solution(answer):
    #l=TYPE THE CODE HERE ,FIND THE LEN OF answer and store in l
    l=len(answer)
    return [random.choice(string.printable) for _ in range(l)]
def evaluate(solution,answer):
    print(solution)
    target=list(answer)
    diff=0
    for i in range(len(target)):
        s=solution[i]
        t=target[i]
        #to calculate the "difference" between two strings, character by character.
        #ord(s) - ord(t) calculates the difference between the ASCII values of the characters s and t.
         #abs() takes the absolute value of this difference to ensure that it is non-negative. This is important because the difference could be negative if s is less than t in terms of ASCII value.
         #The absolute value ensures that the difference is always positive or zero.
        #Type the code here by referring to the above description 
        diff += abs(ord(s) - ord(t)) 
    return diff
def mutate_solution(solution):
    ind=random.randint(0,len(solution)-1)
    solution[ind]=random.choice(string.printable)
    return solution
def SimpleHillClimbing():
    answer="Artificial Intelligence"
    best=generate_random_solution(answer)
    best_score=evaluate(best,answer)
    while True:
        print("Score:",best_score," Solution : ","".join(best))  
        if best_score==0:
            break
        new_solution=mutate_solution(list(best))
        score=evaluate(new_solution,answer)   
        if score<best_score:
            best=new_solution
            best_score=score
#answer="Artificial Intelligence"
#print(generate_random_solution(answer))
#solution=generate_random_solution(answer)
#print(evaluate(solution,answer))
SimpleHillClimbing()

