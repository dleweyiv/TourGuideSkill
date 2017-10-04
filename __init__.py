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

				college_majors_intent = IntentBuilder("CollegeMajorsIntent"). \
						require("CollegeMajorsKeyword").build()
				self.register_intent(college_majors_intent, self.handle_college_majors_intent)


		def handle_fun_fact_villanova_intent(self, message):
				self.speak_dialog("fun.fact.villanova")

		def handle_college_majors_intent(self, message):
				self_speak_dialog("college.majors")

		def stop(self):
				pass

def create_skill():
		return TourGuideSkill()