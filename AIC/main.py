from owlready2 import *
import os
import sys
from typing import List, Dict, Optional
import random
import time
from tutorials import get_tutorial



class MathTutoringSystem:
    def __init__(self, ontology_path: str):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(current_dir, ontology_path)
            
            if not os.path.exists(full_path):
                raise FileNotFoundError(f"Ontology file not found at: {full_path}")
            
            print(f"Loading ontology from: {full_path}")
            self.onto = get_ontology(full_path).load()
            self.current_student = None
            self.current_concept = None
            self.learning_history = []
            
        except Exception as e:
            print(f"Error initializing system: {e}")
            sys.exit(1)

    def update_progress(self, score: float):
        """Update student's progress based on exam score"""
        if self.current_student:
            try:
                current_progress = self.current_student.hasProgress[0] if self.current_student.hasProgress else 0
                # New progress is weighted average: 70% old progress, 30% new score
                new_progress = int((0.7 * current_progress) + (0.3 * score))
                self.current_student.hasProgress = [min(100, new_progress)]
                print(f"\nProgress updated! Current progress: {new_progress}%")
            except Exception as e:
                print(f"Error updating progress: {e}")

    def start_learning_session(self):
        """Start a structured learning session"""
        if not self.current_student or not self.current_concept:
            return False

        print("\n=== Starting Learning Session ===")
        print(f"Concept: {self.current_concept.name}")
        
        session_data = {
            'concept': self.current_concept.name,
            'start_time': time.strftime('%Y-%m-%d %H:%M:%S'),
            'tutorial_completed': False,
            'test_score': 0,
            'questions_attempted': 0
        }

        # 1. Tutorial Section
        print("\n=== Tutorial Section ===")
        tutorial = self.get_concept_tutorial()
        self._show_tutorial(tutorial)
        input("\nPress Enter when you're ready for the practice questions...")
        session_data['tutorial_completed'] = True

        # 2. Practice Questions
        print("\n=== Practice Section ===")
        practice_score = self._conduct_practice_session()
        session_data['practice_score'] = practice_score

        # 3. Final Test
        print("\n=== Final Test ===")
        test_result = self._conduct_test()
        session_data.update(test_result)

        # 4. Show Summary
        self._show_session_summary(session_data)
        
        # Update progress
        self.update_progress(test_result['test_score'])
        
        # Store session history
        self.learning_history.append(session_data)
        
        return True

    def get_concept_tutorial(self) -> Dict:
        """Get detailed tutorial content for current concept"""
        tutorials = {
            'Triangle': {
                'title': 'Understanding Triangles',
                'sections': [
                    {
                        'title': 'Basic Definition',
                        'content': 'A triangle is a polygon with three edges and three vertices.',
                    },
                    {
                        'title': 'Types of Triangles',
                        'content': '1. Right Triangle: Has one 90-degree angle\n'
                                 '2. Equilateral Triangle: All sides equal\n'
                                 '3. Isosceles Triangle: Two sides equal',
                    },
                    {
                        'title': 'Key Properties',
                        'content': '- Sum of angles = 180 degrees\n'
                                 '- Area = (base × height) ÷ 2\n'
                                 '- Perimeter = sum of all sides',
                    }
                ]
            },
            'Circle': {
                'title': 'Understanding Circles',
                'sections': [
                    {
                        'title': 'Basic Definition',
                        'content': 'A circle is a set of points equidistant from a center point.',
                    },
                    {
                        'title': 'Key Terms',
                        'content': '- Radius: Distance from center to edge\n'
                                 '- Diameter: Distance across circle through center\n'
                                 '- Circumference: Distance around the circle',
                    },
                    {
                        'title': 'Formulas',
                        'content': '- Area = πr²\n'
                                 '- Circumference = 2πr',
                    }
                ]
            }
        }
        
        return tutorials.get(self.current_concept.name, {
            'title': f'Learning about {self.current_concept.name}',
            'sections': [
                {
                    'title': 'Introduction',
                    'content': f'Basic introduction to {self.current_concept.name}.'
                }
            ]
        })

    def _show_tutorial(self, tutorial: Dict):
        """Display tutorial content in a structured way"""
        print(f"\n=== {tutorial['title']} ===\n")
        
        for section in tutorial['sections']:
            print(f"## {section['title']} ##")
            print(section['content'])
            print()
            time.sleep(1)  # Give time to read
            input("Press Enter to continue...")
            print()

    def _get_concept_questions(self) -> List[Dict]:
        """Get questions for current concept"""
        questions = {
            'Triangle': [
                {
                    'question': 'What is the sum of angles in a triangle?',
                    'options': ['180 degrees', '360 degrees', '90 degrees', '270 degrees'],
                    'correct': '180 degrees'
                },
                {
                    'question': 'How do you calculate the area of a triangle?',
                    'options': ['(base × height) ÷ 2', 'base × height', 'base + height', '(base + height) ÷ 2'],
                    'correct': '(base × height) ÷ 2'
                }
            ],
            'Circle': [
                {
                    'question': 'What is the formula for the area of a circle?',
                    'options': ['πr²', '2πr', 'πd', 'r²'],
                    'correct': 'πr²'
                },
                {
                    'question': 'What is the relationship between diameter and radius?',
                    'options': ['diameter = 2 × radius', 'radius = 2 × diameter', 'they are equal', 'no relationship'],
                    'correct': 'diameter = 2 × radius'
                }
            ]
        }
        
        return questions.get(self.current_concept.name, [
            {
                'question': f'What is the basic definition of a {self.current_concept.name}?',
                'options': ['Option A', 'Option B', 'Option C', 'Option D'],
                'correct': 'Option A'
            }
        ])

    def _conduct_practice_session(self) -> int:
        """Conduct practice session with immediate feedback"""
        questions = self._get_concept_questions()
        score = 0
        
        for i, q in enumerate(questions, 1):
            print(f"\nPractice Question {i}:")
            print(q['question'])
            for j, option in enumerate(q['options'], 1):
                print(f"{j}. {option}")
            
            while True:
                try:
                    answer = int(input("\nYour answer (enter number): "))
                    if 1 <= answer <= len(q['options']):
                        break
                    print("Invalid option number. Try again.")
                except ValueError:
                    print("Please enter a number.")
            
            selected = q['options'][answer-1]
            if selected == q['correct']:
                print("Correct! Well done!")
                score += 1
            else:
                print(f"Not quite. The correct answer was: {q['correct']}")
                print("Let's review this concept before moving on.")
            
            input("\nPress Enter to continue...")
        
        return (score / len(questions)) * 100

    def _conduct_test(self) -> Dict:
        """Conduct final test"""
        questions = self._get_concept_questions()
        random.shuffle(questions)  # Randomize question order
        score = 0
        answers = []
        
        for i, q in enumerate(questions, 1):
            print(f"\nQuestion {i}:")
            print(q['question'])
            for j, option in enumerate(q['options'], 1):
                print(f"{j}. {option}")
            
            while True:
                try:
                    answer = int(input("\nYour answer (enter number): "))
                    if 1 <= answer <= len(q['options']):
                        break
                    print("Invalid option number. Try again.")
                except ValueError:
                    print("Please enter a number.")
            
            selected = q['options'][answer-1]
            answers.append({
                'question': q['question'],
                'selected': selected,
                'correct': q['correct'],
                'is_correct': selected == q['correct']
            })
            if selected == q['correct']:
                score += 1

        return {
            'test_score': (score / len(questions)) * 100,
            'questions_attempted': len(questions),
            'correct_answers': score,
            'answers': answers
        }

    def get_available_concepts(self) -> List[str]:
        """Get list of available geometric concepts"""
        concepts = []
        try:
            # Get all geometric shapes
            if hasattr(self.onto, 'GeometricShape'):
                shapes = list(self.onto.GeometricShape.subclasses())
                for shape in shapes:
                    if shape.name not in concepts:
                        concepts.append(shape.name)

            # Add 2D shapes
            if hasattr(self.onto, 'TwoDimensional'):
                shapes_2d = list(self.onto.TwoDimensional.subclasses())
                for shape in shapes_2d:
                    if shape.name not in concepts:
                        concepts.append(shape.name)

            # Add specific shapes
            specific_shapes = ['Triangle', 'Circle', 'Square', 'Rectangle', 
                            'RightTriangle', 'EquilateralTriangle', 'IsoscelesTriangle']
            
            for shape in specific_shapes:
                if hasattr(self.onto, shape) and shape not in concepts:
                    concepts.append(shape)

        except Exception as e:
            print(f"Error getting concepts: {e}")
            
        if not concepts:
            # Fallback basic shapes if no concepts found in ontology
            concepts = ['Triangle', 'Circle', 'Square', 'Rectangle']
            
        return concepts

    def register_student(self, name: str, skill_level: str) -> bool:
        """Register a new student in the system"""
        try:
            # Create new student instance with a sanitized name (remove spaces)
            student_id = f"Student_{name.replace(' ', '_')}"
            student = self.onto.Student(student_id)
            
            # Set skill level
            level_id = f"Level_{name.replace(' ', '_')}"
            if skill_level.lower() == "beginner":
                level = self.onto.Beginner(level_id)
            elif skill_level.lower() == "intermediate":
                level = self.onto.Intermediate(level_id)
            elif skill_level.lower() == "advanced":
                level = self.onto.Advanced(level_id)
            else:
                return False

            # Link student to skill level using a list
            student.hasSkillLevel = [level]
            
            # Set progress as a list
            student.hasProgress = [0]
            
            self.current_student = student
            print(f"\nStudent Registration Successful!")
            print(f"Name: {name}")
            print(f"Skill Level: {skill_level.capitalize()}")
            print(f"Initial Progress: 0%")
            return True
            
        except Exception as e:
            print(f"Error registering student: {e}")
            return False

    def conduct_exam(self):
        """Conduct an exam for the current concept"""
        if not self.current_concept:
            print("\nPlease select a concept first!")
            return None

        tutorial_data = get_tutorial(self.current_concept.name)
        exam_questions = tutorial_data['exam_questions']
        random.shuffle(exam_questions)  # Randomize question order
        
        total_questions = len(exam_questions)
        correct_answers = 0
        answers = []

        print("\n=== Final Exam ===")
        print(f"Topic: {self.current_concept.name}")
        print(f"Total Questions: {total_questions}")
        print("\nAnswer each question carefully. Good luck!")

        for i, question in enumerate(exam_questions, 1):
            print(f"\nQuestion {i} of {total_questions}:")
            print(question['question'])
            
            for j, option in enumerate(question['options'], 1):
                print(f"{j}. {option}")
            
            while True:
                try:
                    answer = int(input("\nYour answer (enter number): "))
                    if 1 <= answer <= len(question['options']):
                        break
                    print("Invalid option number. Try again.")
                except ValueError:
                    print("Please enter a number.")

            selected = question['options'][answer-1]
            is_correct = selected == question['correct']
            
            answers.append({
                'question': question['question'],
                'selected': selected,
                'correct': question['correct'],
                'is_correct': is_correct,
                'explanation': question['explanation']
            })

            if is_correct:
                correct_answers += 1

        score = (correct_answers / total_questions) * 100
        
        print("\n=== Exam Results ===")
        print(f"Score: {score:.1f}%")
        print(f"Correct Answers: {correct_answers} out of {total_questions}")
        
        print("\nDetailed Review:")
        for i, answer in enumerate(answers, 1):
            print(f"\nQ{i}: {answer['question']}")
            print(f"Your Answer: {answer['selected']}")
            print(f"Correct Answer: {answer['correct']}")
            print(f"{'✓ Correct!' if answer['is_correct'] else '✗ Incorrect'}")
            if not answer['is_correct']:
                print(f"Explanation: {answer['explanation']}")

        return {
            'score': score,
            'total_questions': total_questions,
            'correct_answers': correct_answers,
            'answers': answers
        }

    def select_concept(self, concept_name: str) -> bool:
        """Select a concept to study"""
        try:
            concept = getattr(self.onto, concept_name)
            self.current_concept = concept
            print(f"\nSelected concept: {concept_name}")
            return True
        except Exception as e:
            print(f"Error selecting concept: {e}")
            return False

    def _show_session_summary(self, session_data: Dict):
        """Display learning session summary"""
        print("\n" + "="*50)
        print("=== Learning Session Summary ===")
        print("="*50)
        
        print(f"\nConcept: {session_data['concept']}")
        print(f"Session Date: {session_data['start_time']}")
        print(f"\nTutorial Completed: {'Yes' if session_data['tutorial_completed'] else 'No'}")
        print(f"Practice Score: {session_data['practice_score']:.1f}%")
        print(f"Final Test Score: {session_data['test_score']:.1f}%")
        
        print("\nDetailed Test Results:")
        for i, answer in enumerate(session_data['answers'], 1):
            print(f"\nQ{i}: {answer['question']}")
            print(f"Your Answer: {answer['selected']}")
            print(f"Correct Answer: {answer['correct']}")
            print(f"Status: {'✓ Correct' if answer['is_correct'] else '✗ Incorrect'}")
        
        print("\nRecommendations:")
        if session_data['test_score'] >= 80:
            print("- Excellent work! You're ready to move on to more advanced concepts.")
        elif session_data['test_score'] >= 60:
            print("- Good effort! Consider reviewing the topics you missed before moving on.")
        else:
            print("- More practice recommended. Consider reviewing the tutorial again.")
        
        print("\n" + "="*50)

