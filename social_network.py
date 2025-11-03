# Person class
class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []  # list of Person objects

    def add_friend(self, friend):
        # Add friend if they are not already in the list
        if friend not in self.friends:
            self.friends.append(friend)


# SocialNetwork class
class SocialNetwork:
    def __init__(self):
        self.people = {}  # dictionary: {name: Person instance}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network!")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        # Check if both people exist in the network
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        # Add each other as friends (bidirectional)
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names)}")


# test
if __name__ == "__main__":
    network = SocialNetwork()

    # Add people
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    # Test duplicate person
    network.add_person("Alex")

    # Create friendships
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Jordan", "Johnny")  # error case
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    print("\n--- Social Network ---")
    network.print_network()


"""
memo
Using a graph to represent a social network is the most natural and efficient structure because relationships between users are bidirectional and dynamic. Each person can connect to many others, and those connections can form complex webs of relationships — a perfect example of a graph with nodes and edges. Lists or trees can only represent one-way or hierarchical relationships, which would make mutual friendships and network traversal much harder to manage.

In this implementation, the adjacency list model allows quick lookups of each user’s friends using a dictionary. This structure is memory-efficient, since we only store direct friendships rather than all possible connections. It also supports fast updates — adding new people or creating friendships only requires modifying small parts of the graph. However, because the friendships are stored in lists, checking for duplicates or printing all connections takes linear time relative to the number of friends each person has.

The main trade-off is between simplicity and scalability. For small to medium-sized networks, using lists within an adjacency list is fast and easy to understand. But for very large social platforms, more advanced data structures like hash sets or graph databases might be needed for faster searching and relationship queries. Overall, this design balances clarity, efficiency, and real-world applicability while illustrating how graphs can model social interactions.
"""
