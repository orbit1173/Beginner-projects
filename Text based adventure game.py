while True:
    answer = input("What you like to play? (yes/no)")

    if answer.lower().strip() == "yes":

        answer = input("You reached a crossroad, Would you like yo go left or right?").lower().strip()
        if answer == "left":
            answer = input("You encounter a monster, would you like to run or attack?")

            if answer == "attack":
                print("That was not the greatest idea, you lost!")
            else:
                print("Good choice, you made it away safely")

                answer = input("You see a car and a plane, which one would you like to take? (Car/Plane)")

                if answer == "Plane":
                    print("Unfortunately you don't know how to fly a plane, you lost LOL")
                else:
                    print("You won!")

        elif answer == "right":
            print("You walked aimlessly to the right and fall on a patch of ice, you injure your legs and cannot continue. Game over!")
        
        else:
            print("Invalid choice, you lost!")

    else:
        print("That's too bad")
        break