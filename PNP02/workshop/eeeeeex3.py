skm=int(input("Enter start kilometer :"))
ekm=int(input("Enter end kilometer :"))
tu=input("Enter time used(hour minute second) :")
hour,minute,second=map(int, tu.split())
print()
print("Car traveled",ekm-skm,"kilometer in",hour,"hrs",minute,"min",second,"sec.")
print("Average velocity was",(ekm-skm)/(hour+(minute/60)+(second/3600))," kph.")