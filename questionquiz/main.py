print("Dobrodosli na AskPython kviz!")
answer=input("Da li ste spremni? (da/ne) :").strip().lower()
score=0
total_question=3

if answer.lower() == "da":
    answer= input("Pitanje broj 1: Koji je glavni grad Srbije? ").strip().lower()
    if answer.lower() == "beograd":
        score +=1
        print("Bravo! Tacan odgovor")
    else:
        print("Netacan odgovor 😒")

    answer= input("Pitanje broj 2: Da li se Srbija granici sa 9 drzava? ").strip().lower()
    if answer.lower() == "ne":
        score+=1
        print("Bravo! Tacan odgovor")
    else:
        print("Netacan odgovor 😒")

    answer= input("Pitanje broj 3: Koja je najduza reka koja protice kroz Srbiju? ").strip().lower()
    if answer.lower() == "dunav":
        score+=1
        print("Bravo! Tacan odgovor")
    else:
        print("Netacan odgovor 😒")

print(f"Hvala sto ste ucestvovali na nasem kratkom kvizu, vas skor je {score}")
bod=(score/total_question)*100
print(f"Ukupan broj bodova: {bod}")
print("CAOS")