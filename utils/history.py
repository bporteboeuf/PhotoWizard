#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module contains history management functionalities


class History: # Each time a file is opened, a History object is created

    def __init__(self):
        self.name = name
        self.events = {}
        self.currentLeaf = None
        self.currentState = None
    return


    def getCurrentState(self):
        return self.currentState

    
    def setCurrentState(self,ID):
        self.currentState = ID
        return


    def getCurrentLeaf(self):
        return self.currentLeaf

    
    def setCurrentLeaf(self,ID):
        self.currentLeaf = ID
        return


    def getEvent(self,ID):
        return self.events[ID]


    def findLeaf(self,ID):
        if ID is not None:
            nextEvent = self.getEvent(ID).getNext()
            if nextEvent is None: # Leaf reached
                return ID
            elif len(nextEvent)==1: # Only one possible next event
                return findLeaf(nextEvent)
            else: # Several possible next events lead to ambiguity
                return None
        else:
            return None


    def getLeaf(self,ID):
        return findLeaf(ID)


    def undo(self): # Undoes the last action
        return self.getEvent(self.getCurrentState()).getPrevious()


    def redo(self): # Redoes the last action
        nextEvent = self.getEvent(self.getCurrentState()).getNext()
        if nextEvent is not None:
            if len(nextEvent) == 1:
                return nextEvent.getID()
            else:
                return None # Several next possible events lead to ambiguity
        else: # Leaf already reached
            return None


    def rebase(self,ID): # Restores the current state to a previous history version, in a given branch and at a given index
        self.currentState = ID
        self.currentLeaf = self.getLeaf(ID)
        return


    def explore(self,ID): # Explores the history, search in deep first, returns a list of lists of ID
        tree = list()
        nextEvents = self.getEvent(ID).getNext()
        if nextEvents is not None:
            if len(nextEvents) == 1:
                tree.append(node)
            else:
                for event in nextEvent:
                    tree.append(explore(event.getID()))
        else:      
            return tree


    def toString(self,tree,index): # Converts a tree from a list of lists to a printable string
        string = ""
        for elt in tree:
            if type(elt) is not list:
                string+="---"+str(elt)
                index += 4
            else:
                string+="\n"+" "*index+"\\"+str(toString(elt,index))
        return string



    def getHistory(self): # Returns the full history as a string
        tree = self.explore([],1)
        tree = self.toString(tree,0)
        return tree



    def add(self,content,label): # adds a new event
        newEvent = Event(len(self.events)+1,self.currentState,content,label)
        currentState = self.getEvent(self.currentState)
        currentState.setNext(newEvent.getID())
        if len(currentState.getNext())>1:
            self.setCurrentLeaf(newEvent.getID())
        return


    def clearHistory(self): # Deletes all events
        self.events = {}
        return









class Event: # Each action creates an event object, which is part of a history branch

    def __init__(self,ID,previous,content,label):
        self.id = ID
        self.next = {}
        self.previous = previous
        self.content = content
        self.label = label
        return


    def getID(self):
        return self.ID


    def getNext(self):
        return self.next


    def setNext(self,ID):
        self.next[ID] = ID
        return
 

    def getPrevious(self):
        return self.previous

    
    def setPrevious(self,ID):
        self.previous = ID
        return

   
    def getContent(self):
        return self.content


    def setContent(self,content):
        self.content = content
        return


    def getLabel(self):
        return self.label


    def setLabel(self,label):
        self.label = label
        return




