"""
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""

from magic8ball.fortunes import Magic8Ball


def main():
    """
    Get some wise text and print it out.
    """
    fortune = Magic8Ball.tell_fortune()  # get a random fortune
    print(fortune)  # print it out


if __name__ == "__main__":
    # run the main function
    main()
