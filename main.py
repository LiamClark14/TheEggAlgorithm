

# calculateWeightedSum - calculates the heuristic value for a student, thereby determining strength of match
# @params requirements - a 2D array, with each element being a [string, int] tuple with the string being the requirement
# and the int being the scalar representing the importance of that requirement
#         skills - an array of skills possessed by any given student
# @return weightedSum - a scalar with a larger value indicating a greater degree of match
def calculateWeightedSum(requirements, skills):
    weightedSum = 0
    for skill in skills:
        for req in requirements:
            if skill == req[0]:
                weightedSum += req[1]
    return weightedSum


# updateRecommendations - updates the recommendations array with the most recently evaluated student
# @params student - the next student that has been assigned a heuristic
#         thresh - the number of students we wish to recommend
#         recommendations - an array of students that we wish to recommend
# @return the updated array of recommendations with the newly evaluated student taken into account
def updateRecommendations(student, thresh, recommendations):
    if len(recommendations) < thresh:
        recommendations.append(student)
        sortRecommendations(recommendations)
    else:
        sortRecommendations(recommendations)
        for i in range(thresh - 1, -1, -1):
            if recommendations[i][1] < student[1]:
                recommendations[i] = student
                sortRecommendations(recommendations)
                break
    return recommendations


# Sort recommendations by strength of match using a merge sort
# @params recs - the unsorted array of recommendations
# @return the sorted array of recommendations
def sortRecommendations(recs):
    n = len(recs)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if recs[j][1] < recs[j + 1][1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                recs[j], recs[j + 1] = recs[j + 1], recs[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return recs

# Student
# Student has a name, Student has skills
class Student:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills


# Startup
# Student has a name, Student has skills
class Startup:
    def __init__(self, name, requirements):
        self.name = name
        self.requirements = requirements


# recommendStudents - the master algorithm
# @params thresh - how many students we wish to recommend
#         students - an array of student objects (students from our database)
#         startup - the startup we wish to match students with
# @return our recommended students for the startup
def recommendStudents(thresh, students, startup):
    recommendations = []

    for student in students:
        weightedSum = calculateWeightedSum(startup.requirements, student.skills)
        weightedStudent = [student.name, weightedSum]
        updateRecommendations(weightedStudent, thresh, recommendations)
    return recommendations

# running tests
def main():
    Shelly = Student("Shelly", ["Art", "Drawing", "Graphic Design", "Speech", "Web Design"])
    Richard = Student("Richard", ["Computer Science", "Frontend", "Backend", "Web Design", "Leadership"])
    Simon = Student("Simon", ["Leadership", "Curiosity", "Figma", "React", "Adaptability"])
    Daisy = Student("Daisy", ["Generosity", "Responsibility", "Figma", "React", "Adaptability"])
    Ralph = Student("Ralph", ["Visual Studio", "Java", "Leadership", "Sales", "Adaptability"])
    Emerson = Student("Emerson", ["Fashion", "Design", "Figma", "Marketing", "Branding", "Curiosity"])
    Troy = Student("Troy", ["Acting", "Dance", "Adaptability", "Mindfulness", "Branding", "Guitar"])
    Nixon = Student("Nixon",  ["Origami", "Birdwatching", "Courteous", "Manners", "Delusional", "Guitar"])
    Roger = Student("Roger", ["Curiosity", "Resourcefulness", "Confidence", "Work ethic", "Leadership", "Guitar"])
    Federer = Student("Federer", ["Tennis", "Cardiovascular Endurance", "Medicine", "Finance", "Marketing", "Eloquence"])

    students = [Shelly, Richard, Simon, Daisy, Ralph, Emerson, Troy, Nixon, Roger, Federer]

    TheEgg = Startup("The Egg", [["Curiosity", 8], ["Leadership", 3], ["Adaptability", 4], ["Figma", 2], ["Branding", 3]])

    print(recommendStudents(6, students, TheEgg))
if __name__ == "__main__":
    main()








