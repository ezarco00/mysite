import course

COURSES = [
    course.Course(period=1,
                  name='Intro to Computer Science',
                  teacher_name='Ms. Lee',
                  resource_name='repl.it',
                  resource_url='https://repl.it/'),
    course.Course(period=2,
                  name='Ap Literature',
                  teacher_name='Mr. Wilson',
                  resource_name='sparknotes',
                  resource_url='http://www.sparknotes.com/'),
    course.Course(period=3,
                  name='Precalculus',
                  teacher_name='Ms.Chand',
                  resource_name='Khan Academy',
                  resource_url='https://www.khanacademy.org/math/precalculus'),
    course.Course(period=4,
                  name='Economics',
                  teacher_name='Mr.Seelbach',
                  resource_name='Investopedia',
                  resource_url='https://www.investopedia.com/terms/e/economics.asp'),
    course.Course(period=5,
                  name='Physics',
                  teacher_name='Mr.Trautman',
                  resource_name='Physics Classroom',
                  resource_url='http://www.physicsclassroom.com/'),
    course.Course(period=6,
                  name='Yearbook',
                  teacher_name='Mr.Barlas',
                  resource_name='Jostens',
                  resource_url='http://yearbookavenue.jostens.com/'),
    ]