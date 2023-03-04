print("Start")

class Deck():
    pile =  []
    hand_1 = []
    hand_2 = []
    scored = []
    score = []

    def SearchWin():
        #Get suit numbers
        scored.append(hand_1[0])
        suits = [0,0,0,0]   #list of occurences of the 4 suits
        for card in hand_1:
            suits[card.suit] += 1

        for i in range(suits):
            #Flush
            if suits[i] >= 5:       #if more than 5 cards of 1 suit
                for card in hand_1:     #Remove cards not of flush suit
                    if card.suit != suits[1]:
                        hand_1.remove(card)
                hand_1.sort(key=Card.value)     #Sort cards of similar suit
                for i in range(hand_1.count - 1):  
                    score.append = hand_count[i].value  #Highest card in flush     
                    #Flush (not straight)   (6, highest card)
                    if Math.abs(hand_1[i].num - hand_1[i+1]) != 1:      #if  not consecutive numbers --> flush
                        score.insert(0, 6)
                        return
                #Straight Flush (9, highest card)
                score(0, 9)
                return
            hand_1.sort(reverse=true, key=Card.value)
            
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

            #Four of a kind (8, number of 4, next highest card)
            if repititions[most] == 4:
                score.append(8)
                score.append(most)
                for card in hand_1:
                    if card.value != most:
                        score.append(card.value)
            
            if repitions[most] == 3:
                #3 of a kind (4, number of 3, next two highest cards)
                score.append(4)
                score.append(most)
                repitions.pop(most)
                for card in hand_1:
                    if card.value != most:
                        score.append(card.value)
                        if(score.count == 4):
                            break
                #Full House (7, number of 3, number of 2)
                if(len(repitions) == 1):
                    score = [7, most, repitions.keys[0]]
                return
            if most == 1:
                for i in range(len(hand_1)-1):
                    isStraight = True
                    if Math.abs(hand_1[i].num - hand_1[i+1]) != 1:      #if  not consecutive numbers --> high card
                        isStraight
                    if isStriaght:
                        #Straight   (5, highest card)
                        score = [5, hand_1[0]]
                    else:
                        #High card  (1, cards from high to low)
                        score = hand_1
                        score.insert(0, 1)
            pairs = []
            for num in repitions.keys:
                if repitions[num] == 2:
                    pairs.append(num)
            
            #One pair   (2, pair number, next 3 highest cards)
            if len(pairs) == 1:
                score = [2, pairs[0]]
                for card in hand_1:
                    if card.value != pairs[0]:
                        score.append(card.value)
                        if len(score) == 5:
                            return

            #Two pair   (3, pair numbers, next highest card)
            if len(pairs) == 1:
                score = [2, pairs[0]]
                for card in hand_1:
                    if card.value != pairs[0] and card.value != pairs[1]:
                        score.append(card.value)
                        return

            

            

Deck()
