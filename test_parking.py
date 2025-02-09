import unittest
from random import randint
from parking import Parking

class TestParking(unittest.TestCase):
    
    # =============== initialization =================
    def test_initialization_with_size_0(self) -> None:
        """Test the initialization with a size of 0."""
        parking = Parking(0)
        self.assertEqual(parking.size, 0)
        self.assertEqual(parking.spots, [])
        self.assertEqual(parking.free_spots, [])
        
    def test_initialization_with_size_1(self) -> None:
        """Test the initialization with a size of 1."""
        parking = Parking(1)
        self.assertEqual(parking.size, 1)
        self.assertEqual(parking.spots, [0])
        self.assertEqual(parking.free_spots, [])
        
    def test_initialization_with_size_2(self) -> None:
        """Test the initialization with a size of 2."""
        parking = Parking(2)
        self.assertEqual(parking.size, 2)
        self.assertEqual(parking.spots, [0, 0])
        self.assertEqual(parking.free_spots, [0])
        
    def test_initialization_with_size_5(self) -> None:
        """Test the initialization with a size of 5."""
        parking = Parking(5)
        self.assertEqual(parking.size, 5)
        self.assertEqual(parking.spots, [0, 0, 0, 0, 0])
        self.assertEqual(parking.free_spots, [0, 1, 2, 3])
   
    def test_initialization_invalid_size(self) -> None:
        """Test that a ValueError is raised when the parking size is negative."""
        with self.assertRaises(ValueError):
            Parking(-1)
    # =============== initialization =================
   
   
    # =============== find_all_adjacent_free_spots =================
    def test_find_all_adjacent_free_spots_with_size_0(self) -> None:
        """Test the find_adjacent_free_spots method with a size of 0."""
        parking = Parking(0)
        parking.spots = []
        parking.find_all_adjacent_free_spots()
        self.assertEqual(parking.free_spots, [])
        
    def test_find_all_adjacent_free_spots_with_size_1(self) -> None:
        """Test the find_adjacent_free_spots method with a size of 1."""
        parking = Parking(1)
        parking.spots = [0]
        parking.find_all_adjacent_free_spots()
        self.assertEqual(parking.free_spots, [])
        parking.spots = [1]
        parking.find_all_adjacent_free_spots()
        self.assertEqual(parking.free_spots, [])
    
    def test_find_all_adjacent_free_spots_with_size_2(self) -> None:
        """Test the find_adjacent_free_spots method with a size of 2."""
        parking = Parking(2)
        parking.spots = [0, 0]
        parking.find_all_adjacent_free_spots()
        self.assertEqual(parking.free_spots, [0])
        parking.spots = [0, 1]
        parking.find_all_adjacent_free_spots()
        self.assertEqual(parking.free_spots, [])
        parking.spots = [1, 0]
        parking.find_all_adjacent_free_spots()
        self.assertEqual(parking.free_spots, [])
        parking.spots = [1, 1]
        parking.find_all_adjacent_free_spots()
        self.assertEqual(parking.free_spots, [])

    def test_find_all_adjacent_free_spots_with_size_3(self) -> None:
        """Test the find_adjacent_free_spots method with a size of 3."""
        parking = Parking(3)
        parking.spots = [0, 0, 0]
        parking.find_all_adjacent_free_spots()
        self.assertEqual(parking.free_spots, [0, 1])
        parking.spots = [0, 0, 1]
        parking.find_all_adjacent_free_spots()
        self.assertEqual(parking.free_spots, [0])
        parking.spots = [0, 1, 0]
        parking.find_all_adjacent_free_spots()
        self.assertEqual(parking.free_spots, [])
        parking.spots = [1, 0, 0]
        parking.find_all_adjacent_free_spots()
        self.assertEqual(parking.free_spots, [1])
        parking.spots = [0, 1, 1]
        parking.find_all_adjacent_free_spots()
        self.assertEqual(parking.free_spots, [])
        parking.spots = [1, 0, 1]
        parking.find_all_adjacent_free_spots()
        self.assertEqual(parking.free_spots, [])
        parking.spots = [1, 1, 0]
        parking.find_all_adjacent_free_spots()
        self.assertEqual(parking.free_spots, [])
        parking.spots = [1, 1, 1]
        parking.find_all_adjacent_free_spots()
        self.assertEqual(parking.free_spots, [])
    # =============== find_all_adjacent_free_spots =================
    
    
    # =============== find_random_adjacent_spots =================    
    def test_find_random_adjacent_spots_with_size_0(self) -> None:
        """Test the find_random_adjacent_spots method with a size of 0."""
        parking = Parking(0)
        parking.spots = []
        parking.find_all_adjacent_free_spots()
        with self.assertRaises(ValueError):
            parking.find_random_adjacent_spots()
    
    def test_find_random_adjacent_spots_with_size_1(self) -> None:
        """Test the find_random_adjacent_spots method with a size of 1."""
        parking = Parking(1)
        parking.spots = []
        parking.find_all_adjacent_free_spots()
        with self.assertRaises(ValueError):
            parking.find_random_adjacent_spots()

    def test_find_random_adjacent_spots_with_size_2(self) -> None:
        """Test the find_random_adjacent_spots method with a size of 2."""
        parking = Parking(2)
        parking.spots = [0, 0]
        parking.find_all_adjacent_free_spots()
        random_spot = parking.find_random_adjacent_spots()
        self.assertEqual(random_spot, 0)

    def test_find_random_adjacent_spots_with_size_3(self) -> None:
        """Test the find_random_adjacent_spots method with a size of 3."""
        parking = Parking(3)
        parking.spots = [0, 0, 0]
        parking.find_all_adjacent_free_spots()
        random_spot = parking.find_random_adjacent_spots()
        self.assertIn(random_spot, [0, 1])
        parking.spots = [0, 0, 1]
        parking.find_all_adjacent_free_spots()
        random_spot = parking.find_random_adjacent_spots()
        self.assertEqual(random_spot, 0)
        parking.spots = [1, 0, 0]
        parking.find_all_adjacent_free_spots()
        random_spot = parking.find_random_adjacent_spots()
        self.assertEqual(random_spot, 1)
    # =============== find_random_adjacent_spots =================


    # =============== fill_adjacent_spots =================
    def test_fill_adjacent_spots_with_size_0(self) -> None:
        """Test the fill_adjacent_spot method with a size of 0"""
        parking = Parking(0)
        parking.spots = []
        parking.find_all_adjacent_free_spots()
        with self.assertRaises(ValueError):
            parking.fill_adjacent_spots(0)
            
    def test_fill_adjacent_spots_with_size_1(self) -> None:
        """Test the fill_adjacent_spot method with a size of 1"""
        parking = Parking(1)
        parking.spots = [0]
        parking.find_all_adjacent_free_spots()
        with self.assertRaises(ValueError):
            parking.fill_adjacent_spots(0)
    
    def test_fill_adjacent_spots_with_size_2(self) -> None:
        """Test the fill_adjacent_spot method with a size of 2"""
        parking = Parking(2)
        parking.spots = [0, 0]
        parking.find_all_adjacent_free_spots()
        parking.fill_adjacent_spots(0)
        self.assertEqual(parking.spots, [1, 1])
        parking.find_all_adjacent_free_spots()
        with self.assertRaises(ValueError):
            parking.fill_adjacent_spots(0)
    
    def test_fill_adjacent_spots_with_size_3(self) -> None:
        """Test the fill_adjacent_spot method with a size of 3"""
        parking = Parking(3)
        parking.spots = [0, 0, 0]
        parking.find_all_adjacent_free_spots()
        parking.fill_adjacent_spots(0)
        self.assertEqual(parking.spots, [1, 1, 0])
        parking.spots = [1, 0, 0]
        parking.find_all_adjacent_free_spots()
        parking.fill_adjacent_spots(1)
        self.assertEqual(parking.spots, [1, 1, 1])
        parking.find_all_adjacent_free_spots()
        with self.assertRaises(ValueError):
            parking.fill_adjacent_spots(0)
    # =============== fill_adjacent_spots =================


    # =============== fill_all_adjacent_spots =================
    def test_fill_all_possible_spots(self) -> None:
        """Test the fill_all_possible_spots method."""
        parking = Parking(2)
        parking.spots = [0, 0]
        parking.fill_all_possible_spots()
        self.assertEqual(parking.spots, [1, 1])  # Only two pairs should be filled
    # =============== fill_all_adjacent_spots =================


    # =============== calculate_occupied_spots =================
    def test_calculate_occupied_spots_with_size_0(self) -> None:
        """Test the calculate_occupied_spots method with a size of 0."""
        parking = Parking(0)
        parking.spots = []
        occupied = parking.calculate_occupied_spots()
        self.assertEqual(occupied, 0)
        
    def test_calculate_occupied_spots_with_size_1(self) -> None:
        """Test the calculate_occupied_spots method with a size of 1."""
        parking = Parking(1)
        parking.spots = [0]
        occupied = parking.calculate_occupied_spots()
        self.assertEqual(occupied, 0)
        parking.spots = [1]
        occupied = parking.calculate_occupied_spots()
        self.assertEqual(occupied, 1)
        
    def test_calculate_occupied_spots_with_size_2(self) -> None:
        """Test the calculate_occupied_spots method with a size of 2."""
        parking = Parking(2)
        parking.spots = [0, 0]
        occupied = parking.calculate_occupied_spots()
        self.assertEqual(occupied, 0)
        parking.spots = [0, 1]
        occupied = parking.calculate_occupied_spots()
        self.assertEqual(occupied, 1)
        parking.spots = [1, 0]
        occupied = parking.calculate_occupied_spots()
        self.assertEqual(occupied, 1)
        parking.spots = [1, 1]
        occupied = parking.calculate_occupied_spots()
        self.assertEqual(occupied, 2)
        
    def test_calculate_occupied_spots_with_size_5(self) -> None:
        """Test the calculate_occupied_spots method with a size of 5."""
        parking = Parking(5)
        parking.spots = [1, 1, 0, 1, 1]
        occupied = parking.calculate_occupied_spots()
        self.assertEqual(occupied, 4)
    # =============== calculate_occupied_spots =================


    # =============== calculate_occupancy_rate =================
    def test_calculate_occupancy_rate_with_size_1(self) -> None:
        """Test the calculate_occupancy_rate method with a size of 1."""
        parking = Parking(1)
        parking.spots = [0]
        occupancy = parking.calculate_occupancy_rate()
        self.assertEqual(occupancy, 0)
        parking.spots = [1]
        occupancy = parking.calculate_occupancy_rate()
        self.assertEqual(occupancy, 1)
        
    def test_calculate_occupancy_rate_with_size_2(self) -> None:
        """Test the calculate_occupancy_rate method with a size of 2."""
        parking = Parking(2)
        parking.spots = [0, 0]
        occupancy = parking.calculate_occupancy_rate()
        self.assertEqual(occupancy, 0)
        parking.spots = [0, 1]
        occupancy = parking.calculate_occupancy_rate()
        self.assertEqual(occupancy, 1/2)
        parking.spots = [1, 0]
        occupancy = parking.calculate_occupancy_rate()
        self.assertEqual(occupancy, 1/2)
        parking.spots = [1, 1]
        occupancy = parking.calculate_occupancy_rate()
        self.assertEqual(occupancy, 1)
        
    def test_calculate_occupancy_rate_with_size_5(self) -> None:
        """Test the calculate_occupancy_rate method with a size of 5."""
        parking = Parking(5)
        parking.spots = [1, 1, 0, 1, 1]
        occupancy = parking.calculate_occupancy_rate()
        self.assertEqual(occupancy, 4/5)
        
    def test_calculate_occupancy_rate_with_size_0(self) -> None:
        """Test the calculate_occupancy_rate method with a size of 5."""
        parking = Parking(0)
        with self.assertRaises(ValueError):
            parking.calculate_occupancy_rate()
    # =============== calculate_occupancy_rate =================
  

    # =============== __str__ method =================
    def test_str_method_with_size_0(self) -> None:
        """Test the __str__ method with a size of 0."""
        parking = Parking(0)
        parking.spots = []
        self.assertEqual(str(parking), "[]")
        
    def test_str_method_with_size_1(self) -> None:
        """Test the __str__ method with a size of 1."""
        parking = Parking(1)
        parking.spots = [0]
        self.assertEqual(str(parking), "[0]")
        parking.spots = [1]
        self.assertEqual(str(parking), "[1]")
        
    def test_str_method_with_size_2(self) -> None:
        """Test the __str__ method with a size of 2."""
        parking = Parking(2)
        parking.spots = [0, 0]
        self.assertEqual(str(parking), "[0, 0]")
        parking.spots = [0, 1]
        self.assertEqual(str(parking), "[0, 1]")
        parking.spots = [1, 0]
        self.assertEqual(str(parking), "[1, 0]")
        parking.spots = [1, 1]
        self.assertEqual(str(parking), "[1, 1]")
    # =============== __str__ method =================



if __name__ == "__main__":
    unittest.main()

