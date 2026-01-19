from typing import List, Tuple
#I can use Tuple like in C#. Nice.

# Constants
MONTHS_PER_YEAR = 12

# Updated input validation functions to handle both float and int types from previous modules.
def validFloat(prompt: str, min_value: float | None = None) -> float:
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def validInt(prompt: str, min_value: int | None = None) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


# Wrappers for specific validations
def validPositiveInt(prompt: str) -> int:
    return validInt(prompt, min_value=1)


def validNonNegativeFloat(prompt: str) -> float:
    return validFloat(prompt, min_value=0.0)

# Computational functions
def computeRainfallStats(rainfalls: List[float]) -> Tuple[int, float, float]:
    months = len(rainfalls)
    total = sum(rainfalls)
    average = total / months if months > 0 else 0.0
    return months, total, average


def computeBookClubPoints(books: int) -> int:
    if books >= 8:
        return 60
    if books >= 6:
        return 30
    if books >= 4:
        return 15
    if books >= 2:
        return 5
    return 0

# UI functions
def rainfallUI() -> None:
    number_of_years = validPositiveInt("Enter the number of years: ")
    rainfalls: List[float] = []

    for year in range(1, number_of_years + 1):
        print(f"\n--- Year {year} ---")
        for month in range(1, MONTHS_PER_YEAR + 1):
            rainfall = validNonNegativeFloat(
                f"Enter the inches of rainfall for month {month}: "
            )
            rainfalls.append(rainfall)

    months, total, average = computeRainfallStats(rainfalls)

    print("\n--- Rainfall Statistics ---")
    print(f"Total number of months: {months}")
    print(f"Total inches of rainfall: {total:.2f}")
    print(f"Average rainfall per month: {average:.2f}")


def bookClubUI() -> None:
    books = validInt("Enter the number of books purchased this month: ", min_value=0)
    points = computeBookClubPoints(books)
    print(f"Points awarded: {points}")


if __name__ == "__main__":
    try:
        while True:
            print("Select an operation:")
            print("1. Calculate Average Rainfall")
            print("2. Calculate Book Club Points")
            print("3. Exit")

            choice = validInt("Enter your choice (1, 2, or 3): ", min_value=1)

            if choice == 1:
                rainfallUI()
            elif choice == 2:
                bookClubUI()
            elif choice == 3:
                print("Goodbye.")
                break
            else:
                print("Invalid selection. Please choose 1, 2, or 3.")
    except (KeyboardInterrupt, EOFError):
        print("\nInput interrupted. Exiting.")