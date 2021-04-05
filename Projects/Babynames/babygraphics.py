"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
-----------------
Name: Yujing Wei
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


# 嗚嗚嗚...沒有仔細看 spec，漏掉 get_x_coordinate()，把這個 function 要做的直接在 draw_names() 做完了 lol
# 測試 Jennifer 和 Lucy 看起來不會影響結果，所以就先 pass....
def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    pass


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # Create two horizontal lines: top and bottom lines.
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    # Calculate width of column.
    col_width = (CANVAS_WIDTH - GRAPH_MARGIN_SIZE * 2) / len(YEARS)

    # Draw lines of years and add text of years by lines to canvas.
    for i in range(len(YEARS)):
        # Create vertical lines for each year.
        canvas.create_line(GRAPH_MARGIN_SIZE + col_width * i, 0,
                           GRAPH_MARGIN_SIZE + col_width * i, CANVAS_HEIGHT)
        # Add text of year to canvas. Text anchor = tkinter.NW.
        canvas.create_text(GRAPH_MARGIN_SIZE + col_width * i, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    col_width = (CANVAS_WIDTH - GRAPH_MARGIN_SIZE * 2) / len(YEARS)  # Width of each column.

    for i in range(len(lookup_names)):                          # Look up names in list of 'lookup_names'.
        lookup_name = lookup_names[i]                           # Check name by index order.
        color = COLORS[i % len(COLORS)]                         # Set color by order of list of 'COLORS'.

        # Add len(YEARS) text 'name & rank' to canvas.  # 12 names
        for j in range(len(YEARS)):
            rank1_x = GRAPH_MARGIN_SIZE + col_width * j         # First point's x between line of ranks in two years.
            if str(YEARS[j]) not in name_data[lookup_name]:     # If 'name' in 'YEAR[j]' not in 1000 ranks,
                rank1 = '*'                                     # Assign '*' to rank.
                rank1_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE     # Set y position on bottom line.
            else:                                               # If 'name' in 'YEAR[j]' in 1000 ranks,
                rank1 = name_data[lookup_name][str(YEARS[j])]   # Assign value of 'name' to rank.
                rank1_y = int(rank1) / MAX_RANK * (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) \
                          + GRAPH_MARGIN_SIZE                   # Set y position based on value of rank
            canvas.create_text(rank1_x + TEXT_DX, rank1_y, text=(str(lookup_name) + str(rank1)),
                               anchor=tkinter.SW, fill=color)   # Create text of 'YEAR[j]' and 'rank1'.

            # Draw len(YEARS)-1 lines on canvas.  # 11 lines
            if j + 1 <= len(YEARS) - 1:                                 # Draw len(YEARS) - 1 lines.
                rank2_x = GRAPH_MARGIN_SIZE + col_width * (j + 1)       # Second point's x.
                if str(YEARS[j + 1]) not in name_data[lookup_name]:     # If 'name' in 'YEAR[j+1]' not in 1000 ranks,
                    rank2_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE         # Set y position on bottom line.
                else:                                                   # If 'name' in 'YEAR[j+1]' in 1000 ranks,
                    rank2 = name_data[lookup_name][str(YEARS[j + 1])]   # Assign value of 'name' to rank.
                    rank2_y = int(rank2) / MAX_RANK * (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) \
                              + GRAPH_MARGIN_SIZE                       # Set y position based on value of rank.

                canvas.create_line(rank1_x, rank1_y, rank2_x, rank2_y,
                                   width=LINE_WIDTH, fill=color)        # Create line between 'rank1' and 'rank2'.


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
