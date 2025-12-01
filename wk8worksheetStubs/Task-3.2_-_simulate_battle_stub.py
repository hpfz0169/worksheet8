# Work completed by Taiyler Popat, Student Number: 201844877

"""
Exercise 3.2: Simulate a Turn-Based Battle (Class-Based)

In this exercise, you will create a Pokemon class and use it to simulate battles.
This demonstrates object-oriented programming principles: encapsulation, methods, and clear responsibilities.
"""

import httpx
import requests


class Pokemon:
    """
    Represents a Pokemon with stats fetched from the PokeAPI.
    """

    def __init__(self, name):
        """
        Initialise a Pokemon by fetching its data from the API and calculating its stats.

        Args:
            name (str): The name of the Pokemon (e.g., "pikachu")
        """
        # TODO: Store the Pokemon's name (lowercase)

        self.name = name.lower()

        # TODO: Fetch Pokemon data from PokeAPI

        # - Create the URL: f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        # - Make GET request
        # - Check response status code (raise error if not 200)
        # - Store the JSON data

        url = f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
        else:
            print("Error")

        # TODO: Calculate and store stats
        # - Use _calculate_stat() for attack, defense, speed
        # - Use _calculate_hp() for max HP
        # - Store stats in a dictionary
        # - Set current_hp = max_hp

        self.data = data

        base_stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}

        self.stats = {
            "attack": self._calculate_stat(base_stats["attack"]),
            "defense": self._calculate_stat(base_stats["defense"]),
            "speed": self._calculate_stat(base_stats["speed"]),
            "max_hp": self._calculate_hp(base_stats["hp"]),
        }

        self.current_hp = self.stats["max_hp"]

        pass

    def _calculate_stat(self, base_stat, level=50, iv=15, ev=85):
        """
        Calculate a Pokemon's stat at a given level.
        Helper method (note the underscore prefix).

        Args:
            base_stat (int): The base stat value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 15)
            ev (int): Effort value (default 85)

        Returns:
            int: The calculated stat
        """
        # TODO: Implement the stat calculation formula
        # Formula: 
        return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

    def _calculate_hp(self, base_stat, level=50, iv=15, ev=85):
        """
        Calculate a Pokemon's HP at a given level.
        HP uses a different formula than other stats.

        Args:
            base_stat (int): The base HP value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 15)
            ev (int): Effort value (default 85)

        Returns:
            int: The calculated HP
        """
        # TODO: Implement the HP calculation formula
        # Formula: 
        return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

    def attack(self, defender):
        """
        Attack another Pokemon, dealing damage based on stats.

        Args:
            defender (Pokemon): The Pokemon being attacked

        Returns:
            int: The amount of damage dealt
        """
        # TODO: Calculate damage using the damage formula
        # Formula: int((((2 * 50 * 0.4 + 2) * self.stats['attack'] * 60) / (defender.stats['defense'] * 50)) + 2)
        # Where 50 is level and 60 is base_power

        # TODO: Make the defender take damage
        # Call defender.take_damage(damage)

        attack_damage = int((((2 * 50 * 0.4 + 2) * self.stats['attack'] * 60) / (defender.stats['defense'] * 50)) + 2)

        defender.take_damage(attack_damage)

        # TODO: Return the damage amount

        return attack_damage

    def take_damage(self, amount):
        """
        Reduce this Pokemon's HP by the damage amount.

        Args:
            amount (int): The damage to take
        """
        # TODO: Reduce current_hp by amount
        # Make sure HP doesn't go below 0

        self.current_hp = self.current_hp - amount
        if self.current_hp < 0:
            self.current_hp = 0

        pass

    def is_fainted(self):
        """
        Check if this Pokemon has fainted (HP <= 0).

        Returns:
            bool: True if fainted, False otherwise
        """
        # TODO: Return True if current_hp <= 0, False otherwise

        return self.current_hp <= 0


    def __str__(self):
        """
        String representation of the Pokemon for printing.

        Returns:
            str: A nice display of the Pokemon's name and HP
        """
        # TODO: Return a string like "Pikachu (HP: 95/120)"
        return f"{self.name} (HP: {self.current_hp}/{self.stats['max_hp']})"


def simulate_battle(pokemon1_name, pokemon2_name):
    """
    Simulate a turn-based battle between two Pokemon.

    Args:
        pokemon1_name (str): Name of the first Pokemon
        pokemon2_name (str): Name of the second Pokemon
    """
    # TODO: Create two Pokemon objects

    pokemon1 = Pokemon(pokemon1_name)
    pokemon2 = Pokemon(pokemon2_name)

    # TODO: Display battle start message
    # Show both Pokemon names and initial HP

    print("LETS GET READY TO RUMBLE")
    print(pokemon1)
    print(pokemon2)

    # TODO: Determine who attacks first based on speed
    # The Pokemon with higher speed goes first
    # Hint: Compare pokemon1.stats['speed'] with pokemon2.stats['speed']

    if pokemon1.stats['speed'] >= pokemon2.stats['speed']:
        attacker = pokemon1
        defender = pokemon2
    else:
        attacker = pokemon2
        defender = pokemon1

    # TODO: Battle loop
    # - Keep track of round number
    # - While neither Pokemon is fainted:
    #   - Display round number
    #   - Attacker attacks defender
    #   - Display damage and remaining HP
    #   - Check if defender fainted
    #   - If not, swap attacker and defender
    #   - Increment round number

    round = 1
    
    while not attacker.is_fainted() and not defender.is_fainted():
        
        print(f"\nRound Number {round}")

        damage = attacker.attack(defender)
        print(f"{attacker.name} deals {damage} damage to {defender.name}!")
        print(f"{defender.name} HP: {defender.current_hp}/{defender.stats['max_hp']}")

    # TODO: Display battle result
    # Show which Pokemon won and their remaining HP

        if defender.is_fainted():
            print(f"\n{defender.name} fainted.")
            print(f"{attacker.name} wins with {attacker.current_hp}/{attacker.stats['max_hp']} HP remaining!")

        placeholder = attacker
        attacker = defender
        defender = placeholder
        round += 1

        pass


if __name__ == "__main__":
    # Test your battle simulator



    # simulate_battle("pikachu", "bulbasaur")

    # Uncomment to test other battles:
    # simulate_battle("Eevee", "Jigglypuff")
    # simulate_battle("eevee", "jigglypuff")
