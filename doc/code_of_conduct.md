# Introduction

This file describes about the coding convention of our project.

# File, Variable, OOP Class and Folder Naming Convention

Rule of naming file and folder in our project.
1.	Every file names should contain only lower case letter.
-	1st Correct Example: `my_folder/`
-	1st Wrong Example: `My_Folder/`, `my_Folder` etc.
-	2nd Correct Example: `hello_world.py`
-	2nd Wrong Example: `Hello_world.py/`, `Hello_World.py` etc.
-	3rd Correct Example: `path`
-	3rd Wrong Example: `Path` etc.
2.	File names that have multiple words should separated by underscores (_)
-	1st Correct Example: `my_folder/`
-	1st Wrong Example: `my-folder/`, `my folder`, `myfolder` etc.
-	2nd Correct Example: `hello_world.py`
-	2nd Wrong Example: `hello-world.py`, `helloworld.py`, `hello world.py` etc.
-	3rd Correct Example: `rotate_matrix`
-	3rd Wrong Example: `rotatematrix` etc.
3.	Don't use characters that is not English Alphabet and number (special characters) and underscores (_)
-	Examples of special characters: space ( ), slash (/), hyphens (-), dollar sign ($), ko (ก), ha (๕) etc.
4.	Use `_YYYYMMDD` as date format for the naming convention.
-	1st Correct Example: `my_folder_20241231/`
-	1st Wrong Example: `my_folder_2024_12_31/`, `my_folder_31122024`, `my_folder_31dec2024`, `my_folder_2024dec31` etc.
-	2nd Correct Example: `hello_world_20241231.py`
-	2nd Wrong Example: `hello_world_2024_12_31/`, `hello_world_31122024`, `hello_world_31dec2024`, `hello_world_2024dec31` etc.
5.	`README.md` is the only file that does not following 1st and 2nd rules.
6.  Every file name that starts with `__`, means that file is unusable, and is in the development process.
-	1st Example: `__deployment.md` means that our deployment documentation is under the development process.
-	2nd Example: `__img_to_str.py` means that our OCR Python script (`img_to_str.py`) is under the development process.
7.  If the file is not the utility file and contains an OOP class, then both file and class have the same name.
-	1st Example: `img_process_img` class belong to `include/imgprocess_img.py`.
-	2nd Example: `table` class belong to `include/table.py`.
8.	The counting should always start with 00.
-	Correct Example: `vec_00`, `vec_01`, `vec_02`
-	Wrong Example: `vec00`, `vec01`, `vec02` etc.
-	Wrong Example: `vec_01`, `vec_02`, `vec_03` etc.
-	Wrong Example: `vec_0`, `vec_1`, `vec_2` etc.
-	Wrong Example: `vec01`, `vec02`, `vec03` etc.
9.  Every variable that intended to not be modified, should only contains capital letter.
-	1st Correct Example: `PI = 3.14159`
-	1st Wrong Example: `pi = 3.14159`, `Pi = 3.14159`
-	2nd Correct Example: `EULER = 2.718`
-	2nd Wrong Example: `euler = 2.718`, `Euler = 2.718` etc.
-	3rd Correct Example: `GRAVITY = 9.81`
-	3rd Wrong Example: `gravity = 9.81`
-	4th Correct Example: `SPEED_OF_LIGHT = 299792458`
-	4th Wrong Example: `SPEEDoFlIGHT = 9.81`, `speed_of_light = 9.81`
10.	It is OK to use Library that does not follow our coding convention.
-	Example: `cv2.adaptiveThreshold`, `cv2.morphologyEx`, 

Here are the additional recommended learning resource.
1.	STOP! Don't Name That File Without First Watching This Video.
*	https://youtu.be/Wu0CxdflECY?si=Wn8Qr2um1QBdgiNv
2.	Naming Things in Code
*	https://youtu.be/-J3wNP6u5YU?si=DG5mLTEiOqmkUgrY
3.	VS Code tips — Convert to Snake Case
*	https://youtu.be/owexcF4a8qg?si=c42N9fxeJuclpzbO
4.	How to make every file names have only lower case recursively ?
*   https://stackoverflow.com/questions/152514/how-do-i-rename-all-folders-and-files-to-lowercase-on-linux

# Naming Meaning

