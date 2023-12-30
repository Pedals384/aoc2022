"""
Task One: Find total calories carried by the elf carrying the most 
calories based on a list of calorie counts for snacks.
Task Two: Find total calories carried by the three elves carrying the
highest number of calories. 
"""

def read_text_file(path: str) -> list[str]:
    """Read text file.

    Reads an input text file into a list of strings. Removes trailing
    new line characters.

    Parameters
    ----------
    path : str
        path to input text file.

    Returns
    -------
    list: [str]
        text file content in a list of strings

    """
    with open(path, "r") as f:
        return [line.strip("\n") for line in f.readlines()]

    
DATAPATH = "input.txt"

calories = read_text_file(DATAPATH)


def get_elf_calories(calories):
    """Compiles the calories for each snack carried by an elf into a 
    single list, then appends it to a list of total calories carried
    by all elves. 

    Args:
        calories (list): Input of a list of strings of calorie counts,
        with each elf separated by a blank line. 

    Returns:
        all_calories (list): List of lists containing the calories for
        each elf. 
    """
    
    all_calories = []
    elf_calories = []
    
    for line in calories:

        # any totals added to the list for that elf's calories
        if line != "":
            elf_calories.append(int(line))
        
        # line breaks separating between each elf
        if line == '':
            all_calories.append(elf_calories)
            # reset elf calories to empty list for next elf
            elf_calories = []

    return all_calories
    
# call function to set the variable for finding highest cals function
total_calories = get_elf_calories(calories)


def find_highest_cals(total_calories):
    """ Takes the list of lists from get_elf_calories and creates a 
    list of the sum of each elf's total calories.

    Args:
        total_calories (list of lists): Each list contains integer 
        values of the calorie count for each elf.
    """
    sum_cals = []
    for elf_calories in total_calories:
        sum_cals.append(sum(elf_calories))
    
    # print results
    print(f" The most calories carried by one elf is:",
          {max(sum_cals)}
    )
    
    # part 2 - sort lit by highest calorie values
    sum_cals.sort(reverse=True)

    top_three_cals = sum_cals[0] + sum_cals[1] + sum_cals[2]

    # print part 2 results
    print(f" The total calories carried by the top 3 elves is:",
        {top_three_cals}
    )
    
find_highest_cals(total_calories)


