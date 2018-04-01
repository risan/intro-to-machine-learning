# coding: utf-8
"""Exploring Enron Dataset"""
import os
import pprint
import pickle

def data_path(path):
    """Get the absolute path.

    :param str path: The path relative to this file directory
    :return: The full path to the given data path
    :rtype: str
    """
    dirname = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.abspath(os.path.join(dirname, "../../data"))

    return os.path.join(data_dir, path)

# Deserialize the list of people involved in Enron case (dictionary type).
# enron_people["LAST_NAME FIRST_NAME MIDDLE_NAME_INITIAL"] = { features_dict }
# Some people have no MIDDLE_NAME_INITIAL, so you just have to use: enron_people["LAST_NAME FIRST_NAME"]
file_handler = open(data_path("enron_people.pkl"), "r")
enron_people = pickle.load(file_handler)
file_handler.close()

pp = pprint.PrettyPrinter(indent=2)

print("🏢 Total number of people: {0}".format(len(enron_people)))
print("🌈 Total number of features: {0}".format(len(enron_people["SKILLING JEFFREY K"])))

total_poi = sum([person["poi"] for person in enron_people.itervalues()])
print("🤡 Total people of interest: {0}".format(total_poi))

print("💰 Total stock value for James Prentice: ${0:,.2f}".format(enron_people["PRENTICE JAMES"]["total_stock_value"]))
print("💌 Total emails from Wesley Colwell to POI: {0}".format(enron_people["COLWELL WESLEY"]["from_this_person_to_poi"]))
print("💰 Total amout of stock options excercised by Jeffrey K Skilling: ${0:,.2f}".format(enron_people["SKILLING JEFFREY K"]["exercised_stock_options"]))

top_people_names = ["LAY KENNETH L", "SKILLING JEFFREY K", "FASTOW ANDREW S"]
top_people = [{"name": person[0], "total_payments": person[1]["total_payments"]} for person in enron_people.iteritems() if person[0] in top_people_names]
person_biggest_total_payments = reduce(lambda paid_most, person: person if person["total_payments"] > paid_most["total_payments"] else paid_most, top_people, { "total_payments": 0 })
print("💰 Person with biggest payment: {0[name]} (${0[total_payments]:,.2f})".format(person_biggest_total_payments))

people_with_salary = filter(lambda person: person[1]["salary"] != "NaN", enron_people.iteritems())
people_with_email_address = filter(lambda person: person[1]["email_address"] != "NaN", enron_people.iteritems())
print("💵 People with salary information: {0}".format(len(people_with_salary)))
print("📧 People with email address information: {0}".format(len(people_with_email_address)))

people_without_total_payments = filter(lambda person: person[1]["total_payments"] == "NaN", enron_people.iteritems())
print("❓ People without total payment information: {0} ({1:.2%})".format(len(people_without_total_payments), len(people_without_total_payments) / float(len(enron_people))))

poi = filter(lambda person: person[1]["poi"], enron_people.iteritems())
poi_without_total_payments = filter(lambda person: person[1]["total_payments"] == "NaN", poi)
print("❓ POI without total payment information: {0} ({1:.2%})".format(len(poi_without_total_payments), len(poi_without_total_payments) / float(len(poi))))
