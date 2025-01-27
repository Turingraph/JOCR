## user useflow

1.	open image
2.	edit image
3.	ocr 
4.	save result

## ui symbols
1.	B = button
2.	E = entry
3.	(S) = save

## Components type
1.	local_panel
2.	setting
3.	display

## local_panel attribute
1.	img_title: str
-	rename E
2.	img_history: linked_list< np.ndarray >
-	img_process and img_process_gray
3.	this_img: np.ndarray
-	do/undo B
4.	origin_img: np.ndarray
-	create-delete B
5.	apply_img: np.ndarray
5.	index: int
-	left-right B
6.	osd: str
-	osd B
7.	text: str
-	img_to_str B
-	text E

## display
1.	zoom: float
-	zoom B
2.	pan: float[2]
-	score bar
3.	img: int
-	img taps
-	index E
4.	show_img: int
-	img B
5.	img_tabs: int
-	left-right B
-	index E
6.	setting_id: int
-	setting_id B

## img_process function
1.	save
-	(S)
2.	remove-create border
-	E
3.	crop
-	B
4.	rotate
-	E

## img_process_gray B
1.	invert_img
2.	remove_noice
3.	thin_font
4.	thick_font

## img_process_gray
1.	dilate
-	2 E
2.	erode 
-	2 E
3.	opening
-	2 E
4.	canny
-	2 E
5.	contour_img
-	4 E
6.	threshold
7.	threshold_adapt
8.	sharp_filter2d
9.	mean_blur
10.	gauss_blur
11.	bilateral_blur

## ocr I
1.	save
-	(S)
2.	img_to_str
3.	osd

## ui (image setting)

+-----------+---------------------------+-----------------------+-----------------------+
| open(dir) | apply_img(p_00, p_01)[ok ]|save_img(dir,p_00,p_01)|save_ocr(dir,p_00,p_01)|
+-----------+---------------------------+-----------------------+-----------------------+
| ocr | img_00 | img_01 |																|
+---------------------------------------------------------------------------------------+
+-------------------------------+----------------------------+--------------------------+
|[ remove bor, create bor]		| rotate(angle) [ok, cancel] |[inv, rem, thin, think]   |
+-------------------------------+----------------------------+--------------------------+
|crop(x, y, w, h) [ok, cancel]	| [create bor, remove bor]	 | 							|
+-------------------------------+----------------------------+--------------------------+
+-----------------------+-----------------------+----------------------------------+---++
|"image 00" [r, x, <, >]|"imag|   " [ok, cancel]|Delete "image 01"? [ok, cancel]   | + ||
+-----------------------+-----------------------+----------------------------------+---++
|[<, >]	show(int mode) [origin, origray, this, apply] [ok, cancel] |				   ||				|
+---------------------------------------------------++-------------+-------------------++
|[+, -]												||								   ||
|													||								   ||
|													||	text						   ||
|													||								   ||
|			image									||								   ||
|													||								   ||
|													||---------------------------------++
|													|| osd (orientation and 			|
|													|| -script detectation) [osd ]		|
+---------------------------------------------------++									|
+---------------------------------------------------++----------------------------------+

## ocr ui

+---------------+---------------+---------------------+---------------------------------+
| psm(int mode) | oem(int mode) | timeout(int second) | 								|
+---------------+---------------+---------------------+---------------------------------+

## img_00 ui

+-------------------------------+----------------------------+--------------------------+
|[ remove bor, create bor]		| rotate(angle) [ok, cancel] |[inv, rem, thin, think]   |
+-------------------------------+----------------------------+--------------------------+
|crop(x, y, w, h) [ok, cancel]	| [create bor, remove bor]	 | 							|
+-----------------------+-------+----------------------------+--------------------------+
