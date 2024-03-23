"""
利用地图数据计算风险程度
severity, probability, exposure
0.2-1
severity:1-5
5*sever1** (1.0 / n)*sever2** (1.0 / n)...*servern** (1.0 / n)
取所有参与人员的严重程度的平均值
exposure:1-5
num 1-10 people-> 1-5
probability
1-5
"""
AIRBAG_DEPLOYED={"DEPLOYED, FRONT":0.8,"DID NOT DEPLOY":0.2,"DEPLOYED, SIDE":0.7,"DEPLOYMENT UNKNOWN":0.6,"DEPLOYED, COMBINATION":1,"DEPLOYED OTHER (KNEE, AIR, BELT, ETC.)":0.6,"NOT APPLICABLE":0.5}
INJURY_CLASSIFICATION={"NONINCAPACITATING INJURY":0.6,"REPORTED, NOT EVIDENT":0.4,"NO INDICATION OF INJURY":0.2,"INCAPACITATING INJURY":0.8," FATAL ":1}

