import json
import pathlib


try:
    import simulation.fast as simulation

    print("Using fast module.")

except ImportError:
    import simulation.slow as simulation

    print("Using slow module.")


def make_directories(*paths):
    """Creates directories on the specified paths if they do not exist."""
    for path in paths:
        if not path.exists():
            path.mkdir()


def main():
    """Most basic implementation of the simulation algorithm to fulfill
    the intended purpose of the application."""

    # Define the path objects
    root_path = pathlib.Path(__file__).resolve().parent
    card_sets_path = root_path.joinpath("card_sets.json")
    output_path = root_path.joinpath("output")
    minimum_path = output_path.joinpath("minimum")
    maximum_path = output_path.joinpath("maximum")

    # Create the output paths
    make_directories(output_path, minimum_path, maximum_path)

    # Parse the JSON file holding the data for the card sets
    with card_sets_path.open("r", encoding="UTF-8") as f:
        card_sets = json.load(f)

    # Iterate over the card sets and process
    for cs, (cc, tc) in card_sets.items():
        print(f"Processing {cs}")

        # Minimum: Obtain PUR cards
        # Maximum: Obtain ALL cards
        minimum = simulation.aggregate(cc, tc, 10_000)
        maximum = simulation.aggregate(cc, cc, 10_000)

        min_result_path = minimum_path.joinpath(f"{cs}.json")
        max_result_path = maximum_path.joinpath(f"{cs}.json")

        with min_result_path.open("w", encoding="UTF-8") as min_file:
            json.dump(minimum, min_file, indent=2)

        with max_result_path.open("w", encoding="UTF-8") as max_file:
            json.dump(maximum, max_file, indent=2)


if __name__ == "__main__":
    main()
