with open('teams.txt', 'w') as file:
    outfile = ""
    for index in range(5):
        team = input(f"Add team {index}: ")
        outfile += team + "\n"
    file.write(outfile)

with open('teams.txt', 'r') as file:
    for index in range(5):
        if index == 0 or index == 3:
            print(file.readline())
        else:
            file.readline()