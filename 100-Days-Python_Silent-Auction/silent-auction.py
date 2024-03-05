print("Welcome to the silent auction")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid

    ifMore = input("Are there other bidders?")
    while ifMore != "yes" and ifMore != "no":
        ifMore = input("I'm sorry; I didn't catch that. Please respond 'yes' or 'no'")
    if ifMore == "yes":
        print("\n" * 100)
    else:
        print("\n" * 100)
        bidding_finished = True

find_highest_bidder(bids)