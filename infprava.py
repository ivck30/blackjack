def calculate_hand_value(hand):
    """Izračuna vrednost roke."""
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

def blackjack_advisor():
    """Osnovni svetovalec za blackjack."""
    print("Dobrodošli v Blackjack svetovalcu! Vnesite svoje karte, da dobite nasvet.")
    hand = input("Vnesite svoje karte (ločite jih z vejico, npr. 'A,7'): ").split(',')
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

        # Osnovna strategija
        if hand_value >= 17:
            print("Nasvet: Stand")
        elif hand_value >= 13 and dealer_card in ['2', '3', '4', '5', '6']:
            print("Nasvet: Stand")
        elif hand_value == 12 and dealer_card in ['4', '5', '6']:
            print("Nasvet: Stand")
        elif len(hand) == 2 and hand[0] == hand[1]:
            print("Nasvet: Split")
        elif hand_value <= 11:
            print("Nasvet: Hit")
        else:
            print("Nasvet: Hit")

        action = input("Vnesite vašo potezo (hit/stand/split): ").strip().lower()
        if action == 'hit':
            new_card = input("Vnesite novo karto: ").strip().upper()
            hand.append(new_card)
        elif action == 'split':
            print("Razdelili ste roko. Upoštevajte nadaljnja pravila.")
        elif action == 'stand':
            print("Odločili ste se za stand. Poglejmo rezultat.")
            break
        else:
            print("Neveljavna poteza. Poskusite znova.")
    if blackjack == False:
        result = input("Ali ste zmagali ali izgubili? (win/lose): ").strip().lower()
        if result == 'win':
            print("Čestitamo! Uporaba strategije se je obrestovala.")
        elif result == 'lose':
            print("Žal ste izgubili. Morda poskusite prilagoditi svojo strategijo.")
        else:
            print("Neveljaven vnos za rezultat igre.")
    elif bust == False:
        result = input("Ali ste zmagali ali izgubili? (win/lose): ").strip().lower()
        if result == 'win':
            print("Čestitamo! Uporaba strategije se je obrestovala.")
        elif result == 'lose':
            print("Žal ste izgubili. Morda poskusite prilagoditi svojo strategijo.")
        else:
            print("Neveljaven vnos za rezultat igre.")

if __name__ == "__main__":
    print("hello")
    blackjack_advisor() 