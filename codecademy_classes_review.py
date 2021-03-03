#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 15:33:03 2021

@author: lilygoodyersait
"""
class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker =  smoker
  def estimated_insurance_cost(self):
    estimated_cost= 250*self.age - 128*self.sex + 370*self.bmi + 425*self.num_of_children + 24000*self.smoker - 12500
    print("""{}'s estimated insurance cost is {} dollars""".format(self.name, str(estimated_cost)))
  def update_age(self, new_age):
    self.age = new_age
    print("{} is now {} years old".format(self.name, str(self.age)))
    self.estimated_insurance_cost()
  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children == 1:

      print("{} has {} child".format(self.name,str(self.num_of_children)))
    else:
      print("{} has {} children".format(self.name,str(self.num_of_children)))
    self.estimated_insurance_cost()
  def patient_profile(self):
    patient_info={}
    patient_info["name"]= self.name
    patient_info["age"]= self.age
    patient_info["bmi"]= self.bmi
    patient_info["num_of_children"]=self.num_of_children
    patient_info["smoker"]= self.smoker
    return patient_info
  def update_bmi(self, new_bmi):
    self.bmi = new_bmi
    print("{} now has a bmi of {}".format(self.name, str(self.bmi)))
    self.estimated_insurance_cost()
     



patient1= Patient("John Doe", 25, 1, 22.2, 0, 0)

print(patient1.name)
print(patient1.age)
print(patient1.sex)
print(patient1.bmi)
print(patient1.num_of_children)
print(patient1.smoker)

patient1.estimated_insurance_cost()
patient1.update_age(26)
patient1.update_num_children(1)
print(patient1.patient_profile())
patient1.update_bmi(56)