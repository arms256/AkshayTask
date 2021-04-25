Sample_request_json = {'columns': [
  {'field_name': 'A_Q1', 'display_name': 'A_Q1', 'data_type': 'character'},
  {'field_name': 'A_Q2', 'display_name': 'A_Q2', 'data_type': 'character'},
  {'field_name': 'A_Q3', 'display_name': 'A_Q3', 'data_type': 'character'},
  {'field_name': 'B_Q1', 'display_name': 'B_Q1', 'data_type': 'character'},
  {'field_name': 'B_Q2', 'display_name': 'B_Q2', 'data_type': 'character'},
  {'field_name': 'B_Q3', 'display_name': 'B_Q3', 'data_type': 'character'},
],
 'data': [{
   'A_Q1': 'Monthly,Semi-Annually',
   'A_Q2': 'Senior Management,Individual Contributors',
   'A_Q3': 'No',
   'B_Q1': 'Wednesdays,Saturdays;Sundays',
   'B_Q2': 'Not Applicable',
   'B_Q3': 'Directors; Managers,IT Consultants,Security consultants'
}]}


answer_dict = {
    0: {
        "Answers": {
            "Monthly": 3,
            "Quarterly": 3,
            "Financial information": 1,
            "Semi-Annually": 1,
            "Annually": 3
        },
        "Column Display Name": "A_Q1",
        "Answer Type": "multi choice"
    },
    1: {
        "Answers": {
            "Senior Management": 5,
            "Individual Contributors": 3,
            "Customers": 5,
            "Vendors": 3
        },
        "Column Display Name": "A_Q2",
        "Answer Type": "multi choice"
    },
    2: {
        "Answers": {
            "YES": 1,
            "NO": 10
        },
        "Column Display Name": "A_Q3",
        "Answer Type": "single choice"
    },
    3: {
        "Answers": {
            "AAA": 1,
            "CAA": 1,
            "BCAA": 1
        },
        "Column Display Name": "A_Q4",
        "Answer Type": "multi choice"
    },
    4: {
        "Answers": {
            "Under USD10,000": 1,
            "Between USD10,000 and USD100,000": 3,
            "Over USD100,000": 5
        },
        "Column Display Name": "A_Q5",
        "Answer Type": "single choice"
    },
    5: {
        "Answers": {
            "Mondays": 1,
            "Tuesdays": 1,
            "Wednesdays": 1,
            "Thursdays": 1,
            "Fridays": 1,
            "Saturdays;Sundays": 5,
        },
        "Column Display Name": "B_Q1",
        "Answer Type": "multi choice"
    },
    6: {
        "Answers": {
            "Less than previous year": 1,
            "Same as previous year": 3,
            "Greater than previous year": 5,
            "Not applicable": 10
        },
        "Column Display Name": "B_Q2",
        "Answer Type": "single choice"
    },
    7: {
        "Answers": {
            "Directors; Managers": 5,
            "IT Consultants": 1,
            "Security Consultants": 1,
            "Employees": 5
        },
        "Column Display Name": "B_Q3",
        "Answer Type": "multi choice"
    }
}


def score():
    sum_score_A = []
    sum_score_B = []
    data = Sample_request_json['data']
    for data in data:
        for q_no,response in data.items():
            for answer_dict_key, answer_dict_value in answer_dict.items():
                if q_no in answer_dict_value['Column Display Name']:
                    # print(f"key of answer_dict : {answer_dict_key}")
                    answer = answer_dict_value["Answers"]
                    answer = dict((k.lower(), v) for k, v in answer.items())
                    if ',' in response:
                        multiple_response = response.split(",")
                        for response in multiple_response:
                            if response.lower() in answer:
                                score = answer[response.lower()]
                                if q_no.startswith('A'):
                                    sum_score_A.append(score)
                                else:
                                    sum_score_B.append(score)

                    else:
                        if response.lower() in answer:
                            score = answer[response.lower()]
                            if q_no.startswith('A'):
                                sum_score_A.append(score)
                            else:
                                sum_score_B.append(score)

    return sum_score_A, sum_score_B


def max_poss_score():
    max_poss_score_A = []
    max_poss_score_B = []
    for answer_dict_key, answer_dict_value in answer_dict.items():
        if "multi choice" in answer_dict_value["Answer Type"]:
            answer = answer_dict_value['Answers']
            if answer_dict_value["Column Display Name"].startswith('A'):
                max_poss_score_A.append(sum(answer.values()))
            else:
                max_poss_score_B.append(sum(answer.values()))
        elif "single choice" in answer_dict_value["Answer Type"]:
            answer = answer_dict_value['Answers']
            if answer_dict_value["Column Display Name"].startswith('A'):
                max_poss_score_A.append(max(answer.values()))
            else:
                max_poss_score_B.append(max(answer.values()))

    return max_poss_score_A, max_poss_score_B


max_score = max_poss_score()
score = score()

print(f"{max_score} is max")
print(f"{score} is score")


max_poss_score_A = sum(max_score[0])
max_poss_score_B = sum(max_score[1])
# print(max_poss_score_A)

score_A = sum(score[0])
score_B = sum(score[1])
# print(score_A)

#risk Score

risk_score_A = int((score_A/max_poss_score_A) * 100)
risk_score_B = int((score_B/max_poss_score_B) * 100)



risk_score = [risk_score_A,risk_score_B]
for score in range(len(risk_score)):
    if risk_score[score] >80 and risk_score[score] <= 100:
        risk_level = "Critical"
    elif risk_score[score] >60 and risk_score[score] <= 80:
        risk_level = "High"
    elif risk_score[score] >40 and risk_score[score] <= 60:
        risk_level = "Medium"
    elif risk_score[score] >0 and risk_score[score] <= 40:
        risk_level = "Low"
    if score == 0 :
        print(f"risk_score_A is {risk_score[score]},risk_level_A is {risk_level}")
    else:
        print(f"risk_score_B is {risk_score[score]},risk_level_B is {risk_level}")
