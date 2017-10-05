# Copyright 2017 David Lewis
# This file is part of the Villanova tour guide mrcroft skill
from os.path import dirname

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'dlew'

LOGGER = getLogger(__name__)

class TourGuideSkill(MycroftSkill):
		def __init__(self):
				super(TourGuideSkill, self).__init__(name="TourGuideSkill")

		def initialize(self):
				fun_fact_villanova_intent = IntentBuilder("FunFactVillanovaIntent"). \
						require("FunFactVillanovaKeyword").build()
				self.register_intent(fun_fact_villanova_intent, self.handle_fun_fact_villanova_intent)

				# ---------------------------------------------------------------------------------

				college_majors_intent = IntentBuilder("CollegeMajorsIntent"). \
						require("CollegeMajorsKeyword").build()
				self.register_intent(college_majors_intent, self.handle_college_majors_intent)

				# ---------------------------------------------------------------------------------

				college_minors_intent = IntentBuilder("CollegeMinorsIntent"). \
						require("CollegeMinorsKeyword").build()
				self.register_intent(college_minors_intent, self.handle_college_minors_intent)

				# ---------------------------------------------------------------------------------

				engineering_resources_intent = IntentBuilder("EngineeringResourcesIntent"). \
						require("EngineeringResourcesKeyword").build()
				self.register_intent(engineering_resources_intent, self.handle_engineering_resources_intent)

				# ---------------------------------------------------------------------------------

				engineering_projects_trips_intent = IntentBuilder("EngineeringProjectsTripsIntent"). \
						require("EngineeringProjectsTripsKeyword").build()
				self.register_intent(engineering_projects_trips_intent, self.handle_engineering_projects_trips_intent)


		def handle_fun_fact_villanova_intent(self, message):
				self.speak_dialog("fun.fact.villanova")

		def handle_college_majors_intent(self, message):
				self.speak_dialog("college.majors")

		def handle_college_minors_intent(self, message):
				self.speak_dialog("college.minors")

		def handle_engineering_resources_intent(self, message):
				self.speak_dialog("engineering.resources")

		def handle_engineering_projects_trips_intent(self, message):
				self.speak_dialog("engineering.projects.trips")

		def stop(self):
				pass

def create_skill():
		return TourGuideSkill()
