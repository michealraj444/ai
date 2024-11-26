from collections import defaultdict

class Solution:
    def __init__(self, head_name):
        self.family = defaultdict(list)
        self.head = head_name
        self.dead = set()

    def birth(self, p_name, c_name):
        self.family[p_name].append(c_name)

    def death(self, name):
        self.dead.add(name)

    def inheritance(self):
        self.ans = []
        self.depth_search(self.head)
        return self.ans

    def depth_search(self, current):
        if current not in self.dead:
            self.ans.append(current)
        for child in self.family[current]:
            self.depth_search(child)


def main():
    head_name = input("Enter the name of the family head: ")
    ob = Solution(head_name)

    while True:
        print("\nOptions: ")
        print("1. Birth")
        print("2. Death")
        print("3. Show Inheritance Order")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            parent = input("Enter parent's name: ").strip()
            child = input("Enter child's name: ").strip()
            ob.birth(parent, child)
            print(f"Child '{child}' born to '{parent}'.")
        elif choice == "2":
            name = input("Enter the name of the person to mark as dead: ").strip()
            ob.death(name)
            print(f"'{name}' is marked as deceased.")
        elif choice == "3":
            print("Inheritance Order:", ob.inheritance())
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
