# Copyright 2017 David Lewis
# This file is part of the Villanova tour guide mrcroft skill
from os.path import dirname, abspath

import sys
import requests
import json
import threading

sys.path.append(abspath(dirname(__file__)))

from adapt.intent import IntentBuilder

try:
    from mycroft.skills.core import MycroftSkill
except:
    class MycroftSkill:
        pass

#from mycroft.util.log import getLogger

import GPIO

__author__ = 'dlew'

LOGGER = getLogger(__name__)

class TourGuideSkill(MycroftSkill):
		def on_led_change(self):
	        	status = GPIO.get("GPIO1")
		        #self.speak("Led is %s" % status)
	
		def __init__(self):
				GPIO.on("GPIO1",self.on_led_change)
				GPIO.on("GPIO2",self.on_led_change)
				GPIO.on("GPIO3",self.on_led_change)
				GPIO.on("GPIO4",self.on_led_change)
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

				# ---------------------------------------------------------------------------------

				alumni_network_intent = IntentBuilder("AlumniNetworkIntent"). \
						require("AlumniNetworkKeyword").build()
				self.register_intent(alumni_network_intent, self.handle_alumni_network_intent)

				# ---------------------------------------------------------------------------------
				
				campus_size_intent = IntentBuilder("CampusSizeIntent"). \
						require("CampusSizeKeyword").build()
				self.register_intent(campus_size_intent, self.handle_campus_size_intent)
				
				# ---------------------------------------------------------------------------------
				
				class_size_intent = IntentBuilder("ClassSizeIntent"). \
						require("ClassSizeKeyword").build()
				self.register_intent(class_size_intent, self.handle_class_size_intent)

				# ---------------------------------------------------------------------------------

				college_liberal_arts_average_salary_intent = IntentBuilder("CollegeLiberalArtsAverageSalaryIntent"). \
						require("CollegeLiberalArtsAverageSalaryKeyword").build()
				self.register_intent(college_liberal_arts_average_salary_intent, self.handle_college_liberal_arts_average_salary_intent)

				# ---------------------------------------------------------------------------------

				college_liberal_arts_job_placement_intent = IntentBuilder("CollegeLiberalArtsJobPlacementIntent"). \
						require("CollegeLiberalArtsJobPlacementKeyword").build()
				self.register_intent(college_liberal_arts_job_placement_intent, self.handle_college_liberal_arts_job_placement_intent)

				# ---------------------------------------------------------------------------------

				college_science_average_salary_intent = IntentBuilder("CollegeScienceAverageSalarayIntent"). \
						require("CollegeLiberalArtsAverageSalaryKeyword").build()
				self.register_intent(college_science_average_salary_intent, self.handle_college_science_average_salary_intent)

				# ---------------------------------------------------------------------------------

				college_science_job_placement_intent = IntentBuilder("CollegeScienceJobPlacementIntent"). \
						require("CollegeScienceJobPlacementKeyword").build()
				self.register_intent(college_science_job_placement_intent, self.handle_college_science_job_placement_intent)

				# ---------------------------------------------------------------------------------

				engineering_formula_intent = IntentBuilder("EngineeringFormulaIntent"). \
						require("EngineeringFormulaKeyword").build()
				self.register_intent(engineering_formula_intent, self.handle_engineering_formula_intent)

				# ---------------------------------------------------------------------------------

				engineering_freshman_curriculum_intent = IntentBuilder("EngineeringFreshmanCurriculumIntent"). \
						require("EngineeringFreshmanCurriculumKeyword").build()
				self.register_intent(engineering_freshman_curriculum_intent, self.handle_engineering_freshman_curriculum_intent)

				# ---------------------------------------------------------------------------------

				engineering_mini_project_intent = IntentBuilder("EngineeringMiniProjectIntent"). \
						require("EngineeringMiniProjectKeyword").build()
				self.register_intent(engineering_mini_project_intent, self.handle_engineering_mini_project_intent)

				# ---------------------------------------------------------------------------------

				engineering_professional_development_intent = IntentBuilder("EngineeringProfessionalDevelopmentIntent"). \
						require("EngineeringProfessionalDevelopmentKeyword").build()
				self.register_intent(engineering_professional_development_intent, self.handle_engineering_professional_development_intent)

				# ---------------------------------------------------------------------------------

				engineering_projects_trips_intent = IntentBuilder("EngineeringProjectsTripsIntent"). \
						require("EngineeringProjectsTripsKeyword").build()
				self.register_intent(engineering_projects_trips_intent, self.handle_engineering_projects_trips_intent)

				# ---------------------------------------------------------------------------------

				engineering_resources_intent = IntentBuilder("EngineeringResourcesIntent"). \
						require("EngineeringResourcesKeyword").build()
				self.register_intent(engineering_resources_intent, self.handle_engineering_resources_intent)

				# ---------------------------------------------------------------------------------

				engineering_service_intent = IntentBuilder("EngineeringServiceIntent"). \
						require("EngineeringServiceKeyword").build()
				self.register_intent(engineering_service_intent, self.handle_engineering_service_intent)

				# ---------------------------------------------------------------------------------

				engineering_study_abroad_intent = IntentBuilder("EngineeringStudyAbroadIntent"). \
						require("EngineeringStudyAbroadKeyword").build()
				self.register_intent(engineering_study_abroad_intent, self.handle_engineering_study_abroad_intent)

				# ---------------------------------------------------------------------------------

				engineering_undergrad_intent = IntentBuilder("EngineeringUndergradIntent"). \
						require("EngineeringUndergradKeyword").build()
				self.register_intent(engineering_undergrad_intent, self.handle_engineering_undergrad_intent)

				# ---------------------------------------------------------------------------------

				engineering_women_intent = IntentBuilder("EngineeringWomenIntent"). \
						require("EngineeringWomenKeyword").build()
				self.register_intent(engineering_women_intent, self.handle_engineering_women_intent)

				# ---------------------------------------------------------------------------------

				financial_aid_eligibility_intent = IntentBuilder("FinancialAidEligibilityIntent"). \
						require("FinancialAidEligibilityKeyword").build()
				self.register_intent(financial_aid_eligibility_intent, self.handle_financial_aid_eligibility_intent)

				# ---------------------------------------------------------------------------------

				graduation_rate_intent = IntentBuilder("GraduationRateIntent"). \
						require("GraduationRateKeyword").build()
				self.register_intent(graduation_rate_intent, self.handle_graduation_rate_intent)

				# ---------------------------------------------------------------------------------

				honors_program_intent = IntentBuilder("HonorsProgramIntent"). \
						require("HonorsProgramKeyword").build()
				self.register_intent(honors_program_intent, self.handle_honors_program_intent)

				# ---------------------------------------------------------------------------------

				nursing_facts_intent = IntentBuilder("NursingFactsIntent"). \
						require("NursingFactsKeyword").build()
				self.register_intent(nursing_facts_intent, self.handle_nursing_facts_intent)

				# ---------------------------------------------------------------------------------

				nursing_job_placement_intent = IntentBuilder("NursingJobPlacementIntent"). \
						require("NursingJobPlacementKeyword").build()
				self.register_intent(nursing_job_placement_intent, self.handle_nursing_job_placement_intent)

				# ---------------------------------------------------------------------------------

				nursing_salary_intent = IntentBuilder("NursingSalaryIntent"). \
						require("NursingSalaryKeyword").build()
				self.register_intent(nursing_salary_intent, self.handle_nursing_salary_intent)

				# ---------------------------------------------------------------------------------

				random_quote_intent = IntentBuilder("RandomQuoteIntent"). \
						require("RandomQuoteKeyword").build()
				self.register_intent(random_quote_intent, self.handle_random_quote_intent)

				# ---------------------------------------------------------------------------------

				retention_rate_intent = IntentBuilder("RetentionRateIntent"). \
						require("RetentionRateKeyword").build()
				self.register_intent(retention_rate_intent, self.handle_retention_rate_intent)

				# ---------------------------------------------------------------------------------

				research_opportunities_fields_intent = IntentBuilder("ResearchOpportunitiesFieldsIntent"). \
						require("ResearchOpportunitiesFieldsKeyword").build()
				self.register_intent(research_opportunities_fields_intent, self.handle_research_opportunities_fields_intent)

				# ---------------------------------------------------------------------------------

				ROTC_program_intent = IntentBuilder("ROTCProgremIntent"). \
						require("ROTCProgramKeyword").build()
				self.register_intent(ROTC_program_intent, self.handle_ROTC_program_intent)

				# ---------------------------------------------------------------------------------

				school_history_fun_facts_intent = IntentBuilder("SchoolHistoryFunFactsIntent"). \
						require("SchoolHistoryFunFactsKeyword").build()
				self.register_intent(school_history_fun_facts_intent, self.handle_school_history_fun_facts_intent)

				# ---------------------------------------------------------------------------------

				service_fun_facts_intent = IntentBuilder("ServiceFunFactsIntent"). \
						require("ServiceFunFactsKeyword").build()
				self.register_intent(service_fun_facts_intent, self.handle_service_fun_facts_intent)

				# ---------------------------------------------------------------------------------

				social_clubs_intent = IntentBuilder("SocialClubsIntent"). \
						require("SocialClubsKeyword").build()
				self.register_intent(social_clubs_intent, self.handle_social_clubs_intent)

				# ---------------------------------------------------------------------------------

				social_housing_intent = IntentBuilder("SocialHousingIntent"). \
						require("SocialHousingKeyword").build()
				self.register_intent(social_housing_intent, self.handle_social_housing_intent)

				# ---------------------------------------------------------------------------------

				social_public_safety_intent = IntentBuilder("SocialPublicSafetyIntent"). \
						require("SocialPublicSafetyKeyword").build()
				self.register_intent(social_public_safety_intent, self.handle_social_public_safety_intent)

				# ---------------------------------------------------------------------------------

				social_travel_intent = IntentBuilder("SocialTravelIntent"). \
						require("SocialTravelKeyword").build()
				self.register_intent(social_travel_intent, self.handle_social_travel_intent)

				# ---------------------------------------------------------------------------------

				sports_academics_intent = IntentBuilder("SportsAcademicsIntent"). \
						require("SportsAcademicsKeyword").build()
				self.register_intent(sports_academics_intent, self.handle_sports_academics_intent)

				# ---------------------------------------------------------------------------------

				sports_national_championships_intent = IntentBuilder("SportsNationalChampionshipsIntent"). \
						require("SportsNationalChampionshipsKeyword").build()
				self.register_intent(sports_national_championships_intent, self.handle_sports_national_championships_intent)

				# ---------------------------------------------------------------------------------

				sports_olympics_intent = IntentBuilder("SportsOlympicsIntent"). \
						require("SportsOlympicsKeyword").build()
				self.register_intent(sports_olympics_intent, self.handle_sports_olympics_intent)

				# ---------------------------------------------------------------------------------

				teachers_fun_fact_intent = IntentBuilder("TeachersFunFactIntent"). \
						require("TeachersFunFactKeyword").build()
				self.register_intent(teachers_fun_fact_intent, self.handle_teachers_fun_fact_intent)

				# ---------------------------------------------------------------------------------

				total_enrollment_intent = IntentBuilder("TotalEnrollmentIntent"). \
						require("TotalEnrollmentKeyword").build()
				self.register_intent(total_enrollment_intent, self.handle_total_enrollment_intent)

				# ---------------------------------------------------------------------------------

				university_ranking_intent = IntentBuilder("UniversityRankingIntent"). \
						require("UniversityRankingKeyword").build()
				self.register_intent(university_ranking_intent, self.handle_university_ranking_intent)

				# ---------------------------------------------------------------------------------

				VSB_ranking_intent = IntentBuilder("VSBRankingIntent"). \
						require("VSBRankingKeyword").build()
				self.register_intent(VSB_ranking_intent, self.handle_VSB_ranking_intent)

				# ---------------------------------------------------------------------------------

				VSB_synopsis_intent = IntentBuilder("VSBSynopsisIntent"). \
						require("VSBSynopsisKeyword").build()
				self.register_intent(VSB_synopsis_intent, self.handle_VSB_synopsis_intent)

				# ---------------------------------------------------------------------------------

				austin_hall_intent = IntentBuilder("AustinHallIntent"). \
						require("AustinHallKeyword").build()
				self.register_intent(austin_hall_intent, self.handle_austin_hall_intent)

				# ---------------------------------------------------------------------------------

				CEER_intent = IntentBuilder("CEERIntent"). \
						require("CEERKeyword").build()
				self.register_intent(CEER_intent, self.handle_CEER_intent)

				# ---------------------------------------------------------------------------------

				church_intent = IntentBuilder("ChurchIntent"). \
						require("ChurchKeyword").build()
				self.register_intent(church_intent, self.handle_church_intent)

				# ---------------------------------------------------------------------------------

				connelly_intent = IntentBuilder("ConnellyIntent"). \
						require("ConnellyKeyword").build()
				self.register_intent(connelly_intent, self.handle_connelly_intent)

				# ---------------------------------------------------------------------------------

				library_intent = IntentBuilder("LibraryIntent"). \
						require("LibraryKeyword").build()
				self.register_intent(library_intent, self.handle_library_intent)

				# ---------------------------------------------------------------------------------

				mendel_intent = IntentBuilder("MendelIntent"). \
						require("MendelKeyword").build()
				self.register_intent(mendel_intent, self.handle_mendel_intent)

				# ---------------------------------------------------------------------------------

				oreo_intent = IntentBuilder("OreoIntent"). \
						require("OreoKeyword").build()
				self.register_intent(oreo_intent, self.handle_oreo_intent)

				# ---------------------------------------------------------------------------------

				south_campus_intent = IntentBuilder("SouthCampusIntent"). \
						require("SouthCampusKeyword").build()
				self.register_intent(south_campus_intent, self.handle_south_campus_intent)

				# ---------------------------------------------------------------------------------

				tolentine_intent = IntentBuilder("TolentineIntent"). \
						require("TolentineKeyword").build()
				self.register_intent(tolentine_intent, self.handle_tolentine_intent)

				# ---------------------------------------------------------------------------------

				west_campus_intent = IntentBuilder("WestCampusIntent"). \
						require("WestCampusKeyword").build()
				self.register_intent(west_campus_intent, self.handle_west_campus_intent)

				# ---------------------------------------------------------------------------------

				aerospace_engineering_intent = IntentBuilder("AeorspaceEngineeringIntent"). \
						require("AerospcaeEngineeringKeyword").build()
				self.register_intent(aerospace_engineering_intent, self.handle_aerospace_engineering_intent)

				# ---------------------------------------------------------------------------------

				bartley_hall_intent = IntentBuilder("BartleyHallIntent"). \
						require("BartleyHallKeyword").build()
				self.register_intent(bartley_hall_intent, self.handle_bartley_hall_intent)

				# ---------------------------------------------------------------------------------

				bathroom_directions_intent = IntentBuilder("BathroomDirectionsIntent"). \
						require("BathroomDirectionsKeyword").build()
				self.register_intent(bathroom_directions_intent, self.handle_bathroom_directions_intent)

				# ---------------------------------------------------------------------------------

				biomedical_engineering_intent = IntentBuilder("BiomedicalEngineeringIntent"). \
						require("BiomedicalEngineeringKeyword").build()
				self.register_intent(biomedical_engineering_intent, self.handle_biomedical_engineering_intent)

				# ---------------------------------------------------------------------------------

				chemical_engineering_intent = IntentBuilder("ChemicalEngineeringIntent"). \
						require("ChemicalEngineeringKeyword").build()
				self.register_intent(chemical_engineering_intent, self.handle_chemical_engineering_intent)

				# ---------------------------------------------------------------------------------

				civil_engineering_intent = IntentBuilder("CivilEngineeringIntent"). \
						require("CivilEngineeringKeyword").build()
				self.register_intent(civil_engineering_intent, self.handle_civil_engineering_intent)

				# ---------------------------------------------------------------------------------

				computer_engineering_intent = IntentBuilder("ComputerEngineeringIntent"). \
						require("ComputerEngineeringKeyword").build()
				self.register_intent(computer_engineering_intent, self.handle_computer_engineering_intent)

				# ---------------------------------------------------------------------------------

				davis_center_pavilion_intent = IntentBuilder("DavisCenterPavilionIntent"). \
						require("DavisCenterPavilionKeyword").build()
				self.register_intent(davis_center_pavilion_intent, self.handle_davis_center_pavilion_intent)

				# ---------------------------------------------------------------------------------

				electrical_engineering_intent = IntentBuilder("ElectricalEngineeringIntent"). \
						require("ElectricalEngineeringKeyword").build()
				self.register_intent(electrical_engineering_intent, self.handle_electrical_engineering_intent)

				# ---------------------------------------------------------------------------------

				engineering_entrepreneurship_intent = IntentBuilder("EngineeringEntrepreneurshipIntent"). \
						require("EngineeringEntrepreneurshipKeyword").build()
				self.register_intent(engineering_entrepreneurship_intent, self.handle_engineering_entrepreneurship_intent)

				# ---------------------------------------------------------------------------------

				health_services_intent = IntentBuilder("HealthServicesIntent"). \
						require("HealthServicesKeyword").build()
				self.register_intent(health_services_intent, self.handle_health_services_intent)

				# ---------------------------------------------------------------------------------

				mechanical_engineering_intent = IntentBuilder("MechanicalEngineeringIntent"). \
						require("MechanicalEngineeringKeyword").build()
				self.register_intent(mechanical_engineering_intent, self.handle_mechanical_engineering_intent)

				# ---------------------------------------------------------------------------------

				mechatronic_engineering_intent = IntentBuilder("MechatronicEngineeringIntent"). \
						require("MechatronicEngineeringKeyword").build()
				self.register_intent(mechatronic_engineering_intent, self.handle_mechatronic_engineering_intent)

				# ---------------------------------------------------------------------------------

				quad_intent = IntentBuilder("QuadIntent"). \
						require("QuadKeyword").build()
				self.register_intent(quad_intent, self.handle_quad_intent)

				# ---------------------------------------------------------------------------------

				st_marys_hall_directions_intent = IntentBuilder("StMarysHallDirectionsIntent"). \
						require("StMarysHallDirectionsKeyword").build()
				self.register_intent(st_marys_hall_directions_intent, self.handle_st_marys_hall_directions_intent)

				# ---------------------------------------------------------------------------------

				techzone_directions_intent = IntentBuilder("TechZoneDirectionsIntent"). \
						require("TechZoneDirectionsKeyword").build()
				self.register_intent(techzone_directions_intent, self.handle_techzone_directions_intent)

				# ---------------------------------------------------------------------------------

				water_fountain_directions_intent = IntentBuilder("WaterFountainDirectionsIntent"). \
						require("WaterFountainDirectionsKeyword").build()
				self.register_intent(water_fountain_directions_intent, self.handle_water_fountain_directions_intent)


		def handle_fun_fact_villanova_intent(self, message):
				self.speak_dialog("fun.fact.villanova")

		def handle_college_majors_intent(self, message):
				#self.speak_dialog("college.majors")
				GPIO.set("GPIO1","On")
				GPIO.set("GPIO2","On")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","On")
				#self.speak_dialog("college.majors")

		def handle_college_minors_intent(self, message):
				self.speak_dialog("college.minors")

		def handle_engineering_resources_intent(self, message):
				self.speak_dialog("college.majors")

		def handle_engineering_projects_trips_intent(self, message):
				self.speak_dialog("college.majors")

		def handle_alumni_network_intent(self, message):
				self.speak_dialog("alumni.network")

		def handle_campus_size_intent(self, message):
				self.speak_dialog("campus.size")

		def handle_class_size_intent(self, message):
				self.speak_dialog("class.size")

		def handle_college_liberal_arts_average_salary_intent(self, message):
				self.speak_dialog("college.liberal.arts.average.salary")

		def handle_college_liberal_arts_job_placement_intent(self, message):
				self.speak_dialog("college.liberal.arts.job.placement")

		def handle_college_science_average_salary_intent(self, message):
				self.speak_dialog("college.science.average.salary")
		
		def handle_college_science_job_placement_intent(self, message):
				self.speak_dialog("college.science.job.placement")

		def handle_engineering_formula_intent(self, message):
				self.speak_dialog("engineering.formula")

		def handle_engineering_freshman_curriculum_intent(self, message):
				self.speak_dialog("engineering.freshman.curriculum")

		def handle_engineering_mini_project_intent(self, message):
				self.speak_dialog("engineering.mini.project")

		def handle_engineering_professional_development_intent(self, message):
				self.speak_dialog("engineering.professional.development")

		def handle_engineering_projects_trips_intent(self, message):
				self.speak_dialog("engineering.projects.trips")

		def handle_engineering_resources_intent(self, message):
				self.speak_dialog("engineering.resources")

		def handle_engineering_service_intent(self, message):
				self.speak_dialog("engineering.service")

		def handle_engineering_study_abroad_intent(self, message):
				self.speak_dialog("engineering.study.abroad")

		def handle_engineering_undergrad_intent(self, message):
				self.speak_dialog("engineering.undergrad")

		def handle_engineering_women_intent(self, message):
				self.speak_dialog("engineering.women")

		def handle_financial_aid_eligibility_intent(self, message):
				self.speak_dialog("financial.aid.eligibility")

		def handle_graduation_rate_intent(self, message):
				self.speak_dialog("graduation.rate")

		def handle_honors_program_intent(self, message):
				self.speak_dialog("honors.program")

		def handle_nursing_facts_intent(self, message):
				self.speak_dialog("nursing.facts")

		def handle_nursing_job_placement_intent(self, message):
				self.speak_dialog("nursing.job.placement")

		def handle_nursing_salary_intent(self, message):
				self.speak_dialog("nursing.salary")

		def handle_random_quote_intent(self, message):
				self.speak_dialog("random.quote")

		def handle_research_opportunities_fields_intent(self, message):
				self.speak_dialog("research.opportunities.fields")

		def handle_retention_rate_intent(self, message):
				self.speak_dialog("retention.rate")

		def handle_ROTC_program_intent(self, message):
				self.speak_dialog("ROTC.program")

		def handle_school_history_fun_facts_intent(self, message):
				self.speak_dialog("school.history.fun.facts")

		def handle_service_fun_facts_intent(self, message):
				self.speak_dialog("service.fun.facts")

		def handle_social_clubs_intent(self, message):
				self.speak_dialog("social.clubs")

		def handle_social_housing_intent(self, message):
				self.speak_dialog("social.housing")

		def handle_social_public_safety_intent(self, message):
				self.speak_dialog("social.public.safety")

		def handle_social_travel_intent(self, message):
				self.speak_dialog("social.travel")

		def handle_sports_academics_intent(self, message):
				self.speak_dialog("sports.academics")

		def handle_sports_national_championships_intent(self, message):
				self.speak_dialog("sports.national.championships")

		def handle_sports_olympics_intent(self, message):
				self.speak_dialog("sports.olympics")

		def handle_teachers_fun_fact_intent(self, message):
				self.speak_dialog("teachers.fun.fact")

		def handle_total_enrollment_intent(self, message):
				self.speak_dialog("total.enrollment")

		def handle_university_ranking_intent(self, message):
				self.speak_dialog("university.ranking")

		def handle_VSB_average_salary_intent(self, message):
				self.speak_dialog("VSB.average.salary")

		def handle_VSB_job_placement_intent(self, message):
				self.speak_dialog("VSB.job.placement")

		def handle_VSB_ranking_intent(self, message):
				self.speak_dialog("VSB.ranking")

		def handle_VSB_synopsis_intent(self, message):
				self.speak_dialog("VSB.synopsis")

		def handle_austin_hall_intent(self, message):
				self.speak_dialog("austin.hall")

		def handle_CEER_intent(self, message):
				self.speak_dialog("CEER")

		def handle_church_intent(self, message):
				self.speak_dialog("church")

		def handle_connelly_intent(self, message):
				self.speak_dialog("connelly")

		def handle_library_intent(self, message):
				self.speak_dialog("library")

		def handle_mendel_intent(self, message):
				self.speak_dialog("mendel")

		def handle_oreo_intent(self, message):
				self.speak_dialog("oreo")

		def handle_south_campus_intent(self, message):
				self.speak_dialog("south.campus")

		def handle_tolentine_intent(self, message):
				self.speak_dialog("tolentine")

		def handle_west_campus_intent(self, message):
				self.speak_dialog("west.campus")

		def handle_aerospace_engineering_intent(self, message):
				self.speak_dialog("aerospace.engineering")

		def handle_bartley_hall_intent(self, message):
				self.speak_dialog("bartley.hall")

		def handle_bathroom_directions_intent(self, message):
				self.speak_dialog("bathroom.directions")

		def handle_biomedical_engineering_intent(self, message):
				self.speak_dialog("biomedical.engineering")

		def handle_chemical_engineering_intent(self, message):
				self.speak_dialog("chemical.engineering")

		def handle_civil_engineering_intent(self, message):
				self.speak_dialog("civil.engineering")

		def handle_computer_engineering_intent(self, message):
				self.speak_dialog("computer.engineering")

		def handle_davis_center_pavilion_intent(self, message):
				self.speak_dialog("davis.center.pavilion")

		def handle_electrical_engineering_intent(self, message):
				self.speak_dialog("electrical.engineering")

		def handle_engineering_entrepreneurship_intent(self, message):
				self.speak_dialog("engineering.entrepreneurship")

		def handle_health_services_intent(self, message):
				self.speak_dialog("health.services")

		def handle_mechanical_engineering_intent(self, message):
				self.speak_dialog("mechanical.engineering")

		def handle_mechatronic_engineering_intent(self, message):
				self.speak_dialog("mechatronic.engineering")

		def handle_quad_intent(self, message):
				self.speak_dialog("quad")

		def handle_st_marys_hall_directions_intent(self, message):
				self.speak_dialog("st.marys.hall.directions")

		def handle_techzone_directions_intent(self, message):
				self.speak_dialog("techzone.directions")

		def handle_water_fountain_directions_intent(self, message):
				self.speak_dialog("water.fountain.directions")
				
		def stop(self):
				pass

def create_skill():
		return TourGuideSkill()
