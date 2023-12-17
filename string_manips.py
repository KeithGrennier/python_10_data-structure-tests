# String Manipulation
task_num_names={
    1:"Concate",
    2:"Length",
    3:"Substring",
    4:"Upper and Lower Case",
    5:"Replace",
    6:"Split",
    7:"Strip Whitespace",
    8:"Find Substring",
    9:"Count occurences",
    10:"Format String"
}
def main():
    import logging

    logging.basicConfig(level=logging.DEBUG)

    def debugging_console(task,var1):
        logging.debug(task)
        logging.debug(var1)
        return
    # 1
    # Concate
    str1 = 'Hello'
    str2 = 'World'

    result= str1 + " " + str2

    debugging_console(task_num_names[1],result)
    # 2
    # Length
    result = len(str1)
    debugging_console(task_num_names[2],f"Length {result}")

    # 3
    # Substring
    result = str1.find("ell")
    debugging_console(task_num_names[3],f"Subtring found at {result}")

    # 4
    # Upper and Lower Case
    result_upper=str1.upper()
    result_lower=str2.lower()
    result=result_upper+result_lower
    debugging_console(task_num_names[4],result)
    # debugging_console(task_num_names[4],result_lower)

    # 5
    # Replace
    task="Replace"
    concate= str1+ " "+ str2
    result_replace = concate.replace(" World",", there!")
    debugging_console(task_num_names[5],result_replace)

    # 6
    # Split
    task="Split"
    sentence = "The rabbit runs faster than the fox."
    result_words = sentence.split()
    debugging_console(task_num_names[6],result_words)

    # 7
    # Strip Whitespace
    task="Whitespace"
    white_space=" What is up   "
    result_white_space=white_space.strip()
    debugging_console(task_num_names[7],result_white_space)

    # 8
    # Find Substring
    task="Substring"
    result_substring=sentence.find("faster")
    debugging_console(task_num_names[8],"Substring found at {result_substring}.")
    # 9
    # Count occurences
    task="Count Occurances"
    result_count = sentence.count("the")
    debugging_console(task_num_names[9],f"the found {result_count} times.")
    # 10
    # Format String
    task="Format String"
    person="John Doe"
    age = 28
    result_format= "The unsub has our {}, age {}.".format(person,age)
    debugging_console(task_num_names[10],result_format)

if __name__ =="__main__":
    main()