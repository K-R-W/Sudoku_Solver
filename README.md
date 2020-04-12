# Sudoku_Solver
A graphic program to solve an unsolved sudoku, and return all possible solution to input set

## Pre-Requisites
tkinter and numpy are used in this project. tkinter should already be available as an internal module in your python build.
**numpy version 1.17.4** was used when this project was last updated
to check your numpy version
```bash
python -c "import numpy; print(numpy.version.version)"
```
to install numpy:
```bash
pip install numpy
```
## Usage
Clone the repo, or raw scrape the sudoku_solver.py file. run the file directly
```python
python sudoku_solver.py
```
the code should run. If it doesn't, report the issue on this [email](mailto:kaustubhwankhede@gmail.com)   
If everything works per plan, you should see the following window
![Image of Blank Sudoku](https://github.com/K-R-W/Sudoku_Solver/blob/master/sample_images/blank_sudoku.png)

Now enter your sudoku numbers. The blocks which are empty in the sudoku should be left empty in the window as well.

![Image of filled sudoku](https://github.com/K-R-W/Sudoku_Solver/blob/master/sample_images/filled_sudoku.png)

Now press submit, and you shall get another window with all possible solutions to the input sudoku.

![Image of result](https://github.com/K-R-W/Sudoku_Solver/blob/master/sample_images/result.png)

Happy solving!
