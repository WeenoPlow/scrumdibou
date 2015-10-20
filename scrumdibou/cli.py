import cmd
import progress
from quizz import Quizz
from TestScrum import Question

# We create an empty list
questions = []

# We add each questions in the "questions" list
questions.append(Question(
    'Question 1/25 : What are the human values? (Check the correct group)',
        {
          "A":"Answer A =>  Simplicity / Visibility / Feedback /  Adaptation",
          "B":"Answer B =>  Modesty / Courage / Transparency / Communication",
          "C":"Answer C =>  Simplicity / Transparency / Feedback /  Knowledge",
          "D":"Answer D =>  Feedback / Courage / Visibility /  Communication"
        },
        10,
        "B",
        1
))

questions.append(Question(
    'Question 2/25 : What are the process values? (Check the correct group)',
        {
          "A":"Answer A =>  Simplicity / Visibility / Feedback /  Communication",
          "B":"Answer B =>  Simplicity / Courage / Transparency / Communication",
          "C":"Answer C =>  Simplicity / Visibility / Feedback /  Adaptation",
          "D":"Answer D =>  Modesty / Courage / Transparency /  Knowledge"
        },
        10,
        "C",
        1
))

questions.append(Question(
    'Question 3/25 : What are the main tasks of the following actors? (Product Owner)',
        {
          "A":"Answer A =>  Maintain the process / Guards the perimeter / self-organized",
          "B":"Answer B =>  Validates deliveries / Pilot the team / Guards the perimeter / Maintain the process",
          "C":"Answer C =>  Lead the team / Maintain the process / self-organized /  validates deliveries",
          "D":"Answer D =>  Guards the perimeter / Validates deliveries / Co-pilot the team"
        },
        10,
        "D",
        1
))

questions.append(Question(
    'Question 4/25 : What are the main tasks of the following actors? (SCRUM Master)',
        {
          "A":"Answer A =>  Pilot the team / Facilitator / Maintain the process",
          "B":"Answer B =>  Pilot the team / cross-functional / Transparency",
          "C":"Answer C =>  Facilitator / Visibility / cross-functional",
          "D":"Answer D =>  Modesty / Courage /  Facilitator"
        },
        10,
        "A",
        1
))

questions.append(Question(
    'Question 5/25 : What are the main tasks of the following actors? (SCRUM Team)',
        {
          "A":"Answer A =>  Facilitator / cross-functional /  Communication",
          "B":"Answer B =>  Analyses and coast / Products the system / self-organized / cross-functional",
          "C":"Answer C =>  cross-functional / Visibility / Guards the perimeter",
          "D":"Answer D =>  Guards the perimeter / Facilitator /  cross-functional / Facilitator"
        },
        10,
        "B",
        1
))

questions.append(Question(
    'Question 6/25 : What is the INVEST model?',
        {
          "A":"Answer A =>  Interesting / Negotiable / Validate / Estimation / Sizable / Testable",
          "B":"Answer B =>  Independent / Negotiable / Valuable / Relevant / Sizable / Time boxed",
          "C":"Answer C =>  Independent / Negotiable / Valuable / Estimable / Size Appropriately / Testable",
          "D":"Answer D =>  Interesting / Negotiable / Validated / Estimable / Size Appropriately / time-boxed"
        },
        10,
        "C",
        1
))


questions.append(Question(
    'Question 7/25 : What is the SMART model?',
        {
          "A":"Answer A =>  Specific / Measurable / Achievable / Relevant / Time-boxed",
          "B":"Answer B =>  Specialization / Measurable / Approximate / Relevant / Time-boxed",
          "C":"Answer C =>  Specific / Measurable / Achievable / Readable / Testable",
          "D":"Answer D =>  Specification / Measurable / Achievable / Relevant / Time-boxed"
        },
        10,
        "A",
        1
))


questions.append(Question(
    'Question 8/25 : What is the DEMING cycle?',
        {
          "A":"Answer A =>  Precision / Do / Comparison / Act",
          "B":"Answer B =>  Plan / Don't Panic / Check / Activation",
          "C":"Answer C =>  Precision / Do / Check / Act",
          "D":"Answer D =>  Plan / Do / Check / Act"
        },
        10,
        "D",
        1
))


