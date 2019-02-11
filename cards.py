class Card():
    def __init__(self, numFace, numSuit):
        self.numFace = numFace
        self.numSuit = numSuit
    def getCardName(self):
        suit_names = ['Spades', 'Hearts', 'Clubs', 'Daimonds']
        face_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        return "%s of %s" % (face_names[self.numFace], suit_names[self.numSuit])
def Make_Deck():
    deck = []
    for numSuit in range(4):
        for numFace in range(13):
            newCard = Card(numFace, numSuit)
            deck.append(newCard)
    return deck
deck = Make_Deck()
for card in deck:
    print(card.getCardName())
    print(card.numFace)
