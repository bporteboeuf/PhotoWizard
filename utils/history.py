#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module contains history management functionalities


class History: # Each time a file is opened, a History object is created

    def __init__(self,ID):
        self.name = ID
        self.events = {}
        self.events[0] = Event(0,None,'InitState','InitialState')
        self.currentState = 0
        self.redoState = None
        return


    def getCurrentState(self):
        return self.currentState

    
    def setCurrentState(self,ID):
        if (type(ID) is int) and (ID >= 0):
            self.currentState = ID
        else:
            raise NameError('PhotoWizardError: Wrong argument format in class History')
        return


    def getRedoState(self):
        return self.redoState


    def setRedoState(self,ID):
        if (type(ID) is int) and (ID > 0):
            self.redoState = ID
        return


    def getEvents(self):
        return self.events


    def setEvents(self,events):
        if (type(events) is dict):
            for elt in events:
                if not isinstance(events[elt],Event):
                    raise NameError('PhotoWizard Error: Wrong argument type in setEvents')
            self.events = events
        else:
            raise NameError('PhotoWizard Error: Wrong argument type in setEvents')
        return


    def getEvent(self,ID):
        if ID is not None:
            return self.events[ID]
        else:
            return None


    def undo(self): # Undoes the last action
        self.setRedoState(self.getCurrentState())
        state = self.getEvent(self.getCurrentState()).getPrevious()
        if state is not None:
            self.setCurrentState(state)
        else:
            print('PhotoWizard Error: Unable to undo actions past initial state')
        return state 


    def redo(self): # Redoes the last action
        if self.getRedoState() is not None:
            tmp = self.getRedoState()
            self.setCurrentState(tmp)
            self.setRedoState(None)
            return tmp
        else:
            nextEvent = self.getEvent(self.getCurrentState()).getNext()
            if nextEvent is not None:
                if len(nextEvent) == 1:
                    self.setCurrentState(nextEvent)
                    return nextEvent
                else:
                    return None # Several next possible events lead to ambiguity
            else: # Leaf already reached
                return None


    def rebase(self,ID): # Restores the current state to a previous history version, in a given branch and at a given index
        if (type(ID) is int) and (ID >= 0):
            self.currentState = ID
        else:
            raise NameError('PhotoWizardError: Wrong argument format in class History')
        return


    def explore(self,ID): # Explores the history, search in deep first, returns a list of lists of ID
        tree = list()
        nextEvents = self.getEvent(ID).getNext()
        if nextEvents is not None:
            if len(nextEvents) == 1:
                tree.append(nextEvents)
            else:
                for event in nextEvents:
                    tree.append(explore(event.getID()))
        else:      
            return tree


    def toString(self,tree,index): # Converts a tree from a list of lists to a printable string
        string = ""
        if tree is not None:
            for elt in tree:
                if type(elt) is not list:
                    string+="---"+str(elt)
                    index += 4
                else:
                    string+="\n"+" "*index+"\\"+str(toString(elt,index))
        return string



    def getFullHistory(self): # Returns the full history as a string
        tree = self.explore(0)
        tree = self.toString(tree,0)
        return tree


    def getHistory(self): # Returns the list of events in the current history - used for export
        hist = []
        tmp = self.getEvent(self.getCurrentState())
        while tmp is not None:
            hist.append(tmp)
            tmp = self.getEvent(tmp.getPrevious())
        return hist[::-1]



    def add(self,content,label): # adds a new event
        newEvent = Event(len(self.events),self.currentState,content,label)
        self.events[newEvent.getID()] = newEvent
        if self.getCurrentState() is not None:
            currentState = self.getEvent(self.getCurrentState())
            currentState.setNext(newEvent.getID())
        self.setCurrentState(newEvent.getID())
        return


    def clearHistory(self): # Deletes all events
        self.events = {}
        return









class Event: # Each action creates an event object, which is part of a history branch

    def __init__(self,ID,previous,request,label):
        if (type(ID) is int) and ((previous is None) or ((type(previous) is int) and (previous >= 0))) and (type(request) is str) and (type(label) is str):
            if (ID >= 0):
                self.id = ID
                self.next = {}
                self.previous = previous
                self.content = request # Contains the request of the user, as defined by mapping.everyFunction
                self.label = label # Contains a label for display
            else:
                raise NameError('PhotoWizard Error: Wrong argument format in class Event')
        else:
            raise NameError('PhotoWizard Error: Wrong argument format in class Event')
        return


    def getID(self):
        return self.id


    def getNext(self):
        return self.next


    def setNext(self,ID):
        if (type(ID) is int) and (ID > 0):
            self.next[ID] = ID
        else:
            raise NameError('PhotoWizardError: Wrong argument format in class Event')
        return
 

    def getPrevious(self):
        return self.previous

    
    def setPrevious(self,ID):
        if (type(ID) is int) and (ID >= 0):
            self.previous = ID
        else:
            raise NameError('PhotoWizardError: Wrong argument format in class Event')
        return

   
    def getContent(self):
        return self.content


    def setContent(self,request):
        if (type(request) is str):
            self.content = request
        else:
            raise NameError('PhotoWizard Error: Wrong argument format in class Event')
        return


    def getLabel(self):
        return self.label


    def setLabel(self,label):
        if type(label) is str:
            self.label = label
        else:
            raise NameError('PhotoWizard Error: Wrong argument format in class Event')
        return