Meaning
1.	img  = input image
2.	ocr  = Optical Character Recognition
3.	path = path of input image
4.	parent = parent directory
5.	str_out = OCR string output text
6.	osd_out = output of pytesseract.image_to_osd (Orientation and Script Detection)
7.	img_out = image output
8.	vec = vector
9.	osd = Orientation and Script Detection

# Python Function Naming Convention

1.	Every Function name don't have capital letter.
-	Correct Example: `def add(num_00: int, num_01: int) -> int:`
-	Wrong Example: `def Add(num_00: int, num_01: int) -> int:` etc.
2.	Function names that have multiple words should separated by underscores (`_`).
-	Correct Example: `def dot_product(vec_00: np.ndarray, vec_01: np.ndarray) -> np.ndarray:`
-	Wrong Example: `def dotproduct(vec_00: np.ndarray, vec_01: np.ndarray) -> np.ndarray:` etc.
3.	Don't use characters that is not English Alphabet and number (special characters) and underscores (`_`)
-	Examples of special characters: space (` `), slash (`/`), hyphens (`-`), dollar sign (`$`), ko (`ก`), ha (`๕`) etc.
4.	All parameter inside the function following our naming convention rule.
-	Correct Example: `def dot_product(vec_00: np.ndarray, vec_01: np.ndarray) -> np.ndarray:`
-	Wrong Example: `def dot_product(vec_0: np.ndarray, vec_1: np.ndarray) -> np.ndarray:`
-	Wrong Example: `def dot_product(vec_1: np.ndarray, vec_2: np.ndarray) -> np.ndarray:`
-	Wrong Example: `def dot_product(vec_01: np.ndarray, vec_02: np.ndarray) -> np.ndarray:`
5.	Always specify the type of input parameter and output.
-	Correct Example: `def dot_product(vec_00: np.ndarray, vec_01: np.ndarray) -> np.ndarray:`
-	Wrong Example: `def dot_product(vec_00: np.ndarray, vec_01: np.ndarray):`
-	Wrong Example: `def dot_product(vec_00, vec_01) -> np.ndarray:`
-	Wrong Example: `def dot_product(vec_00, vec_01):`
6.	Use only space (` `), (not tap (`\t`)), to make space between `def`, parameter, parameter type and output type
-	Correct Example: `def dot_product(vec_00: np.ndarray, vec_01: np.ndarray) -> np.ndarray:`
-	Wrong Example: `def		dot_product(vec_00: np.ndarray, vec_01: np.ndarray) -> np.ndarray:`
-	Wrong Example: `def dot_product(vec_00: np.ndarray, vec_01: np.ndarray)->np.ndarray:`
-	Wrong Example: `def dot_product(vec_00:np.ndarray, vec_01: np.ndarray) -> np.ndarray:`
-	Wrong Example: `def dot_product(vec_00: np.ndarray, vec_01:		np.ndarray) -> np.ndarray:`
7.	No space between the previous character and colon (`:`)
-	Correct Example: `def dot_product(vec_00: np.ndarray, vec_01: np.ndarray) -> np.ndarray:`
-	Wrong Example: `def dot_product(vec_00: np.ndarray, vec_01: np.ndarray) -> np.ndarray :`
-	Wrong Example: `def dot_product(np.ndarray:vec_0, np.ndarray :vec_1) -> np.ndarray:`
-	Wrong Example: `def dot_product(np.ndarray : vec_0, np.ndarray : vec_1) -> np.ndarray:`
8.	No space between the previous character and comma (`,`)
-	Correct Example: `def dot_product(vec_00: np.ndarray, vec_01: np.ndarray) -> np.ndarray:`
-	Wrong Example: `def dot_product(vec_00: np.ndarray,vec_01: np.ndarray) -> np.ndarray:`
-	Wrong Example: `def dot_product(vec_00: np.ndarray ,vec_01: np.ndarray) -> np.ndarray:`
9.	When there is more than 2 parameters, dev should write the 2 indentation with one parameter per a line.
-	1st Correct Example: 
```
def quick_sort(
		ls: list, 
		start: int = 0, 
		stop: int | None = None, 
		is_rand_pivot: bool = False
	) -> void:
	# Activate Quick sort using O(n log(n)) time and O(log(n)) space
```
-	1st Wrong Example: 
```
def quick_sort(ls: list, 
		start: int = 0, 
		stop: int | None = None, 
		is_rand_pivot: bool = False
	) -> void:
	# Activate Quick sort using O(n log(n)) time and O(log(n)) space
```
-	1st Wrong Example: 
```
def quick_sort(
		ls: list, 
		start: int = 0, 
		stop: int | None = None, 
		is_rand_pivot: bool = False
		) -> void:
	# Activate Quick sort using O(n log(n)) time and O(log(n)) space
```
-	1st Wrong Example: 
```
def quick_sort(ls: list, start: int = 0, stop: int | None = None, is_rand_pivot: bool = False) -> void:
	# Activate Quick sort using O(n log(n)) time and O(log(n)) space
```
-	1st Wrong Example: 
```
def quick_sort(
	ls: list, 
	start: int = 0, 
	stop: int | None = None, 
	is_rand_pivot: bool = False
	) -> void:
	# Activate Quick sort using O(n log(n)) time and O(log(n)) space
```
-	1st Wrong Example: 
```
def quick_sort(
	ls: list, 
	start: int = 0, 
	stop: int | None = None, 
	is_rand_pivot: bool = False) -> void:
	# Activate Quick sort using O(n log(n)) time and O(log(n)) space
```
-	2nd Correct Example: `def dot_product(vec_00: np.ndarray, vec_01: np.ndarray) -> np.ndarray:`
-	2nd Wrong Example: 
```
def dot_product(
		vec_00: np.ndarray, 
		vec_01: np.ndarray
	) -> np.ndarray:
```


