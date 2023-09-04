import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path # adds source with movie None to the path, to start
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.

    To clarify:
        node.state = type: string, what: actor id
        node.parent = type: node, what: the node that came previous to
        node.action = type: string, what: movie id
    """

    # check if actors are the same, then no solution
    if source == target:
        raise Exception("You need to select two different actors!")

    # create an empty set for visited nodes
    explored_set = set()

    # start with a frontier that contains the initial state
    frontier = QueueFrontier() # shortest path based on breath search
    node = Node(state=source, parent=None, action=None)
    frontier.add(node) # add the node for source action

    #Repeat
    while True:
        #if the frontier is empty, then no solution
        if frontier.empty():
            return None

        # remove a node from the frontier
        r_node = frontier.remove()

        # if node contains a goal state, return the solution
        if r_node.state == target:
            path = [] #creates path to return

            while r_node.parent is not None:
                path.append((r_node.action, r_node.state)) # add movie id and actor id to path
                r_node = r_node.parent # "resets" the node, entering the loop again
                # the loop will finishe when parent is None, as set in the initial node
            path.reverse() # reverse the path, from source to target
            return path # return the path

        else:
            #adds visited node to set
            explored_set.add((r_node.state, r_node.action)) #adds to actor and movie id

            # if goal state not found, adds neighboors from node to frontier
            for movie_id, person_id in neighbors_for_person(r_node.state):
                if not (person_id, movie_id) in explored_set: #only adds to frontier if not already explored to prevent loop
                    #creates new node to add to the frontier
                    # Reminder: the state is the person id, the parent is the current node, and the action is the movie_id
                    n_node = Node(state=person_id, parent=r_node, action=movie_id)
                    frontier.add(n_node)


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()