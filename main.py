print("Welcome to my first game :)")
name = input("What is your name?  ")
age = int(input("What is your age?  "))


health = 10

if age >= 18:
    print("You are able to play the game!")
    wants_to_play = input("Do you want to play?  ").lower()
    if wants_to_play == 'yes':
        print("You are starting out with",health ,"health.")
        print("Let's play!! ")

        right_left = input("First choice => Right or Left?  ").lower()
        if right_left == 'left':
            ans = input("Nice, you see a path that leads to a pond... Do you swim across, or walk around? Swim/Walk  ").lower()
            if ans == "Walk":
                print("You walked around the pond and reached the other side of the lake")
            elif ans == "Swim":
                print("You swim across, but you get covered with leeches. You lose 5 health.")
                health -= 5
            
            ans = input("You see a path that leads to a bigger road, and path that leads to a forest. Which do you choose? Road/Forest ").lower()
            if ans == 'forest':
                print("You get attacked by wasps and lost 5 health")
                health -=5

            elif ans == 'road':
                print('You take the road and follow it to the city')

            if health <=0:
                print("You now have 0 health and you lost the game...")
            else:
                print("You have survived!.... You win!")

        else:
            print("You fell down the hole and lost...")
    else: 
        print("K, bye!")

else: 
    print("You are not old enough to play.")