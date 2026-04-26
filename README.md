# py_fds_project_copy
A project originally written as a solution to an FDS assignment in C++, now rewritten as a Python script (with minor changes) for another assignment

---
Original task summary:
- crates are provided via the 'crates.txt' file in the format 'weight uuid'
- a warehouse should be created with 10 shelves, an arrival queue and a sorting queue
- the shelves form a node-backed linked list
- the crates are to be inserted on the shelves such that:
  <ol type="1">
    <li>there are at most 4 crates per shelf</li>
    <li>the total weight must be at most 1000kgs</li>
  </ol>
- the crates in the file are sorted in such a way as to allow a valid insertion without sorting
- the shelves are outputted to the standard output as a regular linked list
- a validation method is executed and printed to the standard output

Core components:
- Crate - currently a tuple, but might change in order to implement inheritance
- Shelf - a storage for crates that also serves as a linked list node
- SteelShelf - child of Shelf with higher capacity and weight limit
- UnsortedSteelShelf - child of SteelShelf which can store crates in any order regardless of weight
- ArrivalQueueNode - linked list node implemented as a queue in the Warehouse
- Warehouse - container class for all other modules

---

### How to use
#### Method 1:
- open .\py_fds_project_copy\run.cmd
- when prompted, enter the file name
- if left blank, the default file name of 'crates.txt' will be used

#### Method 2:
- open the folder in terminal (cmd/ps)
- enter the following command: py -m main
- by default, the file 'crates.txt' will be used
- to process a different file, use: py -m main -filename 'filename.txt'

---

### Requirements met
- The code in the python modules should abide all python convention - self-explanatory
- There should be a proper structure of the project - all classes/tests are located in separate files
- All public methods should be properly documented with docstrings
- The program should have functionality that reads from/writes to a file
- The name(s) of the file(s) and/or other important input should not be hard-coded
- The project should include at least 100 lines of code
- All of the project files should abide the pep8 rules
- Unit tests should be included, covering at least 50% of the code
- Each class should have only non-public members, the proper getters/setters and if needed validation of the data in the setters
- There should be at least one operator that is overloaded in at least one of the classes
- The project should include some manipulation of the data (can be solved by custom implementation of the "sorting floor")
- All python modules should include a comment at the beginning of the file explaining in short what the file contains
- Classes forming three-level hierarchy exploring inheritance (“is-a relationship”) (might require redesign)
- The coverage report should not contain information about the coverage of unit test files
