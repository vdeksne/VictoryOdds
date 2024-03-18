# TODO

import cs50


def calculate_quarters(cents):
    # // - tikai veselais iznakums
    # % - tikai atlikums
    coins = cents // 25
    return coins


def calculate_dimes(cents):
    coins = cents // 10
    return coins


def calculate_nickels(cents):
    coins = cents // 5
    return coins


def calculate_pennies(cents):
    coins = cents // 1
    return coins


def get_cents():
    cents = 0
    while cents < 1:
        cents = cs50.get_float("Change owed: ")
        cents = int(cents * 100)
    return cents


# funkcija vai uzreiz kods, vai pārbaude par run pogu


def main():
    cents = get_cents()
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5
    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1
    coins = quarters + dimes + nickels + pennies
    print(coins)


if __name__ == "__main__":
    main()
