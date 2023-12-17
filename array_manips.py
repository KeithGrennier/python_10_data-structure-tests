# Array Manips
task_num_names={
    1:"Accessing Elements",
    2:"Slicing",
    3:"Appending Elements",
    4:"Inserting at specific index",
    5:"Removing Elements",
    6:"Pop an element",
    7:"Sorting",
    8:"Reversing",
    9:"List Comprehension",
    10:"Filtering Elements"
}
def main():
    import logging
    logging.basicConfig(level=logging.DEBUG)

    def debugging_console(task:str,var1):
        logging.debug(task)
        logging.debug(var1)
        return

    """ TEMPLATE
    # 
    #code
    result=""
    debugging_console(task_num_names[],result)
    """
    arr_nums=[1,1,2,3,5,8,13]
    arr_str=['joe','jane,','bob','susie']

    # Begin Tasks
    # 1
    # Accessing Elements
    #code
    result=arr_nums[-2]

    debugging_console(task_num_names[1],result)

    # 2
    # Slicing
    #code
    result=arr_nums[1:3]
    debugging_console(task_num_names[2],result)

    # 3
    # Appending Elements
    #code
    result=arr_nums.copy()
    result.append(21)
    debugging_console(task_num_names[3],result)

    # 4
    # Inserting at specific index
    #code
    result=arr_str.copy()
    result.insert(3,'joseph')
    debugging_console(task_num_names[4],result)

    # 5
    # Removing Elements
    #code
    result=arr_nums.copy()
    result.remove(1)
    debugging_console(task_num_names[5],result)

    # 6
    # Pop an element
    #code
    result=arr_nums.copy()
    result.pop()
    debugging_console(task_num_names[6],result)

    # 7
    # Sorting
    #code
    result=arr_str.copy()
    result.sort()
    debugging_console(task_num_names[7],result)

    # 8
    # Reversing
    #code
    result=arr_nums.copy()
    result.reverse()
    debugging_console(task_num_names[8],result)

    # 9
    # List Comprehension
    #code
    result=[x**2 for x in arr_nums]
    debugging_console(task_num_names[9],result)

    # 10
    # Filtering Elements
    #code
    result=list(filter(lambda x: x%2 == 0,arr_nums))
    debugging_console(task_num_names[10],result)

if __name__ == "__main__":
    main()