def calculate_hand_value(hand):
    """Izračun vrednosti roke."""
    value = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            value += 10
            aces += 1
        else:
            value += int(card)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    
    
    return value

def blackjack_svetovalec():
    """svetovallec za igro blackjack."""
    print("Dobrodošli v Blackjack svetovalcu! Vnesite svoje karte, da dobite nasvet.")
    hand = input("Vnesite svoje karte (ločite jih z vejico, npr. 'A,7'):").split(',')
    hand = [card.strip().upper for card in hand]

    dealer_card = input("Vnesite delilčevo vidno karto: ").strip().upper()
    blackjack = False
    bust = False
    while True:
        hand_value = calculate_hand_value(hand)
        print(f"Vaša trenutna roka ({', '.join(hand)}): {hand_value}")

        if hand_value > 21:
            print("Vaša roka presega 21. To je BUST. Konec igre.")
            bust = True
            break
        if hand_value == 21:
            print("BLACKJACK! Zmagali ste igro!")
            blackjack = True
            break
        if hand_value >= 17:
            print("Nasvet: STAND")
        elif hand_value >= 13 and dealer_card in ['2', '3', '4', '5', '6']:
            print("Nasvet: STAND")
        elif hand_value == 12 and dealer_card in ['4', '5', '6']:
            print("Nasvet: STAND")
        


if __name__ == "__main__":
    print("Pozdravljeni!")
    blackjack_svetovalec()