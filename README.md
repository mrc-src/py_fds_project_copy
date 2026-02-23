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
