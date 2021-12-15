
from polygon import Polygon
from polygonsequence import PolygonSequence
import pytest
import inspect
import os
import re 


README_CONTENT_CHECK_FOR = [
    'Polygon',
    'PolygonSequence',
    'init',
    'repr',
    'eq',
    'gt',
    'len',
    'getitem',
    'maximum_efficient_polygon'
]

def test_session9_readme_exists():
    '''Test to check if the README.md file has been created and stored in close vicinity'''

    assert os.path.isfile("README.md"), "Found README.md file!"


def test_session9_readme_500_words():
    '''Test to check if the README.md file has equal to or greater than 500 words'''

    readme_words=[word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_session9_readme_proper_description():
    '''Test to check if description has been provided for each of the functions declared within the code'''
    
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_session9_readme_file_for_more_than_10_hashes():
    '''Test to check if the number of topics and subtopics described within the README.md file is equal to or greater than 10'''

    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10, "You have not described all the functions/classes well in your README.md file"


def test_session9_indentations():
    '''Test to check if the indentation in the session9.py file follows the PEP8 guidelines'''

    lines = inspect.getsource(session9)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        print(space)
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_session9_function_name_had_cap_letter():
    '''PEP8 gudelines state that function names cannnot have capital letters in them. This test checks if there are any \
    capital lettes within function names and throws error if there are.'''

    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


################################ Validation for Objective 1: Creating a Polygon class,  polygon_class ######################################

def test_session9_polygon_class_number_of_vertices():
    '''Test to ensure that the input argument for the number of vertices is an integer.'''

    with pytest.raises(TypeError, match=r".*Please enter an integer only*"):
        Polygon("hello", 5)


def test_session9_polygon_class_positive_value_for_vertices():
    '''Test to ensure that the input argument for the number of vertices is a positive value.'''

    with pytest.raises(ValueError, match=r".*The number of vertices should be a positive value*"):
        Polygon(-3, 5)


def test_session9_polygon_class_greater_than_or_equal_to_three_vertices():
    '''Test to ensure that the value of the input argument for the number of vertices is equal to greater than 3.'''

    with pytest.raises(ValueError, match=r".*The number of vertices should be greater than or equal to three*"):
        Polygon(1, 5)


def test_session9_polygon_class_circumradius_int_or_float():
    '''Test to ensure that the value of the input argument for the circumradius is either of an int or a float type.'''

    with pytest.raises(TypeError, match=r".*The value of circumradius should be an int or a float*"):
        Polygon(4, "circumradius")


def test_session9_polygon_class_value_of_properties_are_positive():
    '''Test to ensure that the calculated values of the interior angle, edge length, apothem, area and perimeter are positive.'''

    p = Polygon(4, 5)
    assert (p.interiorangle > 0), "The value of the interior angle should be a positive value"
    assert (p.edgelength > 0), "The value of the edge length should be a positive value"
    assert (p.apothem > 0), "The value of the apothem should be a positive value"
    assert (p.area > 0), "The value of the area should be a positive value"
    assert (p.perimeter > 0), "The value of the perimeter should be a positive value"


def test_session9_polygon_class_output_check():
    '''Test to ensure that the defined polygon class returns the appropriate results.'''

    p = Polygon(4, 5)
    assert (bool(p) == True), "The class is not giving appropriate output"

def test_session9_polygon_class_repr_check():
    '''Test to ensure that the proper description of the class is being output by \
    the representation class.'''

    check_list = ["interior angle", "edge length", "apothem", "area", "perimeter"]
    reprcomplete = True
    p = Polygon(4, 5)
    reprout = p.__repr__()
    for c in check_list:
        if c not in reprout:
            reprcomplete = False
    assert reprcomplete == True, "The representation function has not been implemented"


def test_session9_polygon_class_equality_check():
    '''Test to ensure that the values of the number of vertices and circumradii are being compared with accuracy.'''

    p1 = Polygon(4, 5)
    p2 = Polygon(4, 5)
    assert (p1 == p2),"The comparison of number of vertices and circumradius is not accurate"


def test_session9_polygon_class_greater_than_check():
    '''Test to ensure that the algorithm is correctly distinguishing between two polygons whose vertices are not the same, \
    specifically when one is greater than the other.'''
    p1 = Polygon(5, 5)
    p2 = Polygon(4, 5)
    assert (p1 > p2),"The comparison of number of vertices is not accurate"




################################ Validation for Objective 2: Creating a Custom Polygon sequence type, polygonsequence_class ######################################

def test_session9_polygonsequence_class_number_of_vertices():
    '''Test to ensure that the input argument for the number of vertices is an integer.'''

    with pytest.raises(TypeError, match=r".*Please enter an integer only*"):
        PolygonSequence("hello", 5)


def test_session9_polygonsequence_class_positive_value_for_vertices():
    '''Test to ensure that the input argument for the number of vertices is a positive value.'''

    with pytest.raises(ValueError, match=r".*The max number of vertices should be a positive value*"):
        PolygonSequence(-3, 5)


def test_session9_polygonsequence_class_circumradius_int_or_float():
    '''Test to ensure that the value of the input argument for the circumradius is either of an int or a float type.'''

    with pytest.raises(TypeError, match=r".*The value of circumradius should be an int or a float*"):
        PolygonSequence(4, "circumradius")


def test_session9_polygonsequence_class_circumradius_positive_check():
    '''Test to ensure that the value of the input argument for the circumradius is either of an int or a float type.'''

    with pytest.raises(ValueError, match=r".*The value of circumradius should be positive*"):
        PolygonSequence(4, -5)


def test_session9_polygonsequence_class_circumradius_output_check():
    '''Test to ensure that the defined polygon sequence class returns the appropriate results.'''

    p = PolygonSequence(10, 5)
    assert (bool(p) == True), "The class is not giving appropriate output"


def test_session9_polygonsequence_class_repr_check():
    '''Test to ensure that the proper description of the class is being output by \
    the representation class.'''

    check_list = ["PolygonSequence", "class",  "polygons", "vertices", "circumradius"]
    reprcomplete = True
    ps = PolygonSequence(10, 5)
    reprout = ps.__repr__()
    for c in check_list:
        if c not in reprout:
            print(c)
            reprcomplete = False
    assert reprcomplete == True, "The representation function has not been implemented"


def test_session9_polygonsequence_length_check():
    '''Test to check the length of the polygon sequence'''
    ps = PolygonSequence(10, 5)
    assert len(ps) == 10, "Length function not implemnted correctly"


def test_session9_polygonsequence_less_than_3_index_access():
    '''Test to check the return for index less than 3'''

    ps = PolygonSequence(10, 5)
    assert (bool(ps[2]) == False), "The class is not giving appropriate output for  index less than 3"


def test_session9_polygonsequence_index_access():
    '''Test to check if indexing works on our PolygonSequence class'''

    ps = PolygonSequence(10, 5)
    p1 = ps[3]
    p2 = ps[5]
    assert isinstance(p1, session9.Polygon), "Indexing does not seem to work on PolygonSequence"
    assert isinstance(p2, session9.Polygon), "Indexing does not seem to work on PolygonSequence"


def test_session9_polygonsequence_negative_index_access():
    '''Test to check if Negative indexing works on our PolygonSequence class'''

    ps = PolygonSequence(10, 5)
    p1 = ps[-3]
    p2 = ps[-5]
    assert isinstance(p1, session9.Polygon), "Negative indexing does not seem to work on PolygonSequence"
    assert isinstance(p2, session9.Polygon), "Negative indexing does not seem to work on PolygonSequence"


def test_session9_polygonsequence_slice_access():
    '''Test to check if slicing works on our PolygonSequence class'''

    ps = PolygonSequence(10, 5)
    p1 = ps[1:2:1]
    assert bool(p1) == True, "Slicing does not seem to work on PolygonSequence"


def test_session9_polygonsequence_maximum_efficient_polygon():
    '''Test to check the maximum_efficient_polygon function'''

    ps = PolygonSequence(10, 5)
    assert round(ps.maximum_efficient_polygon(), 2) == 2.35, "Something is wrong in finding maximum efficient polygon"
