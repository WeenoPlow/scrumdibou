# coding: utf8
'''
Created on Oct  220 5
'''



# We create the var 'correction'. It will be displayed if user press 'yes' after the quiz to display the correction

correction = """

'Question 1: What are the human values? (Check the correct group)'
'Answer A =>  Simplicity / Visibility / Feedback /  Adaptation' 
'Answer B =>  Modesty / Courage / Transparency / Communication' 
'Answer C =>  Simplicity / Transparency / Feedback /  Knowledge' 
'Answer D =>  Feedback / Courage / Visibility /  Communication'
'GOOD ANSWER : -> B' 


'Question 2: What are the process values? (Check the correct group)' 
'Answer A =>  Simplicity / Visibility / Feedback /  Communication' 
'Answer B =>  Simplicity / Courage / Transparency / Communication' 
'Answer C =>  Simplicity / Visibility / Feedback /  Adaptation' 
'Answer D =>  Modesty / Courage / Transparency /  Knowledge'
'GOOD ANSWER : -> C' 


'Question 3: What are the main tasks of the following actors? (Product Owner)' 
'Answer A =>  Maintain the process / Guards the perimeter / self-organized' 
'Answer B =>  Validates deliveries / Pilot the team / Guards the perimeter / Maintain the process' 
'Answer C =>  Lead the team / Maintain the process / self-organized /  validates deliveries' 
'Answer D =>  Guards the perimeter / Validates deliveries / Co-pilot the team'
'GOOD ANSWER : -> D' 


'Question 4: What are the main tasks of the following actors? (SCRUM Master)' 
'Answer A =>  Pilot the team / Facilitator / Maintain the process' 
'Answer B =>  Pilot the team / cross-functional / Transparency' 
'Answer C =>  Facilitator / Visibility / cross-functional' 
'Answer D =>  Modesty / Courage /  Facilitator'
'GOOD ANSWER : -> A' 


'Question 5: What are the main tasks of the following actors? (SCRUM Team)' 
'Answer A =>  Facilitator / cross-functional /  Communication' 
'Answer B =>  Analyses and coast / Products the system / self-organized / cross-functional' 
'Answer C =>  cross-functional / Visibility / Guards the perimeter' 
'Answer D =>  Guards the perimeter / Facilitator /  cross-functional / Facilitator'
'GOOD ANSWER : -> B' 


'Question 6: What is the INVEST model?' 
'Answer A =>  Interesting / Negotiable / Validate / Estimation / Sizable / Testable' 
'Answer B =>  Independent / Negotiable / Valuable / Relevant / Sizable / Time boxed' 
'Answer C =>  Independent / Negotiable / Valuable / Estimable / Size Appropriately / Testable' 
'Answer D =>  Interesting / Negotiable / Validated / Estimable / Size Appropriately / time-boxed'
'GOOD ANSWER : -> C' 


'Question 7: What is the SMART model?' 
'Answer A =>  Specific / Measurable / Achievable / Relevant / Time-boxed' 
'Answer B =>  Specialization / Measurable / Approximate / Relevant / Time-boxed' 
'Answer C =>  Specific / Measurable / Achievable / Readable / Testable' 
'Answer D =>  Specification / Measurable / Achievable / Relevant / Time-boxed'
'GOOD ANSWER : -> A' 


'Question 8: What is the DEMING cycle?' 
'Answer A =>  Precision / Do / Comparison / Act' 
'Answer B =>  Plan / Don\'t Panic / Check / Activation' 
'Answer C =>  Precision / Do / Check / Act' 
'Answer D =>  Plan / Do / Check / Act'
'GOOD ANSWER : -> D' 


'Question 9: What is the SCRUM cycle? (The good order)' 
'Answer A =>  Sprint + Daily Scrum > Sprint Meeting > Product Backlog > Potentially shippable product > Adaptation > Retrospectives' 
'Answer B =>  Product Backlog > Sprint Meeting > Sprint + Daily Scrum > Potentially shippable product > Retrospectives > Adaptation' 
'Answer C =>  Product Backlog > Sprint Meeting > Sprint + Daily Scrum > Sprint Meeting > Retrospectives > Potentially shippable product' 
'Answer D =>  Sprint + Daily Scrum > Sprint Meeting > Product Backlog > Adaptation > Retrospectives > Potentially shippable product'
'GOOD ANSWER : -> B' 
                      
 
'Question 10: Who are the SCRUM Members?' 
'Answer A =>  Product Owner / Scrum Master / Scrum Team' 
'Answer B =>  Participant Contributor / Scrum Master / Scrum Team' 
'Answer C =>  Product Owner / Scrum Master / Informed Party' 
'Answer D =>  Product Owner / Experts / Scrum Team'
'GOOD ANSWER : -> A' 
  

'Question 11: What are the Jeffies 3C\'s?' 
'Answer A =>  Calculation / Construction / Confirmation' 
'Answer B =>  Create / Conversation / Confirmation' 
'Answer C =>  Card / Conversion / Construction' 
'Answer D =>  Card / Conversation / Confirmation'
'GOOD ANSWER : -> D' 


'Question 12: What is the User Story?' 
'Answer A =>  A short story about user' 
'Answer B =>  A long description of a situation that is a source of value for the Scrum team' 
'Answer C =>  A short description of a feature that is a source of value for the product user or customer' 
'Answer D =>  A report form user or customer about a feature already existing on a product'
'GOOD ANSWER : -> C' 
  

'Question 13: What is the user story format?' 
'Answer A =>  <Title> As <role>I want <Something> To <Achieve a Goal>' 
'Answer B =>  As <role>I want <Something> To <Achieve a Goal>' 
'Answer C =>  <Title> As <role>I need <Something>' 
'Answer D =>  To <recipient>From <Expeditor>Subject: <Subject>'
'GOOD ANSWER : -> A' 
  

'Question 14: Who are the stakeholders (Participants)?' 
'Answer A =>  Manager / Participant Contributor / Informed Party / Experts' 
'Answer B =>  Scrum Master / Product Owner / Scrum Team' 
'Answer C =>  Manager / Users / Scrum Team / Experts' 
'Answer D =>  Master / Customers / Informed Party / Experts'
'GOOD ANSWER : -> A' 


'Question 15: What is the intruder?' 
'Answer A =>  Sprint review' 
'Answer B =>  Sprint Backlog' 
'Answer C =>  Sprint Retrospective' 
'Answer D =>  Scrum Meeting'
'GOOD ANSWER : -> B' 


'Question 16: Where can I find the Acceptance Criteria?' 
'Answer A =>  Bottom of the card (user story)' 
'Answer B =>  At the back of the card (user story)' 
'Answer C =>  In Product Backlog' 
'Answer D =>  On the front of the card (user story)'
'GOOD ANSWER : -> B' 


'Question 17: What is TDD?' 
'Answer A =>  Test Driving by Developers' 
'Answer B =>  Test / Directed / Development' 
'Answer C =>  Test Driving Development' 
'Answer D =>  Test / Direction / Determined'
'GOOD ANSWER : -> C' 


'Question 18: What is \'sprint Backlog\'?' 
'Answer A =>  List of jobs to do for a Sprint' 
'Answer B =>  List of tasks remaining' 
'Answer C =>  List of tasks that has been done' 
'Answer D =>  The only task remaining'
'GOOD ANSWER : -> A' 
  

'Question 19: What is the average duration of the Sprint?' 
'Answer A =>    - 6 weeks' 
'Answer B =>  2 - 4 weeks' 
'Answer C =>    - 3 weeks' 
'Answer D =>  3 - 4 weeks'
'GOOD ANSWER : -> B' 

         
'Question 20: The Product Backlog is under the <???>\'s responsibility' 
'Answer A =>  Product Owner' 
'Answer B =>  Scrum Team' 
'Answer C =>  Scrum Master' 
'Answer D =>  Customers'
'GOOD ANSWER : -> A' 
                      
    
'Question 2 : The Sprint Backlog is under the <???>\'s responsibility' 
'Answer A =>  Product Owner' 
'Answer B =>  Users' 
'Answer C =>  Scrum Team' 
'Answer D =>  Scrum Master'
'GOOD ANSWER : -> C' 
                      
       
'Question 22: The Burndown chart is under the <???>\'s responsibility' 
'Answer A =>  Stakeholders' 
'Answer B =>  Scrum Team' 
'Answer C =>  Customers' 
'Answer D =>  Scrum Master'
'GOOD ANSWER : -> D' 
                      
                                          
'Question 23: What is a Epic User Story?' 
'Answer A =>  This is a big user story that is split into several smaller user stories' 
'Answer B =>  It does not exist in scrum' 
'Answer C =>  This is a very complex user story' 
'Answer D =>  This is a important user story'
'GOOD ANSWER : -> A' 
                
                      
'Question 24: What is the goal of the Initial Project Perimeter?'    
'Answer A =>  Identify the scrum actors' 
'Answer B =>  Identify the main themes and requirements' 
'Answer C =>  Identify the ideas' 
'Answer D =>  Identify the tasks'
'GOOD ANSWER : -> B' 


'Question 25: What is the velocity?'          
'Answer A =>  It\'s the estimation of the point which can be done per day'
'Answer B =>  It\'s the estimation of the point which can be done per sprint'
'Answer C =>  Is a production capacity measurement linked to a developer for one day'
'Answer D =>  Is a production capacity measurement linked to a single team in the specific context of a project'      
'GOOD ANSWER : -> D'
        
"""    






