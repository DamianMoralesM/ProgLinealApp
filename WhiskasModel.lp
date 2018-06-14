\* The Whiskas Problem *\
Maximize
Total_Cost_of_Ingredients_per_can: 0.008 BeefPercent + 0.013 ChickenPercent
Subject To
PercentagesSum: 3 BeefPercent + ChickenPercent <= 30
PercentagesSum2: 2 BeefPercent + 6 ChickenPercent <= 20
Bounds
0 <= ChickenPercent
Generals
ChickenPercent
End
