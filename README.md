# Hotel-Chain-Database

A Text based hotel chains data base which is created through the use of Binary Search Trees. Hotel ratings are found inside a text file. Each line of data contains the following:

hotel ID number
preferred location score/25
reputation score/25
cleanliness and comfort score/15
amenities score/20
price (budget) score/20
luxury score/35
overall average satisfaction of guests /65  

The binary search tree sorts via hotel ID number. 

The user is prompted with 5 different options as follows:

1) add a new node to the tree (manually input the hotel ID number and all of it's associated scores).

2) find the average of any one of the scores (prompt the user for which criteria to find the average of).

3) prompt the user for a criterion (i.e. cleanliness and comfort) and the minimum acceptable score. For example, the user may only be willing to stay in a hotel that receives a cleanliness and comfort score of 60% or greater. Print a listing of all hotel ID numbers whose criteria is greater than or equal to the minimum acceptable score.

4) count the number of hotels that got less than a 70% rating on the "overall average satisfaction of guests" criteria.

5) look up the scores for a hotel. If a tourist arrives looking for information on a particular hotel, the function should prompt the user for a hotel ID number and, if that hotel is found, print its scores.  If the hotel is not found, it should print a message that "the hotel does not exist".
