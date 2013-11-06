# -*- encoding: utf-8 #

'''
  usage:

'''

from  recommendations import *
import os

class itemBasedRecommendations():
  def __init__(self):
    self.prefs,self.ratingArray = loadMovieLens(os.getcwd()+'/data')
    self.numOfUsers, self.numOfItems = self.ratingArray.shape

  def getAvgRatingOfUser(self,userId):
    # return Average rating of a user for all items (only rated items)
    numOfRating = sum((self.ratingArray[userId-1,:]>0)*1)  
    return sum(self.ratingArray[userId-1,:])/numOfRating

  def getAvgRatingOfAllUsers(self):
   
    avg = np.zeros(self.numOfUsers);
    for i in range(self.numOfUsers):
      avg[i-1] = self.getAvgRatingOfUser(i); 
    return avg

  def getSimilarityOfItems(self,Item1,Item2):
    # return similarity of Item1 and Item2 for a user
    rating1 = self.ratingArray[:,Item1-1]
    rating2 = self.ratingArray[:,Item2-1] 
    avg = self.getAvgRatingOfAllUsers()
    A = (rating1-avg)*(rating1>0)*1
    B = (rating2-avg)*(rating2>0)*1      
    similarity = sum(A*B)/np.sqrt(sum(A*A+B*B));
    return similarity

  def predictRating(self,item,userId):
    similarity = np.zeros(self.numOfItems);    
    for i in range(self.numOfItems):
      similarity[i-1] = self.getSimilarityOfItems(i,item)
      if i==item:
        similarity[i-1] = 0 
    Total = sum(self.ratingArray[userId-1,:]*similarity*(self.ratingArray[userId-1,:]>0)*1) 
    weighted = sum(similarity*(self.ratingArray[userId-1,:]>0)*1)
    return Total/weighted


if __name__ == '__main__':
  
  rec = itemBasedRecommendations()
  for i in range(30):
    print rec.getSimilarityOfItems(31,i)
  #print rec.predictRating(200,1)  


