from typing import Any, Text, Dict, List, Union

import mysql.connector
from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from database_connectivity import DataUpdate, DataExtract
from rasa_sdk.events import SlotSet, UserUtteranceReverted, ActionReverted, FollowupAction


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_your_num"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(text="Hello World!")
        # print(tracker.get_slot('num'))
        # dispatcher.utter_template('utter_your_num', tracker, number=details[str(tracker.get_slot('NAME')).lower()])
        return []

    class ActionDataExtract(Action):

        def name(self) -> Text:
            return "action_data_extract"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            global row
            mod_name = "'" + tracker.get_slot("REGISTRATION") + "'"
            message = "nope"
            # data=DataExtract(tracker.get_slot('REGISTRATION'))
            # print("Here is details",data)
            # dispatcher.utter_message("+".join(data))

            # dispatcher.utter_message()
            # print(tracker.get_slot('num'))
            # dispatcher.utter_template('utter_your_num', tracker, number=details[str(tracker.get_slot('NAME')).lower()])
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="root",
                database="rasa_feedback"
            )
            mycursor = mydb.cursor()
            # sql_select_query = "select * from accommodation_data where REGISTRATION =  {mod_name}"
            # set variable in query
            mycursor.execute(f"SELECT  * FROM accommodation_data WHERE REGISTRATION = {mod_name}")
            myresult = mycursor.fetchall()
            for m in myresult:
                message = '\n'.join(m)

            mycursor.close()
            mydb.close()
            dispatcher.utter_message(text=message)
            return [SlotSet('REGISTRATION',None)]

    class ActionFormReg(FormAction):
        def name(self) -> Text:
            """Unique identifier of the form"""

            return "form_reg"

        @staticmethod
        def required_slots(tracker: Tracker) -> List[Text]:
            """A list of required slots that the form has to fill"""

            return ["REGISTRATION"]

        def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
            """A dictionary to map required slots to
                - an extracted entity
                - intent: value pairs
                - a whole message
                or a list of them, where a first match will be picked"""

            return {
                "REGISTRATION": [self.from_text()]
            }

        def submit(
                self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any],
        ) -> List[Dict]:
            """Define what the form has to do
                after all required slots are filled"""

            # utter submit template

            return []

    class ActionAccommodationSubmit(Action):

        def name(self) -> Text:
            return "action_submit_data"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            dispatcher.utter_message(template="utter_thanks")
            DataUpdate(tracker.get_slot('REGISTRATION'), tracker.get_slot('NAME'), tracker.get_slot('DOB'),
                       tracker.get_slot('Address'), tracker.get_slot('CELL'),
                       tracker.get_slot('CITY'), tracker.get_slot('COURSE'),
                       tracker.get_slot('EMAIL'), tracker.get_slot('GENDER'),
                       tracker.get_slot('SCHOOL'), )
            dispatcher.utter_message("Your Data Saved")

            # print(tracker.get_slot('num'))
            # dispatcher.utter_template('utter_your_num', tracker, number=details[str(tracker.get_slot('NAME')).lower()])
            return [SlotSet('NAME',None),SlotSet('GENDER',None),SlotSet('SCHOOL',None),SlotSet('COURSE',None),
        SlotSet('DOB',None),SlotSet('CELL',None),SlotSet('CITY',None),SlotSet('EMAIL',None),SlotSet('Address',None),
                SlotSet('REGISTRATION',None)]

    class ActionCustomFallback(Action):

        def name(self) -> Text:
            return "custom_fallback_action"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            dispatcher.utter_message(template="utter_custom")
            return [UserUtteranceReverted()]

    class ActionAskAffirmation(Action):

        def name(self) -> Text:
            return "prev_action_default_ask_affirmation"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            dispatcher.utter_message(template="utter_ask_affirmation")
            return [UserUtteranceReverted()]

    class YourResidence(Action):

        def name(self) -> Text:
            return "action_your_residence"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            # Calling the DB
            # calling an API
            # do anything
            # all caluculations are done
            dispatcher.utter_message(template="utter_residence")

            return [UserUtteranceReverted(), FollowupAction(tracker.active_form.get('name'))]


class ActionFormInfo(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_info"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["NAME", "DOB", "Address", "CELL", "CITY", "COURSE", "EMAIL", "GENDER", "REGISTRATION", "SCHOOL", ]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        Name = tracker.get_slot('NAME'),
        gender = tracker.get_slot('GENDER'),
        school = tracker.get_slot('SCHOOL'),
        course = tracker.get_slot('COURSE'),
        dob = tracker.get_slot('DOB'),
        cell = tracker.get_slot('CELL'),
        city = tracker.get_slot('CITY'),
        email = tracker.get_slot('EMAIL'),
        address = tracker.get_slot('Address'),
        REGISTRATION = tracker.get_slot('REGISTRATION')
        dispatcher.utter_message(template="utter_submit", school='SCHOOL'
                                 )

        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "NAME": [self.from_text()],
            "GENDER": [self.from_text()],
            "SCHOOL": [self.from_text()],
            "COURSE": [self.from_text()],
            "DOB": [self.from_text()],
            "CELL": [self.from_text()],
            "CITY": [self.from_text()],
            "EMAIL": [self.from_text()],
            "Address": [self.from_text()],
            "REGISTRATION": [self.from_text()]
        }