questions.append(Question(
    'Question 9/25 : What is the SCRUM cycle? (The good order)',
        {
          "A":"Answer A =>  Sprint + Daily Scrum > Sprint Meeting > Product Backlog > Potentially shippable product > Adaptation > Retrospectives",
          "B":"Answer B =>  Product Backlog > Sprint Meeting > Sprint + Daily Scrum > Potentially shippable product > Retrospectives > Adaptation",
          "C":"Answer C =>  Product Backlog > Sprint Meeting > Sprint + Daily Scrum > Sprint Meeting > Retrospectives > Potentially shippable product",
          "D":"Answer D =>  Sprint + Daily Scrum > Sprint Meeting > Product Backlog > Adaptation > Retrospectives > Potentially shippable product"
        },
        10,
        "B",
        1
))


questions.append(Question(
    'Question 10/25 : Who are the SCRUM Members?',
        {
          "A":"Answer A =>  Product Owner / Scrum Master / Scrum Team",
          "B":"Answer B =>  Participant Contributor / Scrum Master / Scrum Team",
          "C":"Answer C =>  Product Owner / Scrum Master / Informed Party",
          "D":"Answer D =>  Product Owner / Experts / Scrum Team"
        },
        10,
        "A",
        1
))

questions.append(Question(
    'Question 11/25 : What are the Jeffries 3C\'s?',
        {
          "A":"Answer A =>  Calculation / Construction / Confirmation",
          "B":"Answer B =>  Create / Conversation / Confirmation",
          "C":"Answer C =>  Card / Conversion / Construction",
          "D":"Answer D =>  Card / Conversation / Confirmation"
        },
        10,
        "D",
        1
))

questions.append(Question(
    'Question 12/25 : What is the User Story?',
        {
          "A":"Answer A =>  A short story about user",
          "B":"Answer B =>  A long description of a situation that is a source of value for the Scrum team",
          "C":"Answer C =>  A short description of a feature that is a source of value for the product user or customer",
          "D":"Answer D =>  A report form user or customer about a feature already existing on a product"
        },
        10,
        "C",
        1
))

questions.append(Question(
    'Question 13/25 : What is the user story format?',
        {
          "A":"Answer A =>  <Title> As <role>, I want <Something> To <Achieve a Goal>",
          "B":"Answer B =>  As <role>, I want <Something> To <Achieve a Goal>",
          "C":"Answer C =>  <Title> As <role>, I need <Something>",
          "D":"Answer D =>  To <recipient>, From <expeditor>, Subject: <Subject>"
        },
        10,
        "A",
        1
))

questions.append(Question(
    'Question 14/25 : Who are the stakeholders (Participants)?',
        {
          "A":"Answer A =>  Manager / Participant Contributor / Informed Party / Experts",
          "B":"Answer B =>  Scrum Master / Product Owner / Scrum Team",
          "C":"Answer C =>  Manager / Users / Scrum Team / Experts",
          "D":"Answer D =>  Master / Customers / Informed Party / Experts"
        },
        10,
        "A",
        1
))

questions.append(Question(
    'Question 15/25 : What is the intruder?',
        {
          "A":"Answer A =>  Sprint review",
          "B":"Answer B =>  Sprint Backlog",
          "C":"Answer C =>  Sprint Retrospective",
          "D":"Answer D =>  Scrum Meeting"
        },
        10,
        "B",
        1
))

questions.append(Question(
    'Question 16/25 : Where can I find the Acceptance Criteria?',
        {
          "A":"Answer A =>  Bottom of the card (user story)",
          "B":"Answer B =>  At the back of the card (user story)",
          "C":"Answer C =>  In Product Backlog",
          "D":"Answer D =>  On the front of the card (user story)"
        },
        10,
        "B",
        1
))


questions.append(Question(
    'Question 17/25 : What is TDD?',
        {
          "A":"Answer A =>  Test Driving by Developers",
          "B":"Answer B =>  Test / Directed / Development",
          "C":"Answer C =>  Test Driving Development",
          "D":"Answer D =>  Test / Direction / Determined"
        },
        10,
        "C",
        1
))


questions.append(Question(
    'Question 18/25 : What is "sprint Backlog"?',
        {
          "A":"Answer A =>  List of jobs to do for a Sprint",
          "B":"Answer B =>  List of tasks remaining",
          "C":"Answer C =>  List of tasks that has been done",
          "D":"Answer D =>  The only task remaining"
        },
        10,
        "A",
        1
))


