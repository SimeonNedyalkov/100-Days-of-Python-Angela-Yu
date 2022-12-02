
# HINT: You can call clear() to clear the output in the console.


bid = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            print(f"The winner is {winner} and won with {highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    bid[name] = price
    any_other = input("Are there any other bidders? yes or no? n\ ")
    if any_other == "no":
        bidding_finished = True
        find_highest_bidder(bid)
    elif any_other == "yes":
        bidding_finished = False



