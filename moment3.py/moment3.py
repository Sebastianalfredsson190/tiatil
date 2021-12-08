lön = int(input("Hur många kr tjänar du varje månad?"))
kommunalskatt=lön*0.2136
landstingsskatt=lön*0.1148
lönefterskatt=lön-kommunalskatt-landstingsskatt
årslön = lön*12
statligskatt=0


if årslön < 19247:
    kommunalskatt=0
    landstingsskatt=0
    lönefterskatt=lön-kommunalskatt-landstingsskatt
    
if årslön > 468700 and årslön < 675700:
    statligskatt=lön*0.2
    lönefterskatt=lön-statligskatt-landstingsskatt-kommunalskatt
    print(f"Du betalar: {round(statligskatt)}kr i statligskatt")

if årslön > 675700:
    statligskatt=lön*0.25
    lönefterskatt=lön-statligskatt-landstingsskatt-kommunalskatt
    print(f"Du betalar: {round(statligskatt)}kr i statligskatt")

totalskatt=statligskatt+kommunalskatt+landstingsskatt
bruttolön1=totalskatt/lön
bruttolön2=bruttolön1*100

print(f"Din lön: {round(lön)}kr")
print(f"Din kommunalaskatt ligger på: {round(kommunalskatt)}kr")
print(f"Din landstingsskatt ligger på: {round(landstingsskatt)}kr")
print(f"Din totalt betala skatt ligger på: {round(totalskatt)}kr")
print(f"Andel betald skatt: {round(bruttolön2,2)}%")
print(f"Din lön efter skatt: {round(lönefterskatt)}kr")