#!/usr/bin/python

import argparse
# find highest price
# find lowest price
# has to start at 0 index of the array to act like buying and selling through the day
# then subtract the lowest from the highest to get profit or lose.
# Buying has to be first before selling


def find_max_profit(prices):
    current_min_price_so_far = prices[0]
    max_profit_so_far = prices[1] - prices[0]
    for i in range(1, len(prices)):
        # Keep track of the smallest price before it goes up in price!
        if prices[i] < current_min_price_so_far:
            current_min_price_so_far = prices[i]
            # print("prices[i]1:", prices[i])
            # print("current_min:", current_min_price_so_far)
        # Once the current_min is less than the price[i] elif comes in where it will then
        # minus the continues prices[i] from current_min until it finds the max profit
        elif prices[i] - current_min_price_so_far > max_profit_so_far:
            max_profit_so_far = prices[i] - current_min_price_so_far
            # print("prices[i]2:", prices[i],
            #       "current_min 2:", current_min_price_so_far)
            # print("max_profit:", max_profit_so_far)
    print(max_profit_so_far)


find_max_profit([1050, 270, 1540, 3800, 2])


# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