def main():
    """Main function to run the Math Tutoring System"""
    try:
        system = MathTutoringSystem("ontology.owl")
    except Exception as e:
        print(f"Failed to initialize the system: {e}")
        return

    while True:
        try:
            # Display current student info if exists
            if system.current_student:
                print(f"\nCurrent Student: {system.current_student.name}")
                if system.current_concept:
                    print(f"Current Concept: {system.current_concept.name}")
            
            # Display main menu
            print("\n=== Math Tutoring System Menu ===")
            print("1. Register New Student")
            print("2. Select Learning Concept")
            print("3. View Tutorial")
            print("4. Take Exam")
            print("5. View Progress History")
            print("6. Exit")

            choice = input("\nEnter your choice (1-6): ").strip()

            if choice == "1":
                # Student Registration
                name = input("Enter student name: ").strip()
                if not name:
                    print("\nError: Name cannot be empty!")
                    continue
                    
                print("\nSelect skill level:")
                print("1. Beginner")
                print("2. Intermediate")
                print("3. Advanced")
                skill_choice = input("Enter choice (1-3): ").strip()
                
                skill_map = {"1": "beginner", "2": "intermediate", "3": "advanced"}
                if skill_choice in skill_map:
                    if system.register_student(name, skill_map[skill_choice]):
                        print("\nRegistration successful! Let's start learning.")
                        print("Please select a concept to begin.")
                    else:
                        print("\nRegistration failed. Please try again.")
                else:
                    print("\nInvalid skill level choice!")

            elif choice == "2":
                # Concept Selection
                if not system.current_student:
                    print("\nPlease register first!")
                    continue

                print("\nAvailable concepts:")
                concepts = system.get_available_concepts()
                
                if not concepts:
                    print("No concepts available at the moment.")
                    continue

                for i, concept in enumerate(concepts, 1):
                    print(f"{i}. {concept}")
                
                concept_choice = input("\nSelect concept number: ").strip()
                try:
                    concept_index = int(concept_choice) - 1
                    if 0 <= concept_index < len(concepts):
                        if system.select_concept(concepts[concept_index]):
                            print("\nYou can now:")
                            print("1. View Tutorial")
                            print("2. Take Exam")
                            print("Choose an option from the main menu.")
                        else:
                            print("\nError selecting concept. Please try again.")
                    else:
                        print("\nInvalid concept number!")
                except ValueError:
                    print("\nInvalid input. Please enter a number.")

            elif choice == "3":
                # View Tutorial
                if not system.current_student:
                    print("\nPlease register first!")
                    continue
                if not system.current_concept:
                    print("\nPlease select a concept first!")
                    continue

                tutorial = system.get_concept_tutorial()
                if tutorial:
                    for section in tutorial['sections']:
                        print(f"\n=== {section['title']} ===")
                        print(section['content'])
                        input("\nPress Enter to continue to next section...")
                    print("\nTutorial completed! You can now take the exam.")
                else:
                    print("\nNo tutorial available for this concept.")

            elif choice == "4":
                # Take Exam
                if not system.current_student:
                    print("\nPlease register first!")
                    continue
                if not system.current_concept:
                    print("\nPlease select a concept first!")
                    continue

                print("\nStarting exam session...")
                print("This exam will test your knowledge of", system.current_concept.name)
                ready = input("Are you ready to begin? (yes/no): ").strip().lower()
                
                if ready == 'yes':
                    result = system.conduct_exam()
                    if result:
                        # Store exam result in learning history
                        system.learning_history.append({
                            'date': time.strftime('%Y-%m-%d %H:%M:%S'),
                            'concept': system.current_concept.name,
                            'score': result['score'],
                            'questions_attempted': result['total_questions'],
                            'correct_answers': result['correct_answers']
                        })
                        system.update_progress(result['score'])
                else:
                    print("\nExam cancelled. Take some time to review the tutorial.")

            elif choice == "5":
                # View Progress History
                if not system.current_student:
                    print("\nPlease register first!")
                    continue
                
                if not system.learning_history:
                    print("\nNo learning sessions completed yet.")
                    print("Complete a tutorial or take an exam to see your progress!")
                    continue
                
                print("\n=== Learning History ===")
                for i, session in enumerate(system.learning_history, 1):
                    print(f"\nSession {i}:")
                    print(f"Date: {session['date']}")
                    print(f"Concept: {session['concept']}")
                    print(f"Score: {session['score']}%")
                    print(f"Questions Attempted: {session['questions_attempted']}")
                    print(f"Correct Answers: {session['correct_answers']}")
                    print("-" * 30)

            elif choice == "6":
                # Exit
                print("\nThank you for using the Math Tutoring System!")
                print("Keep learning and practicing!")
                break

            else:
                print("\nInvalid choice. Please enter a number between 1 and 6.")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please try again or contact support if the problem persists.")
            continue

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nCritical error occurred: {e}")
        print("The program will now exit.")
        sys.exit(1)