# Additional Python Coding Convention

1.	There is always space between any characters (include number and `[`, `]`, `(`, `)`, `{` and `}`) with `+`, `-`, `*`, `/`, `%`, `=`, `|`, `**` and `->`
-	1st Correct Example: `vec_y = vec_00 + vec_01`
-	1st Wrong Example: `vec_y = vec_00 +vec_01`
-	1st Wrong Example: `vec_y = vec_00+ vec_01`
-	1st Wrong Example: `vec_y = vec_00+vec_01`
-	1st Wrong Example: `vec_y =vec_00 + vec_01`
-	1st Wrong Example: `vec_y=vec_00 + vec_01`
-	1st Wrong Example: `vec_y=vec_00 + vec_01`
-	2nd Correct Example: `def dot_product(vec_00: np.ndarray, vec_01: np.ndarray) -> np.ndarray:`
-	2nd Wrong Example: `def dot_product(vec_00: np.ndarray, vec_01: np.ndarray) ->np.ndarray:`
-	2nd Wrong Example: `def dot_product(vec_00: np.ndarray, vec_01: np.ndarray)-> np.ndarray:`
-	2nd Wrong Example: `def dot_product(vec_00: np.ndarray, vec_01: np.ndarray)->np.ndarray:`
-	3rd Correct Example: `ls = ["Mumu", "CheChe", "Tata"]`
-	3rd Wrong Example: `ls =["Mumu", "CheChe", "Tata"]`
-	3rd Wrong Example: `ls= ["Mumu", "CheChe", "Tata"]`
-	3rd Wrong Example: `ls=["Mumu", "CheChe", "Tata"]`
2.	There is no space between any characters (include number) with `[`, `]`, `(`, `)`, `{` and `}`
-	Correct Example: `ls = ["Mumu", "CheChe", "Tata"]`
-	Wrong Example: `ls = [ "Mumu", "CheChe", "Tata"]`
-	Wrong Example: `ls = ["Mumu", "CheChe", "Tata" ]`
-	Wrong Example: `ls = [ "Mumu", "CheChe", "Tata" ]`
3.	Use `'` for single character string and `"` for multiple characters string.
-	1st Correct Example: `my_grade = 'A'`
-	1st Wrong Example: `my_grade = "A"`
-	2nd Correct Example: `my_name = "CheChe"`
-	2nd Wrong Example: `my_name = 'CheChe'`

# Non Serious Rule

Non Serious Rule list

1.	1st, 2nd and 3rd rules of Additional Python Coding Convention section
2.	6th, 7th, 8th and 9th rules of Python Function Naming Convention section

Note that it is allow to violate some of our coding convention rule in the "Non Serious Rule" list, but it is recommended to follow our rule as much as possible.
Anyone who want to contribute our project can help us write script that convert our code, such that it follow our coding convention automatically.

# Additional Resource

Here is the following resource to learn more about our project
1.	`README.md` about our project.
1.	`doc_user/` about how to user our project. It is under development process.
3.	`doc/README.md` about meaning of each md files in `doc/` directory.
4.	`doc/folder_structure.md` about the folder structure of our project.
