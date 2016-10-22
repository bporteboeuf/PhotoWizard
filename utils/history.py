#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module contains history management functionalities


class History: # Each time a file is opened, a History object is created

    def __init__(self):
        self.name = name
        self.branch = [newBranch()]
        self.currentstate = None
    return


    def newBranch(branch): # Creates a new history branch

        return


    def removeBranch(branch): # Suppresses a history branch

        return


    def undo(): # Undoes the last action

        return


    def redo(): # Redoes the last action

        return


    def restore(branch,index): # Restores the current state to a previous history version, in a given branch and at a given index

        return


    def getCurrentState(branch): # Gets current state of a given history branch

        return


    def getHistory(branch): # Returns the full history of the given branch

        return


    def insertEvent(branch,index,event): # Inserts a new event in a given branch, at a given index

        return


    def removeEvent(branch,index,event): # Deletes an event in a given branch, at a given index

        return


    def search(ID): # Locates an event by its ID, returns its branch and its index

        return






class HistoryBranch: # A history branch is created when there is a fork in the history of an image
    
    def __init__(self,name):


        return

    def insertEvent(event,index) : # Inserts an event

        return

    def removeEvent(event,index):
        
        return
    



class Event: # Each action creates an event object, which is part of a history branch

    def __init__(self,ID,branch,parent,state):
        self.id = ID
        self.branch = branch
        self.next = None
        self.previous = parent
        self.state = state
        return


    def getNext():
        return self.next


    def getPrevious():
        return self.previous


    def setNext(nextEvent):
        self.next = nextEvent
        return
    
    def setPrevious(previousEvent):
        self.previous = previousEvent
        return