questions.append(Question(
    'Question 19/25 : What is the average duration of the Sprint?',
        {
          "A":"Answer A =>  1 - 6 weeks",
          "B":"Answer B =>  2 - 4 weeks",
          "C":"Answer C =>  1 - 3 weeks",
          "D":"Answer D =>  3 - 4 weeks"
        },
        10,
        "B",
        1
))

questions.append(Question(
    'Question 20/25 : The Product Backlog is under the <???>\'s responsibility',
        {
          "A":"Answer A =>  Product Owner",
          "B":"Answer B =>  Scrum Team",
          "C":"Answer C =>  Scrum Master",
          "D":"Answer D =>  Customers"
        },
        10,
        "A",
        1
))


questions.append(Question(
    'Question 21/25 : The Sprint Backlog is under the <???>\'s responsibility',
        {
          "A":"Answer A =>  Product Owner",
          "B":"Answer B =>  Users",
          "C":"Answer C =>  Scrum Team",
          "D":"Answer D =>  Scrum Master"
        },
        10,
        "C",
        1
))

questions.append(Question(
    'Question 22/25 : The Burndown chart is under the <???>\'s responsibility',
        {
          "A":"Answer A =>  Stakeholders",
          "B":"Answer B =>  Scrum Team",
          "C":"Answer C =>  Customers",
          "D":"Answer D =>  Scrum Master"
        },
        10,
        "D",
        1
))

questions.append(Question(
    'Question 23/25 : What is a Epic User Story?',
        {
          "A":"Answer A =>  This is a big user story that is split into several smaller user stories",
          "B":"Answer B =>  It does not exist in scrum",
          "C":"Answer C =>  This is a very complex user story",
          "D":"Answer D =>  This is a important user story"
        },
        10,
        "A",
        1
))


questions.append(Question(
    'Question 24/25 : What is the goal of the Initial Project Perimeter?',
        {
          "A":"Answer A =>  Identify the scrum actors",
          "B":"Answer B =>  Identify the main themes and requirements",
          "C":"Answer C =>  Identify the ideas",
          "D":"Answer D =>  Identify the tasks"
        },
        10,
        "B",
        1
))


questions.append(Question(
    'Question 25/25 : What is the velocity?',
        {
          "A":"Answer A =>  It's the estimation of the point which can be done per day",
          "B":"Answer B =>  It's the estimation of the point which can be done per sprint",
          "C":"Answer C =>  Is a production capacity measurement linked to a developer for one day",
          "D":"Answer D =>  Is a production capacity measurement linked to a single team in the specific context of a project"
        },
        10,
        "D",
        1
))

class Scrumdibou(cmd.Cmd):

    # We define the text display when user type 'help' or '?'
    """
    Commands :

      start      ->  Start new quiz
      quit       ->  Quit the quiz
      help       ->  Display all commands
      ?          ->  Display all commands

    """

    # We define the intro text
    intro = ("""
      Welcome to

    #####  ##### #####  ##  ## ##       ## ####   ## #####   ####  ##  ##
   ##     ##     ##  ## ##  ## ###     ### ##  ##    ##  ## ##  ## ##  ##
   ###### ##     ####   ##  ## ####   #### ##  ## ## #####  ##  ## ##  ##
       ## ##     ## ##  ##  ## ## ## ## ## ##  ## ## ##  ## ##  ## ##  ##
   #####  ###### ##  ## #####  ##  ##   ## ####   ## ######  ####  #####

  Type 'help' or '?' for more instructions
  To begin the quiz -> Enter 'start' then press <Enter> key  :)
    """)
    # Define the prompt
    prompt = ("Scrumdibou>")

    #Function of initialization (Manage Questions/Answers then the results, then the correction
    def do_start(self, arg):
        quizz = Quizz(questions)
        quizz.start()
        quizz.results()
        quizz.correction()
        #quizz.save()

    # Manage the highscore's display
    def do_highscore(self, arg):
        Quizz.highscore()

    # Function for quit the application
    def do_quit(self, arg):
        print()
        print("Thank you for playing !!!")
        return True

    # Function 'help'
    def do_help(self, arg):
        print (self.__doc__)


if __name__ == "__main__":
    Scrumdibou().cmdloop()
