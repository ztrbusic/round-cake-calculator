import math

#Inputs the original recipe tray size and ingredient amounts
print("Write the original recipe tray size:")
originalTray = int(input())

print("Write the original recipe flour amount:")
originalFlour = int(input())

print("Write the original recipe sugar amount:")
originalSugar = int(input())

print("Write the original recipe baking powder amount size:")
originalBakingPowder = int(input())

print("Write the original recipe vanilla sugar amount:")
originalVanillaSugar = int(input())

print("Write the original recipe butter amount:")
originalButter = int(input())

print("Write the original recipe egg amount:")
originalEgg = int(input())

print("Write the original recipe milk amount:")
originalMilk = int(input())

print("Write the original recipe vanilla pudding amount:")
originalVanillaPudding = int(input())

print("Write the original recipe filling sugar amount:")
originalFillingSugar = int(input())

print("Write the original recipe mileram amount:")
originalMileram = int(input())

#Inputs the target tray size
print("Write the target recipe tray size:")
targetTray = int(input())

#Calculates the ratio between original recipe and target tray sizes
originalTrayArea = math.pi * (originalTray ** 2)
targetTrayArea = math.pi * (targetTray ** 2)
trayRatio = targetTrayArea / originalTrayArea
print("Your tray ratio is " + str(trayRatio) + ".")

#Calculates the new, target, ingredient amounts using the tray ratio
targetFlour = originalFlour * trayRatio
targetSugar = originalSugar * trayRatio
targetBakingPowder = originalBakingPowder * trayRatio
targetVanillaSugar = originalVanillaSugar * trayRatio
targetButter = originalButter * trayRatio
targetEgg = originalEgg * trayRatio
targetMilk = originalMilk * trayRatio
targetVanillaPudding = originalVanillaPudding * trayRatio
targetFillingSugar = originalFillingSugar * trayRatio
targetMileram = originalMileram * trayRatio

#Rounds and prints the new ingredient amounts 
print("Your target ingredient amounts are:")
print("Flour: " + str(round(targetFlour, 2)))
print("Baking Powder: " + str(round(targetBakingPowder, 2)))
print("Vanilla sugar: " + str(round(targetVanillaSugar, 2)))
print("Butter: " + str(round(targetButter, 2)))
print("Egg: " + str(round(targetEgg, 2)))
print("Milk: " + str(round(targetMilk, 2)))
print("Vanilla pudding: " + str(round(targetVanillaPudding, 2)))
print("Sugar: " + str(round(targetSugar, 2)))
print("Mileram: " + str(round(targetMileram, 2)))