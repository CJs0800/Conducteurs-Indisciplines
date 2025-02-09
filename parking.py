from random import randint

class Parking():
    """
    Simulates a parking system with adjacent spots constraints.

    Attributes:
        size (int): The total number of parking spots.
        spots (List[int]): A list representing parking spots (0 = free, 1 = occupied).
        free_spots (List[int]): A list of indices representing the starting positions of adjacent free spots.
    """
    
    def __init__(self, size:int) -> None:
        """
        Initializes the parking with `size` free spots.

        Args:
            size (int): The number of parking spots.
        
        Raises:
            ValueError: If the size is negative.
        """
        if size < 0:
            raise ValueError("La taille doit être un entier positif")
        else:
            self.size = size
            self.spots = [0] * size
            self.find_all_adjacent_free_spots()
        
    def find_all_adjacent_free_spots(self) -> None:
        """
        Identifies the starting indices of all adjacent pairs of free spots.

        This method updates the `free_spots` list with indices where two adjacent spots are free.
        """
        self.free_spots = []
        for i in range(self.size-1):
            if self.spots[i] == 0 and self.spots[i+1] == 0:
                self.free_spots.append(i)
    
    def find_random_adjacent_spots(self) -> int:
        """
        Returns a random index of two adjacent free spots.

        Returns:
            int: The index of the first spot in a pair of adjacent free spots.
        """
        if self.size == 0:
            raise ValueError("Aucun emplacement disponible")
        else:
            return self.free_spots[randint(0, len(self.free_spots)-1)]
    
    def fill_adjacent_spots(self, first_free_spots:int) -> None:
        """
        Fills two adjacent free spots starting from the given index.

        Args:
            first_free_spot (int): The index of the first free spot in the adjacent pair to be filled.
        """
        if not (first_free_spots in self.free_spots):
            raise ValueError("L'emplacement n'est pas libre")
        else:
            self.spots[first_free_spots] = 1
            self.spots[first_free_spots+1] = 1
        
    def fill_all_possible_spots(self) -> None:
        """
        Fills all possible adjacent pairs of free spots in the parking.

        This method iteratively finds and fills adjacent free spots until no such pair remains.
        """
        while (len(self.free_spots) != 0):
            chosen_spots = self.find_random_adjacent_spots()
            self.fill_adjacent_spots(chosen_spots)
            self.find_all_adjacent_free_spots()
    
    def calculate_occupied_spots(self) -> int:
        """
        Calculates the number of occupied parking spots.

        Returns:
            int: The number of occupied spots.
        """
        return sum(self.spots)
    
    def calculate_occupancy_rate(self) -> float:
        """
        Calculates the occupancy rate of the parking.

        Returns:
            float: The ratio of occupied spots to total spots.
        """
        if self.size == 0:
            raise ValueError("Division par 0 impossible")
        else:
            return self.calculate_occupied_spots() / self.size

    def __str__(self) -> str:
        """
        Returns a string representation of the parking spots.

        Returns:
            str: A string of the parking spots list where 0 represents free and 1 represents occupied spots.
        """
        return str(list(self.spots))
    


if __name__ == "__main__":
    parking_size = int(input("Entrez le nombre de places du parking : "))
    parking = Parking(parking_size)
    parking.fill_all_possible_spots()
    occupied_spots = parking.calculate_occupied_spots()
    occupancy = parking.calculate_occupancy_rate()
    print("\nTaille \t Places prises \t Pourcentage d'occupation")
    print(f"{parking_size} \t {occupied_spots} \t\t {occupancy*100}%")
