from datetime import datetime, timedelta
import random

# Generate a grid with random colors
def generate_commit_grid():
    days = 7  # Number of days in a row
    weeks = 52  # Number of weeks in the grid
    grid = []

    for week in range(weeks):
        week_data = []
        for day in range(days):
            # Randomize commit intensity (0 for no commits, higher values for more commits)
            intensity = random.randint(0, 4)
            week_data.append(intensity)
        grid.append(week_data)
    return grid

# Write grid to an HTML file (or SVG)
def write_grid_html(grid):
    with open("commit_grid.html", "w") as file:
        file.write("<html><body><table>")
        for week in grid:
            file.write("<tr>")
            for day in week:
                color = {
                    0: "#ebedf0",  # No commits
                    1: "#c6e48b",
                    2: "#7bc96f",
                    3: "#239a3b",
                    4: "#196127"
                }[day]
                file.write(f'<td style="width: 10px; height: 10px; background-color: {color};"></td>')
            file.write("</tr>")
        file.write("</table></body></html>")

if __name__ == "__main__":
    grid = generate_commit_grid()
    write_grid_html(grid)
