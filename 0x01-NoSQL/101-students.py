#!/usr/bin/env python3
'''Top students sorted
'''


import pymongo


def top_students(mongo_collection):
    '''Returns all students sorted by average score
       
       mongo_collection - database to search and find all
       documents with respective scores
    '''
    all_students = mongo_collection.find()
    all_score = []
    for each_student in all_students:
        total_score = sum(topic['score'] for topic in each_student['topics'])
        total_number = len(each_student['topics'])
        average_score = total_score / total_number
        all_score.append({'_id': each_student['_id'], 'name': each_student['name'], 'averageScore': average_score})
    sorted_students = sorted(all_score, key=lambda x: x['averageScore'], reverse=True)
    return sorted_students
