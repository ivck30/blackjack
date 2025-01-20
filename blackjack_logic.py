def calculate_hand_value(hand):
    """Izračun vrednosti roke."""
    value = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            value += 11
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
    hand = [card.strip().upper() for card in hand]

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
        elif len(hand) == 2 and hand[0] == hand[1]:
            print("Nasvet: SPLIT")
        elif hand_value <= 11:
            print("Nasvet: HIT")
        else:
            print("Nasvet: HIT")
        
        poteza = input("Vnesite vašo potezo (HIT/STAND/SPLIT): ").strip().lower()
        if poteza == 'hit':
            nova_karta = input("Vnesite novo karto:").strip().upper()
            hand.append(nova_karta)
        elif poteza == 'split':
            print("Razdelili ste roko. Sledite nadaljnjim nasvetom.")
        elif poteza == 'stand':
            print("Odločili ste se za STAND. Poglejva rezultat.")
            break
        else:
            print("Neveljavna poteza. Poskusite znova.")
    if blackjack == False:
        rezultat = input("Ali ste zmagali ali izgubili? (zmaga/poraz): ").strip().lower()
        if rezultat == 'zmaga':
            print("Čestitam! Uporaba svetovalca se je obrestovala.")
        elif rezultat == 'poraz':
            print("Žal ste izgubili. Poskusite ponovno.")
        else:
            print("Neveljaven rezultat igre.")


if __name__ == "__main__":
    print("Pozdravljeni!")
    blackjack_svetovalec()