# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 22:03:00 2018

@author: 葛云飞
"""

import json

txt = ""
'''
with open('PMtask_Relation_TestSet.json', 'r') as f:
  data = json.load(f)
  for i in data["documents"]:
#      print(i["id"]+"|t|"+i["passages"][0]["text"])
      txt = txt + i["id"]+"|t|"+i["passages"][0]["text"] + "\n"
#      print(i["id"]+"|t|"+i["passages"][1]["text"])
      txt = txt + i["id"]+"|t|"+i["passages"][1]["text"] + "\n"
      for j in i["passages"][0]["annotations"]:
          txt = txt + i["id"]+"\t"+str(j["locations"][0]["offset"])+"\t"+str(j["locations"][0]["offset"]+j["locations"][0]["length"])+"\t"+j["text"]+"\t"+j["infons"]["type"]+"\t"+j["infons"]["identifier"] + "\n"
#          print(i["id"]+"\t"+str(j["locations"][0]["offset"])+"\t"+str(j["locations"][0]["offset"]+j["locations"][0]["length"])+"\t"+j["text"]+"\t"+j["infons"]["type"]+"\t"+j["infons"]["identifier"])
      for j in i["passages"][1]["annotations"]:
          txt = txt + i["id"]+"\t"+str(j["locations"][0]["offset"])+"\t"+str(j["locations"][0]["offset"]+j["locations"][0]["length"])+"\t"+j["text"]+"\t"+j["infons"]["type"]+"\t"+j["infons"]["identifier"] + "\n"
#          print(i["id"]+"\t"+str(j["locations"][0]["offset"])+"\t"+str(j["locations"][0]["offset"]+j["locations"][0]["length"])+"\t"+j["text"]+"\t"+j["infons"]["type"]+"\t"+j["infons"]["identifier"])
      for k in i["relations"]:
          txt = txt + i["id"]+"\tCID\t"+k["infons"]["Gene1"]+"\t"+k["infons"]["Gene2"] + "\n"
#          print(i["id"]+"\tCID\t"+k["infons"]["Gene1"]+"\t"+k["infons"]["Gene2"])
      txt = txt + "\n"
print(txt)

with open("PMtask_Relation_TestSet.txt", "w",encoding="utf-8")as f:
    f.write(txt)
'''

with open('PMtask_Relations_TrainingSet.json', 'r') as f:
  data = json.load(f)
  for i in data["documents"]:
#      print(i["id"]+"|t|"+i["passages"][0]["text"])
      txt = txt + i["id"]+"|t|"+i["passages"][0]["text"] + "\n"
#      print(i["id"]+"|t|"+i["passages"][1]["text"])
      txt = txt + i["id"]+"|t|"+i["passages"][1]["text"] + "\n"
      for j in i["passages"][0]["annotations"]:
          txt = txt + i["id"]+"\t"+str(j["locations"][0]["offset"])+"\t"+str(j["locations"][0]["offset"]+j["locations"][0]["length"])+"\t"+j["text"]+"\t"+j["infons"]["type"]+"\t"+j["infons"]["NCBI GENE"] + "\n"
#          print(i["id"]+"\t"+str(j["locations"][0]["offset"])+"\t"+str(j["locations"][0]["offset"]+j["locations"][0]["length"])+"\t"+j["text"]+"\t"+j["infons"]["type"]+"\t"+j["infons"]["identifier"])
      for j in i["passages"][1]["annotations"]:
          txt = txt + i["id"]+"\t"+str(j["locations"][0]["offset"])+"\t"+str(j["locations"][0]["offset"]+j["locations"][0]["length"])+"\t"+j["text"]+"\t"+j["infons"]["type"]+"\t"+j["infons"]["NCBI GENE"] + "\n"
#          print(i["id"]+"\t"+str(j["locations"][0]["offset"])+"\t"+str(j["locations"][0]["offset"]+j["locations"][0]["length"])+"\t"+j["text"]+"\t"+j["infons"]["type"]+"\t"+j["infons"]["identifier"])
      for k in i["relations"]:
          txt = txt + i["id"]+"\tCID\t"+k["infons"]["Gene1"]+"\t"+k["infons"]["Gene2"] + "\n"
#          print(i["id"]+"\tCID\t"+k["infons"]["Gene1"]+"\t"+k["infons"]["Gene2"])
      txt = txt + "\n"
print(txt)

with open("PMtask_Relations_TrainingSet.txt", "w",encoding="utf-8")as f:
    f.write(txt)