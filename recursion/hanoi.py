def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
    else:
        tower_of_hanoi(n - 1, source, auxiliary, destination)
        print(f"Move disk {n} from {source} to {destination}")
        tower_of_hanoi(n -1, auxiliary, destination, source)
        
if __name__ == "__main__":
    tower_of_hanoi(3, 'A', 'C', 'B') # Move disk 1 from A to C
                                      # Move disk 2 from A to B
                                      # Move disk 1 from C to B
                                      # Move disk 3 from A to C
                                      # Move disk 1 from B to A
                                      # Move disk 2 from B to C
                                      # Move disk 1 from A to C