def filter_by_state(list_dict, state="EXECUTED"):
     new_list = []
     for i in list_dict:
         if i["state"] == state:
             new_list.append(i)
     return new_list

