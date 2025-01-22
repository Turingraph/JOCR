# List of directory

1.	`doc/`
2.	`tests/`
3.	`img_process/`
4.	`img_to_str/`
5.	`include/`
6.	`doc_user/`
7.	`table/`
8.	`img_observe/`
9.	`get_data/`
10.	`spell/`
11.	`frontend/`
12.	`frontend_img/`
13.	`language/`
14.	`latex/`

Note that the following directory are empty because this project is in very early state.
1.  `doc_user/`
2.  `table/`
3.  `img_observe/`
4.  `get_data/`
5.  `spell/`
6.  `frontend/`
7.	`frontend_img`
8.  `language/`
9.  `latex/`

# Open Closed Principle

* It is the coding guidance concept where it is recommended to code, such that programmer can
  add new feature to the code without modifying the existing code, 
  in order to avoid wasting time on rewrite the code and make unexpected bugs.
* The likely consequences of poor Open Closed code are Shotgun Surgery smell and Divergent Change smells.

You can learn more about Open Closed Principle and related concepts in this URL list.
1. Open Closed Principle
* https://www.freecodecamp.org/news/open-closed-principle-solid-architecture-concept-explained/
2. Shotgun Surgery
* https://refactoring.guru/smells/shotgun-surgery
3. Divergent Change 
* https://refactoring.guru/smells/divergent-change

# `include/`

This directory contains only Python files in OOP paradigm. 

The purpose of include directory is to help developers add new feature by 
1. Creating new files in `dir_a/`.
2. Import new file inside include as `dir_a.py`
3. Add new class method using function from new file.
4. Git commit 
5. Code testing by import class inside `tests/` directory.
6. Check the coding mistake, refactor the code if needed and Git commit.
* Read this https://refactoring.guru/refactoring/smells to learn more about coding mistake.

Note that some files inside include directory have same starting name, plus "_" and their additional short name. Such as
1. `img_process/`
2. `include/img_process.py`	      // Normal image class
3. `include/img_process_gray.py`	// Gray image class that inherit from normal image class.

It is recommended to write new files that only contains related similar functions 
and each function only has one purpose (follow the Single Responsibility Principle), 
in order to make sure that when the code is not works as expected for a specific task,
it is easier to debug and improve the existing feature without modifying unrelated features.

Another recommendation is to avoid using inheritance unless there is a clear reason to do so and parent class has a few unextended child class (child class that does not has another child class)
because every child classes are depending on parent class, which sometimes make adding new feature 
without modify the existing code becomes harder (violate Open Closed Principle). The clear exception are
* `img_process_gray` and `img_process_img` are only 2 children of `img_process` parent class.

This approach help developers code in SOLID manner.

Read this https://www.freecodecamp.org/news/solid-principles-single-responsibility-principle-explained/ to learn more about SOLID principle.

# `doc/` (documentation)

This directory contains only md documentation files. 
Read `doc/README.md` to learn more about doc directory.
Read `README.md` to learn more about our project, how to use it and how to contribute.

# `tests/`

The purpose of `tests/` directory is to
1. Test if the code works as expected.
2. Demonstrate how to use our Python script.

`tests/hello_world/` directory 
1. It is the only sub directory that contains only `h_0.py` and `h_1.py`.
2. It's purpose is to show how to import Python file from other directory.
3. It works by `sys.append(parent)`

Each directory of `tests/` contains 5 components
1. `img/`
* This subdirectory contains input image files.
2. `img_out/`
* This subdirectory contains output image directory.
3. `str_out/`
* This subdirectory contains string text output directory.
4. `img.py`
* `img/ -> img_out/`
* It displays and converts input image from `img/` to output image inside `img_out/`.
5. `str.py`
* `img/, img_out/ -> str_out/`
* It converts image from `img/` and/or `img_out/`, to create output text file inside `str_out/`.

Note that
1. Some directory have multiple subdirectorys and/or Python files with the same name but with different numbers, e.g.
* `01_index/` contains `img_out_00/` and `img_out_01/`
2. Some directory might not have all of the mentioned 5 components
* `fft/` directory does not contains `str.py` and `str_out/`

# `img_process` (image Processing)

This directory contains image processing Python script for processing image, in order to make the Pytesseract OCR output more reliable.

# `img_to_str` (image to string)

This directory contains Pytesseract script that is used for converting image with text to text file.

# `doc_user/` (User documentation)

This directory contains only user documentation files.

# `table/`

This directory contains the OCR and image processing script for get the csv data from table image. 

# `img_observe/`

This directory contains the image processing script for analyzing input image's pixels.
This directory help user to use img_process automatically.

# `get_data/`

This directory aims for helping the user collect data for 
1.	getting ocr text output as csv, txt and pdf.
2.	allowing developer develop more effective AI model include.
-	OCR model
-	Spelling checking language model
-	Text Language detection model
-   other NLP Model

# `spell/`

This directory contains NLP model for checking and correct OCR output.

# `frontend/`

This directory contains frontend React Typescript code.
Anyone can also recommend us about the better alternative frontend framework for our project.

# `frontend_img/`

This directory contains only image of frontend UI design.
Anyone can design frontend UI design for our project.

# `language/`

This directory contains the AI model that detect the language that the text input is based on.

# `latex/`

This directory contains the OCR model that detect the Latex and mathematical notations e.g. ratio, integration sign, vector symbol etc.
