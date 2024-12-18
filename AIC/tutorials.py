# tutorials.py

TUTORIALS = {
    'Triangle': {
        'title': 'Understanding Triangles',
        'sections': [
            {
                'title': 'Basic Definition',
                'content': '''A triangle is a polygon with three edges and three vertices. It is one of the basic shapes in geometry.

Key Points:
* Has three sides and three angles
* Is a closed shape
* Sum of all interior angles is 180 degrees'''
            },
            {
                'title': 'Types of Triangles',
                'content': '''There are several types of triangles based on their angles and sides:

1. Based on Angles:
   * Acute Triangle: All angles less than 90°
   * Right Triangle: One angle exactly 90°
   * Obtuse Triangle: One angle greater than 90°

2. Based on Sides:
   * Equilateral Triangle: All sides equal
   * Isosceles Triangle: Two sides equal
   * Scalene Triangle: No sides equal'''
            },
            {
                'title': 'Area and Perimeter',
                'content': '''Important Formulas:

1. Area Calculation:
   * Area = (base × height) ÷ 2
   * For equilateral triangle: A = (√3/4) × a²
     where 'a' is the length of a side

2. Perimeter Calculation:
   * Perimeter = sum of all sides
   * For equilateral triangle: P = 3a
     where 'a' is the length of a side'''
            }
        ],
        'exam_questions': [
            {
                'question': 'What is the sum of interior angles in a triangle?',
                'options': ['180 degrees', '360 degrees', '90 degrees', '270 degrees'],
                'correct': '180 degrees',
                'explanation': 'The sum of interior angles in any triangle is always 180 degrees.'
            },
            {
                'question': 'Which type of triangle has all sides of equal length?',
                'options': ['Equilateral', 'Isosceles', 'Scalene', 'Right'],
                'correct': 'Equilateral',
                'explanation': 'An equilateral triangle has all three sides of equal length.'
            },
            {
                'question': 'What is the formula for the area of a triangle?',
                'options': ['(base × height) ÷ 2', 'base × height', 'base + height', '(base + height) ÷ 2'],
                'correct': '(base × height) ÷ 2',
                'explanation': 'The area of a triangle is calculated by multiplying base and height, then dividing by 2.'
            },
            {
                'question': 'In a right triangle, what is the measure of the right angle?',
                'options': ['90 degrees', '60 degrees', '45 degrees', '180 degrees'],
                'correct': '90 degrees',
                'explanation': 'A right triangle always has one angle that measures exactly 90 degrees.'
            },
            {
                'question': 'Which triangle has exactly two sides of equal length?',
                'options': ['Isosceles', 'Equilateral', 'Scalene', 'Obtuse'],
                'correct': 'Isosceles',
                'explanation': 'An isosceles triangle has exactly two sides of equal length.'
            },
            {
                'question': 'What is the Pythagorean theorem used for?',
                'options': [
                    'Finding the length of sides in a right triangle',
                    'Finding the area of any triangle',
                    'Finding the perimeter of a triangle',
                    'Finding the angles of a triangle'
                ],
                'correct': 'Finding the length of sides in a right triangle',
                'explanation': 'The Pythagorean theorem (a² + b² = c²) is used to find the length of sides in a right triangle.'
            },
            {
                'question': 'In an equilateral triangle, what are the measures of all angles?',
                'options': ['60 degrees each', '45 degrees each', '90 degrees each', '30 degrees each'],
                'correct': '60 degrees each',
                'explanation': 'In an equilateral triangle, all angles are equal and measure 60 degrees (180 ÷ 3 = 60).'
            },
            {
                'question': 'What is the perimeter of a triangle with sides 3, 4, and 5 units?',
                'options': ['12 units', '10 units', '15 units', '60 units'],
                'correct': '12 units',
                'explanation': 'The perimeter is the sum of all sides: 3 + 4 + 5 = 12 units.'
            },
            {
                'question': 'In a right triangle, what is the name of the longest side?',
                'options': ['Hypotenuse', 'Base', 'Height', 'Adjacent'],
                'correct': 'Hypotenuse',
                'explanation': 'The hypotenuse is the longest side of a right triangle and is opposite to the right angle.'
            },
            {
                'question': 'What type of triangle has one angle greater than 90 degrees?',
                'options': ['Obtuse', 'Acute', 'Right', 'Equilateral'],
                'correct': 'Obtuse',
                'explanation': 'An obtuse triangle has one angle that measures more than 90 degrees.'
            }
        ],

    },
    'Square': {
        'title': 'Understanding Squares',
        'sections': [
            {
                'title': 'Basic Definition',
                'content': '''A square is a regular quadrilateral with four equal sides and four right angles (90 degrees).

Key Properties:
* All sides are equal in length
* All angles are 90 degrees
* Opposite sides are parallel
* Diagonals are equal in length and bisect each other at right angles'''
            },
            {
                'title': 'Area and Perimeter',
                'content': '''Important Formulas:

1. Area Calculation:
   * Area = side × side (or s²)
   * Area = a²  where 'a' is the length of any side

2. Perimeter Calculation:
   * Perimeter = 4 × side
   * P = 4a  where 'a' is the length of any side

3. Diagonal Calculation:
   * Diagonal = side × √2
   * d = a√2  where 'a' is the length of any side'''
            },
            {
                'title': 'Special Properties',
                'content': '''Special Characteristics:

1. Symmetry:
   * Has 4 lines of symmetry
   * Rotational symmetry of order 4

2. Additional Properties:
   * All squares are rectangles
   * All squares are rhombuses
   * Diagonals bisect each other at 90 degrees
   * Diagonals divide the square into four equal triangles'''
            }
        ],
            'exam_questions': [
                {
                    'question': 'What is the formula for the area of a square?',
                    'options': ['side × side', 'side + side', '4 × side', '2 × side'],
                    'correct': 'side × side',
                    'explanation': 'The area of a square is calculated by multiplying the length of one side by itself (s²).'
                },
                {
                    'question': 'How many lines of symmetry does a square have?',
                    'options': ['4', '2', '1', '3'],
                    'correct': '4',
                    'explanation': 'A square has 4 lines of symmetry: 2 diagonal and 2 through the midpoints of opposite sides.'
                },
                {
                    'question': 'What is the formula for the perimeter of a square?',
                    'options': ['4 × side', 'side × side', '2 × side', 'side + side'],
                    'correct': '4 × side',
                    'explanation': 'The perimeter of a square is calculated by multiplying the length of one side by 4.'
                },
                {
                    'question': 'How many right angles (90 degrees) does a square have?',
                    'options': ['4', '2', '3', '1'],
                    'correct': '4',
                    'explanation': 'A square has four right angles, each measuring 90 degrees.'
                },
                {
                    'question': 'What is the relationship between the diagonals of a square?',
                    'options': [
                        'Equal length and perpendicular',
                        'Different lengths',
                        'Parallel to each other',
                        'None of the above'
                    ],
                    'correct': 'Equal length and perpendicular',
                    'explanation': 'The diagonals of a square are equal in length and intersect at right angles (90 degrees).'
                },
                {
                    'question': 'If a square has a side length of 5 units, what is its area?',
                    'options': ['25 square units', '20 square units', '10 square units', '15 square units'],
                    'correct': '25 square units',
                    'explanation': 'Area = side × side = 5 × 5 = 25 square units'
                },
                {
                    'question': 'Which of these is NOT a property of a square?',
                    'options': [
                        'Opposite angles are different',
                        'All sides are equal',
                        'Diagonals bisect each other',
                        'All angles are 90 degrees'
                    ],
                    'correct': 'Opposite angles are different',
                    'explanation': 'All angles in a square are equal (90 degrees), including opposite angles.'
                },
                {
                    'question': 'How do you find the diagonal of a square?',
                    'options': [
                        'Multiply side length by √2',
                        'Multiply side length by 2',
                        'Divide side length by 2',
                        'Add two sides'
                    ],
                    'correct': 'Multiply side length by √2',
                    'explanation': 'The diagonal of a square can be found using the formula: diagonal = side × √2'
                },
                {
                    'question': 'What is the sum of interior angles of a square?',
                    'options': ['360 degrees', '180 degrees', '270 degrees', '400 degrees'],
                    'correct': '360 degrees',
                    'explanation': 'A square has four 90-degree angles, so the sum is 4 × 90 = 360 degrees.'
                },
                {
                    'question': 'What type of quadrilateral is a square?',
                    'options': [
                        'Regular quadrilateral',
                        'Irregular quadrilateral',
                        'Scalene quadrilateral',
                        'None of the above'
                    ],
                    'correct': 'Regular quadrilateral',
                    'explanation': 'A square is a regular quadrilateral because all its sides and angles are equal.'
                }
            ]
        }
}

def get_tutorial(concept_name: str):
    """Retrieve tutorial for a specific concept"""
    return TUTORIALS.get(concept_name, {
        'title': f'Learning about {concept_name}',
        'sections': [
            {
                'title': 'Introduction',
                'content': f'Basic introduction to {concept_name}.'
            }
        ],
        'exam_questions': [
            {
                'question': f'What is a {concept_name}?',
                'options': ['Option A', 'Option B', 'Option C', 'Option D'],
                'correct': 'Option A',
                'explanation': 'Basic explanation would go here.'
            }
        ]
    })