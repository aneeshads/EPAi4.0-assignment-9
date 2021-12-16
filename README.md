# Session 9 assignment of EPAi4.0
### Submitted by Aneesha Das
### E-mail id: dasaneesha@gmail.com


# Sequence Types – 1

In Python, a sequence can be defined as a container that can essentially preserve the order of a collection of homogeneous or heterogeneous items which are iterable and indexable. Sequences can be further classified as mutable – where the items can be modified – and non-mutable – where the items cannot be modified. Examples of immutable sequences include tuple, strings etc., whereas examples of mutable sequences include list, dictionaries etc.

The present assignment is about accepting such arguments as number of vertices and the length of the circumradius of a polygon, and then making a module that will include the formula for calculating different parameters related to the polygon.
 
## Description of classes implemented in the current code

### Polygon

The class 'Polygon' accepts the number of vertices (greater than or equal to 3) and the circumradius of a polygon as input arguments. The various functions within the class calculate the measures of interior angle, edge length, apothem, area and perimeter for the polygon, till two places after decimal. 

Brief descriptions of the functions defined within the Polygon class are as follows:

#### __init__

The initializer function defines that the class accepts two parameters - the number of vertices  of the polygon whose properties have to be calculated, and the circumradius of the same. Circumradius is expressed as the radius of an imaginary circle that can be inscribed around the polygon.

##### Usage:
Polygon(numberofvertices, circumradius)

where, numberofvertices = number of vertices input by the user,
       cirumradius = circumradius input by the user


#### __repr__

The dunder method of representation function describes the messages that are displayed when the class Polygon is called without an argument.

##### Usage:
Polygon() (this invokes the __repr__ function)


#### __eq__

The dunder method of equality has been defined to compare and return with an affirmative when the dimensions - number of vertices and circumradii - of two input polygons are equal.

##### Usage:
polygon1 == polygon2

where,  polygon1 = Polygon(numberofvertices1, circumradius1),
	polygon2 = Polygon(numberofvertices2, circumradius2)
   

#### __gt__

The dunder method of greater than has been defined to compare and return with an affirmative when the number of vertices of one input polygon is greater than the other.

##### Usage:
polygon1 > polygon2

where,  polygon1 = Polygon(numberofvertices1, circumradius1),
	polygon2 = Polygon(numberofvertices2, circumradius2)


A brief description of the test cases that have been employed to test the functions are as follows:

| Name of the test case                                              | Brief description of the test case                                                                                      | Status(Passed/Failed |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|----------------------|
| test_session9_polygon_class_number_of_vertices                     | Test to ensure that the input argument for the number of vertices is an integer                                         | Passed               |
| test_session9_polygon_class_positive_value_for_vertices            | Test to ensure that the input argument for the number of vertices is a positive value.                                  | Passed               |
| est_session9_polygon_class_greater_than_or_equal_to_three_vertices | Test to ensure that the value of the input argument for the number of vertices is equal to greater than three.          | Passed               |
| test_session9_polygon_class_circumradius_int_or_float              | Test to ensure that the value of the input argument for the circumradius is either of an int or a float type.           | Passed               |
| test_session9_polygon_class_value_of_properties_are_positive       | Test to ensure that the calculated values of the interior angle, edge length, apothem, area and perimeter are positive. | Passed               |
| test_session9_polygon_class_output_check                           | Test to ensure that the defined representation class returns the appropriate results.                                   | Passed               |
| test_session9_polygon_class_repr_check                             | Test to ensure that the proper description of the class is being output by  the representation class.                   | Passed               |
| test_session9_polygon_class_equality_check                         | Test to ensure that the values of the number of vertices and circumradii are being compared with accuracy.              | Passed               |

Finally, the class has been converted into a module. It has been successfully demonstrated that the module can be incorporated and initiated as per the usage protocols.


### PolygonSequence

This class creates a sequence of polygons with varying number of vertices and the same circumradius. The least possible number of vertices that a polygon can possess is three. The index of the sequence corresponds to the number of vertices in the polygon (which means that index values under 3 are not accepted). The circumradius is assumed to be the same for all the polygons. Brief descriptions of the functions defined within the Polygon class are as follows:


#### __init__
The class is initialized in a way that it can accept the arguments of maximum vertices and circumradius.

##### Usage:
PolygonSequence(maxvertices, circumradius)


#### __len__

The dunder method of length returns the number of polygons that are present within the sequence.

##### Usage:
len(PolygonSequence(maxvertices, circumradius))


#### __getitem__

The dunder method of getitem returns the item in the sequence as per the index or the slice.

##### Usage:
custompolygon[3]

or

custompolygon[5:9:1]

where custompolygon = PolygonSequence (maxvertices, circumradius)


#### __repr__

The dunder method of representation returns the polygon with the maximum number  of vertices and the common circumradius.

##### Usage:
PolygonSequence()


#### maximum_efficient_polygon

A polygon that has the highest area to perimeter ratio is denoted as the maximum efficiency polygon. This function finds the polygon which has the maximum efficiency among all the others within the sequence.

##### Usage:

PolygonSequence(maxvertices, circumradius). maximum_efficient_polygon()


A brief description of the test cases that have been employed to test the functions are as follows:

| Name of the test case                                           | Brief description of the test case                                                                            | Status(Passed/Failed |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------|
| test_session9_polygonsequence_class_number_of_vertices          | Test to ensure that the input argument for the number of vertices is an integer.                              | Passed               |
| test_session9_polygonsequence_class_positive_value_for_vertices | Test to ensure that the input argument for the number of vertices is a positive value.                        | Passed               |
| test_session9_polygonsequence_class_circumradius_int_or_float   | Test to ensure that the value of the input argument for the circumradius is either of an int or a float type. | Passed               |
| test_session9_polygonsequence_class_circumradius_positive_check | Test to ensure that the value of the input argument for the circumradius is either of an int or a float type. | Passed               |
| test_session9_polygonsequence_class_circumradius_output_check   | Test to ensure that the defined polygon sequence class returns the appropriate results.                       | Passed               |
| test_session9_polygonsequence_class_repr_check                  | Test to ensure that the proper description of the class is being output by the representation class.          | Passed               |
| test_session9_polygonsequence_length_check                      | Test to check the length of the polygon sequence.                                                             | Passed               |
| test_session9_polygonsequence_less_than_3_index_access          | Test to check the return for index less than three.                                                           | Passed               |
| test_session9_polygonsequence_index_access                      | Test to check if indexing works on the PolygonSequence class.                                                 | Passed               |
| test_session9_polygonsequence_negative_index_access             | Test to check if negative indexing works on the  PolygonSequence class.                                       | Passed               |
| test_session9_polygonsequence_slice_access                      | Test to check if slicing works on the PolygonSequence class.                                                  | Passed               |
| test_session9_polygonsequence_maximum_efficient_polygon         | Test to check if the maximum_efficient_polygon function is giving appropriate output.                         | Passed               |

Finally, the class has been converted into a module. It has been successfully demonstrated that the module can be incorporated and initiated as per the usage protocols.

The following table illustrates the test cases that have been employed to check the various aspects of document formatting of the README.md and the session9.py files.

| Name of the test case                             | Brief description of the test case                                                                                                                                                                                           | Function/File being tested | Status (Passed/Failed) |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|------------------------|                          
| test_session9_readme_exists                       | This test checks if the README.md file has been created.                                                                                                                                                                     | README.md                  | Passed                 |
| test_session9_readme_500_words                    | This test checks if the README.md file contains at least 500 words.                                                                                                                                                          | README.md                  | Passed                 |
| test_session9_readme_proper_description           | This test checks if the functions have been described well in the README.md file.                                                                                                                                            | README.md                  | Passed                 |
| test_session9_readme_file_for_more_than_10_hashes | This test checks if a minimum of ten topics have been mentioned in the README.md file.                                                                                                                                       | README.md                  | Passed                 |
| test_session9_indentations                        | The PEP8 guidelines state that the number of spaces left should be a multiple of four, for defining proper indentation within a code.This test checks if the code has been written adhering to the aforementioned guideline. | session9.py                | Passed                 |
| test_session9_function_name_had_cap_letter        | According to PEP8 guidelines, the names of functions cannot have any capital letters in them. This test ensures that there are no such capital letters in the names of functions.                                            | session9.py                | Passed                 |







