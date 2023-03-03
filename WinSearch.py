print("Start")

class Deck():
    pile =  []
    hand_1 = []
    hand_2 = []
    scored = []
    score = (0, 0)

    def SearchWin():
        #Get suit numbers
        scored.append(hand_1[0])
        suits = [0,0,0,0]   #list of occurences of the 4 suits
        for card in hand_1:
            suits[card.suit] += 1

        for i in range(suits):
            #Flush
            if suits[i] >= 5:       #if more than 5 cards of 1 suit
                for card in hand_1:     #Remove cards not of flush suit and add values to tiebreak score
                    if card.suit != suits[1]:
                        score[1] += card.value
                        hand_1.remove(card)
                hand_1.sort(key=Card.value)     #Sort cards of similar suit
                for i in range(hand_1.count - 1):       
                    #Flush (not straight)   
                    if Math.abs(hand_1[i].num - hand_1[i+1]) != 1:      #if  not consecutive numbers --> flush
                        score[0] = 6
                        return
                #Straight Flush
                score[0] = 9
                return
            hand_1.sort(key=Card.value)
            
            #
            #Dictionary<int number, int quantity>
            repitions = {}
            for card in hand_1:
                if(repitions.get(card) is None):
                    repitions[card.value] = 1
                else:
                    repitions[card.value] += 1

            most = 0
            for num in repitions.keys:
                if repition[num] > most:
                    most = num
            if(most == 4):

            

            


Deck()