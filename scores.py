"""
Program: dictionary.py
Author: Duroje Gwamna
Date Last Modified: 11/14/2021

This program shows two functions that operate on a dictionary that stores
user test scores: get_test_score() that updates the dictionary, and average_scores()
that will collect the keys and values of the dictionary to return the average value
"""

def get_test_scores():
    scores_dict = dict()
    num_scores = int(input("Enter the number of scores: "))
    for i in range (0, num_scores):
        score = int(input("Enter test score: "))
        while score < 0 or score > 100:
            score = int(input("Invalid test score. Please re-try: "))
        scores_dict.update({i:score})
    return scores_dict

def average_scores(dict):
    if dict == {}:
        raise ValueError
    sum = 0
    num_scores = len(dict) # get num scores from dictionary
    keys = list(dict) # get keys from dictionary 
    for k in keys:
        sum += dict.get(k) # stores the sum of all values in dictionary
    return  sum/num_scores

if __name__ == "__main__":
    scores = get_test_scores()
    test_scores = {1:100, 2:96, 3:99}
    print("Average test score: %3.1f" % (average_scores(scores)))
    print("\n")
    print("Average test scores using 'test_scores': %3.1f" % (average_scores(test_scores)))
    

    
    

    



    

