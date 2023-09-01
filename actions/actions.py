# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# #
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []


# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionShareTimetable(Action):
#     def name(self) -> Text:
#         return "action_share_timetable"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         response = "The timetable for each semester depends on module availability. We may consider a tentative timetable. If you miss subjects in semesters 1 and 2, you can take them in semesters 4/5 or with the junior batch."
#         dispatcher.utter_message(text=response)
        
#         return []

# class ActionMinimumCredits(Action):
#     def name(self) -> Text:
#         return "action_minimum_credits"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         response = "There is no minimum credit requirement, but it's recommended to complete the compulsory courses."
#         dispatcher.utter_message(text=response)
        
#         return []

# class ActionAddDropPeriod(Action):
#     def name(self) -> Text:
#         return "action_add_drop_period"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         response = "You can add or drop courses within the first two weeks of the semester. If you need changes later, contact the relevant lecturer and the MSc coordinator."
#         dispatcher.utter_message(text=response)
        
#         return []

# class ActionElectiveVsOptional(Action):
#     def name(self) -> Text:
#         return "action_elective_vs_optional"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         response = "Electives belong to different buckets and require a specific number of modules from that bucket to meet credit requirements. Optionals are not tied to specific buckets and can be taken as needed."
#         dispatcher.utter_message(text=response)
        
#         return []

# class ActionSpecializationSwitch(Action):
#     def name(self) -> Text:
#         return "action_specialization_switch"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         response = "We recommend selecting a specialization at the start and sticking with it. Changing later might make it challenging to catch up with missed subjects."
#         dispatcher.utter_message(text=response)
        
#         return []

# class ActionAttendOtherLectures(Action):
#     def name(self) -> Text:
#         return "action_attend_other_lectures"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         response = "If you wish to attend lectures for courses you're not enrolled in, please contact the respective lecturers for permission and guidance."
#         dispatcher.utter_message(text=response)
        
#         return []

# class ActionGPACalculationOptional(Action):
#     def name(self) -> Text:
#         return "action_gpa_calculation_optional"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         response = "Yes, credits from Optional modules are also calculated in the GPA."
#         dispatcher.utter_message(text=response)
        
#         return []

# class ActionSubjectAvailability(Action):
#     def name(self) -> Text:
#         return "action_subject_availability"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         response = "The subjects not covered in this semester are usually offered annually. You can consider taking them in upcoming semesters or with the junior batch."
#         dispatcher.utter_message(text=response)
        
#         return []

# class ActionCreditsLimit(Action):
#     def name(self) -> Text:
#         return "action_credits_limit"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         response = "While you can take additional credits beyond 36, it's not very common as this would add an extra workload."
#         dispatcher.utter_message(text=response)
        
#         return []

# class ActionCoursePeriodExtension(Action):
#     def name(self) -> Text:
#         return "action_course_period_extension"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         response = "The maximum duration for the program is 4 years. The normal duration is 2 years. Extensions beyond 4 years require valid reasons, such as health-related issues, approved by the Faculty PostGraduate board."
#         dispatcher.utter_message(text=response)
        
#         return []

# class ActionIndustrialProjectAlternative(Action):
#     def name(self) -> Text:
#         return "action_industrial_project_alternative"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         response = "Yes, you can opt for CS6995 Industrial Project (5 credits) and CS6996 MSc Independent Research (15 credits) instead of the normal dissertation (CS6999). However, this option is not very popular recently. You should discuss this with MSc coordinators."
#         dispatcher.utter_message(text=response)
        
#         return []

# # Add more actions for other intents...
