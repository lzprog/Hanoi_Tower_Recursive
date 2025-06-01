class Tower:
    def __init__(self, vet):
        self.tower = vet

class Hanoi_Tower:
    def __init__(self):
        self.tower_1 = None
        self.tower_2 = None
        self.tower_3 = None
        self.steps_count = 0

    def init_tower(self, n):
        new_tower1 = Tower([])
        while(n != 0):
            new_tower1.tower.append(n)
            n = n - 1
        new_tower2, new_tower3 = Tower([]), Tower([])
        self.tower_1 = new_tower1
        self.tower_2 = new_tower2
        self.tower_3 = new_tower3
      
    def push_to_stack(self, fromTower, toTower):
        disc = fromTower.tower.pop()
        toTower.tower.append(disc)

    def play_tower(self, n, tower_1, tower_2, tower_3):
        self.steps_count = self.steps_count + 1
        if(n == 1):
            self.show_tower()
            self.push_to_stack(tower_1, tower_3)
            self.show_tower()
        else:
            self.show_tower()
            self.play_tower(n - 1, tower_1, tower_3, tower_2)
            self.push_to_stack(tower_1, tower_3)
            self.show_tower()
            self.play_tower(n - 1, tower_2, tower_1, tower_3)


    def show_tower(self):
        print(f"T1: {self.tower_1.tower}")
        print(f"T2: {self.tower_2.tower}")
        print(f"T3: {self.tower_3.tower}")
        print("-" * 30)

tower_of_hanoi = Hanoi_Tower()
n = int(input("Quantos discos voce deseja? "))
tower_of_hanoi.init_tower(n)
steps = tower_of_hanoi.play_tower(n, tower_of_hanoi.tower_1, tower_of_hanoi.tower_2, tower_of_hanoi.tower_3)
print("\nEu precisei de {%d} passos." % (tower_of_hanoi.steps_count))
