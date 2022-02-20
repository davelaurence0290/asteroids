# Asteroids
David Smith
Key Technology, Programming Exercise.
19/02/2022

##Problem Statement
You are part of a mission to explore a group of asteroids. These asteroids are well-behaved in that they all move in the same plane and are static to one another. A spacecraft, equipped with measuring devices, will land on one of the asteroids to perform all sorts of experiments. It is your task to choose the ideal asteroid to land on such that from that vantage point the system can monitor the whole asteroid constellation within the smallest viewing angle.

Input:
A text file. The first line contains a single integer, N the number of asteroids. The following N lines contain integer X and Y coordinates of the asteroids separated by spaces.

Output:
On the console. Two integers, X and Y, separated by a space, that are the coordinates of the ideal asteroid to land on.

Example:

Input:<br />
3<br />
0 0<br />
1 1<br />
10 0<br />

Output:<br />
10 0


Format:
Please complete this task in either Python or C++. In both cases you should provide the full source code (if you have multiple source files, use: tar cvzf solution.tgz &lt;source dir&gt;, to create a zipped archive file). The source code is everything you created to complete this project according to good practices.

In case your solution is in Python, it should be executable using the command: python solution.py &lt;input file&gt; (Python version 2.7 or higher, please specify which version you have used). If you require external modules, they have to be installable using pip.

In case your solution is in C++, it should be compilable with the command: g++ -o solution solution.cpp (g++ version 4.7.2 or higher, please specify which version you have used), and executable as: solution &lt;input file&gt;. If you require external libraries, please be specific. External commercial libraries are not allowed.<br />

---

##Solution

The problem statement strikes me as a very relevant case for Key Technology and its applications for detection and object sorting:
1. Examining a field of objects in a single plane, similar to our line of sorters which utilize belts on which all product is stabilized and is static to one another.
2. Inspection of a single object in the field of view: identified by many data points on its surface, and on which we might be interested in looking at the outer bounds.

After thinking about a way to find the 'asteroid' with the lowest vantage angle when observing all others, several observations led me down the chosen path:
1. The asteroid of interest will lie on the outer polygon which includes and contains all others.
2. The enclosing polygon which contains all asteroids will be convex.

Therefore, if I can find a way to solve for this convex hull polygon, then all I would need to do is check which point (asteroid) has the minimum angle, and present it through the console. This point would intuitively be the point from which all other points are viewable, at the minimum angle.

Luckily, after a brief search, many algorithms exist to find the convex hull of a set of points. I settled on using the Graham's Scan method, which can be found here:
[Link]https://en.wikipedia.org/wiki/Graham_scan

Its steps include:
1. Find the lowest point in terms of the y coordinate, p0.
2. Sort all other points Pn from least to greatest with respect to the angle between the ray Pn-P0 and the x axis.
3. Starting with p0, consider all other points Pn in order and add them to the set defining the convex hull as long as pn-1, pn, pn+1 form a 'left turn' when going counter clockwise around the enclosing polygon.
	a. if a right turn is encountered, Pn is inside the polygon, and should be omitted from the hull.
	b. if a point is collinear, it can be discarded or included, depending on application.

Post Graham's Scan:
4. After arriving at the solution for the convex hull, I simply computed the minimum internal angle in the hull and presented the point to the console as requested.

For implementation of the Graham Scan in python much of the impementation was modeled after the code found at:
[Link]https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/

---

##Notes on Implementation
Development in Python 3.6.6<br />
Pycharm Community Edition IDE

- For sorting the points in step 2 above, each pair of points (p1, p2) considered were sorted according to their cross product (p1-p0) X (p2-p0) when connecting p0 to the two points individually, forming two rays beginning at p0. If the cross product was positive, then p2-p0 was of greater angle then p1-p0, and therefore p2 should come after p1. If negative, p1 should come after p2. If the cross product was 0, then the points are collinear with p0, and the closer point to p0 should be first.
- For distance comparisons, the square of the distance was used, instead of the true distance. This was sufficient for comparing the distance of two pairs of points.
- For angle comparisons in step 4 above, the value of the cosine of the angle was used, instead of the angle value. This was sufficient as the highest cosine would yield the smallest angle. Since cosine is monotonic on the interval [0,pi] and all internal angles are guaranteed to be < pi (def convex hull), then finding the highest cosine value would yield the desired asteroid point.
- For this solution, I elected to not error check input, and assumed its form, contents would remain consistent. (i.e. if the file exists, is found, and open for read, program proceeds assuming it contains points of the format in the problem statement)
- Since the only user input was the initial input.txt file, inputs from one function to another were generally assumed to be valid. Little argument validation was performed. For example, functions expecting integer args did not verify that the args weren't strings, etc.
- Most methods are organized as utility (static) methods of a class. This helped me quickly generate unit test methods, and also store the __asteroid0 (lowest-y reference asteroid) as a class variable and avoid a global variable, or passing around a constant between function calls.
- Even if the number of asteroids supplied is different from what is declared at input line 1, then the program still runs and solves the asteroid set. Declaring fewer asteroids than are supplied will result in program only considering and solving with as many asteroids as were declared. Declaring more points than are supplied will not affect the solution.
- Duplicate asteroid points are removed from the input set.
- If the input set contains not enough points:
	1. No points: the program prints "No asteroids supplied."
	2. Fewer than 3 points (after removing duplicates), then the trivial solution will be given: the first point in the set list (may be different than first supplied asteroid after removing duplicates). As there are at most two points, either point would work.

##Other Remarks
- Improvements to unit testing might include randomizing the integer inputs for asteroid coordinates where possible.
- With more experience, it would be interesting to see how to better organize unit testing. "Do I really need a new function for each test case, or could I cleverly reuse the functions for multiple cases?"
- I used a class with mostly static utility functions with a class member variable to house the functionality. If all my functions are static, should I just have added all these functions into the main.py file instead of having a class?
	1. From the beginning, I think I only used a class so I could have a class variable and avoid the use of a global.