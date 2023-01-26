## Greet 
* greet
  - utter_how_can_I_help
## happy path
* greet
  - utter_how_can_I_help
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_how_can_I_help
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_how_can_I_help
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## hostel_meaning
* hostel-meaning
  - utter_hostel_meaning

## what-hostel-owner
* what_hostel_owner
  - utter_what_hostel_owner



## facilities-private-hostels
* facilities-private-hostels
  - utter_facilities_private_hostels

## list-private-hostel-owners
* list-private-hostel-owners
  - utter_list_private_hostel_owners

## specificities-real-estate-hostels
* specificities-real-estate-hostels
  - utter_specificities_real_estate_hostels

## list-real-estate
* list-real-estate
  - utter_list_real_estate


## what-hostel-types
* what-hostel-types
  - utter_what_hostel_types

## more-info-NUST-shared-hostel
* more-info-NUST-shared-hostel
  - utter_more_info_NUST_shared_hostel

## more-info-nust-bedsit
* more-info-nust-bedsit
  - utter_more_info_nust_bedsit

## more-info-NUST-studios
* more-info-NUST-studios
  - utter_more_info_NUST_studios

## more-info-NUST-family-hostel
* more-info-NUST-family-hostel
  - utter_more_info_NUST_family_hostel

## more-info-adapted-hostels
* more-info-adapted-hostels
  - utter_more_info_adapted_hostels

## where-hostels
* where-hostels
  - utter_where_hostels

## are-there-hotels
* are-there-hotels
  - utter_are_there_hotels

## are-there-youth-hostels
* are-there-youth-hostels
  - utter_are_there_youth_hostels

## useful-info-hostels
* useful-info-hostels
  - utter_useful_info_hostels

## info-support-hostel
* info-support-hostel
  - utter_info_support_hostel

## what-housing-possibilities
* what-housing-possibilities
  - utter_what_housing_possibilities

## get-nust-hostel_affirm
* get-nust-hostel
    - form_info
    - form{"name": "form_info"}
    - form{"name": null}
    - utter_submit_data
* affirm
   - action_submit_data

## get-nust-hostel_deny
* get-nust-hostel
    - form_info
    - form{"name": "form_info"}
    - form{"name": null}
    - utter_submit_data
* deny
  - utter_thanks


* goodbye
  - utter_goodbye
## contact-NUST-housing-service
* contact-NUST-housing-service
  - utter_contact_NUST_housing_service

## get-private-hostel
* get-private-hostel
  - utter_get_private_hostel

## get-real-estate-hostel
* get-real-estate-hostel
  - utter_get-real_estate_hostel

## get-hostel-keys
* get-hostel-keys
  - utter_get_hostel_keys

## price-NUST-hostels
* price-NUST-hostels
  - utter_price_NUST_hostels


## what-if-not-pay-hostel
* what-if-not-pay-hostel
  - utter_what_if_not_pay_hostel

## get-hostel-request-proof
* get-hostel-request-proof
  - utter_get_hostel_request_proof


## first-thing-to-do-hostel
* first-thing-to-do-hostel
  - utter_first_thing_to_do_hostel

## to-do-before-leaving-hostel
* to-do-before-leaving-hostel
  - utter_to_do_before_leaving_hostel

## no-exit-inventory
* no-exit-inventory
  - utter_no_exit_inventory

## may-sublet
* may-sublet
  - utter_may_sublet

## what-charges-for-hostel
* what-charges-for-hostel
  - utter_what_charges_for_hostel

## Boys_Hostels
* Boys_Hostels
  - utter_Boys_Hostels

## Girls_Hostels
* Girls_Hostels
  - utter_Girls_Hostels

## default fallbac
* bot_challenge
  - action_custom_fallback
  

## scholarships
* scholarship
  - utter_scholar
## summer warnings
* summer_warning
  - utter_summer
## admission schedules
* admission_schedule
  - utter_schedule
## fee structure
* fee_structure
  - utter_fee
## how-pay-monthly-hostel
* how-pay-monthly-hostel
  - utter_how_pay_monthly_hostel




## graduation time
* graduation
  - utter_graduate
## facilities-nust-hostels
* facilities-nust-hostels
  - utter_facilities_nust_hostels




## summer courses
* summer_courses
  - utter_summer_courses

## why nust
* nust
  - utter_NUST

## job rate at fast
* job_rate
  - utter_job

## social eventsat fast
* social_events
  - utter_events

## past papers
* past_papers
  - utter_sample

## eligibility criteria
* admission
  - utter_recruit

## A eligibility criteria
* admission2
  - utter_admins

## NET
* NET
  - utter_net

## SAT
* SAT
  - utter_SAT

## tests conducted
* tests_conducted
  - utter_tests

## apply
* apply
  - utter_apply



## offered programs
* offered_programs
  - utter_programs

## hostel
* hostel
  - utter_hostel

## test pattern
* test_pattern
  - utter_pattern

## negative marking
* negative_marking
  - utter_negative

## evening classes
* evening_classes
  - utter_evening

## sports seats
* sports_seats
  - utter_sports


## self finance
* self_finance
  - utter_self


## domicile
* domicile
  - utter_domicile

## aggregate
* aggregate
  - utter_aggregate

## academic period
* academic_period
  - utter_period

## Warning
* Warning
  - utter_Warning


## Fyp Registration
* Fyp_Registration
  - utter_fyp


## Transfer
* Transfer
  - utter_Transfer


## GPA I
* GPA_I
  - utter_gpai

## GPA
* GPA
  - utter_gpa

## credit hour
* credit_hour
  - utter_credit

## classes
* classes
  - utter_class

## Admission of former
* Admission_of_former
  - utter_former

## awaited admission
* awaited_admission
  - utter_awaited

## semester week
* semester_week
  - utter_semester

## summer campus
* summer_campus
  - utter_campus

## summer withdraw
* summer_withdraw
  - utter_sum

## new summer
* new_summer
  - utter_new

## improve gpa
* improve_gpa
  - utter_improve

## freezing semester
* freezing_semester
  - utter_freezing

## Rechecking paper
* Rechecking_paper
  - utter_Rechecking

## degree duration
* degree_duration
  - utter_degree

## spring admission
* spring_admission
  - utter_spring

## withdraw course
* withdraw_course
  - utter_withdraw

## medals
* medals
  - utter_medal


## career office
* career_office
  - utter_career

## dean
* dean
  - utter_dean


## headquarter
* headquarter
  - utter_headquarter


## nust_isb_address
* nust_isb_address
  - utter_isb

## nust_blo_address
* nust_blo_address
  - utter_blo

## nust_khi_address
* nust_khi_address
  - utter_khi


## nust_rwp_address
* nust_rwp_address
  - utter_rwp



## library
* library
  - utter_library



## cafeteria
* cafeteria
  - utter_cafeteria


## mosque
* mosque
  - utter_mosque


## auditorium
* auditorium
  - utter_auditorium

## bast campus
* best_campus
  - utter_bestcampus


## academic office
* academic_office
  - utter_academic

## admin office
* admin_office
  - utter_admin

## student affair office
* students_affair
  - utter_students

## hod office
* hod_office
  - utter_hod

## director office
* director_office
  - utter_director

## contacts
* contacts
  - utter_contacts

## information_extract
* information_extract
   - form_reg
   - form{"name": "form_reg"}
   - form{"name": null}
   - slot{"REGISTRATION": 2}
   - action_data_extract





