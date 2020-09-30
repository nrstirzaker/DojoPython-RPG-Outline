#def showInstructions
#    RPG Game
#    ========

#    Get to the Garden with a key and a potion
#    Avoid the monsters!

#    You are getting tired, each time you move you loose 1 health point. 

#    Commands:
#       go [direction]
#       get [item]

#def showStatus

# define data structure using a dictionary

#def gameLoop
#   showStatus
#   get Input  
#   if input start with 'go':
#       if player can move in the direction specified
#           decrease health
#           move to that room
#       else
#           tell user they can't got that way
# 
#   if input start 'get':
#       if the item specified is in the room:
#           add item to inventory
#           remove item from the room
#           print "you've got item......"      
#   else
#           print "can't get item"
#
#   if item in room is monster
#       print game over
#
#   if health = 0
#       print gamne over
#
#   if win condition (exit room, key and potion)
#       print you win