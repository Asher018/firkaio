**Firka.io projekt leírás**


**Basic Git parancsok:**

Első alkalommal:

 - git config --global user.name "Your Name"
 - git config --global user.email "youremail@yourdomain.com"


Branch létrehozás, elnevezési konvenció:
 - git checkout -b bugfix/short_name_of_bug-issueSzám
 - git checkout -b feature/short_name-of_feature-1

git add :
 - git add . -> mappából minden fájlt hozzáad
 - git add -A -> minden fájlt hozzáad
 - git add -u -> csak tracked file-ok hozzáadása
 - git add -p -> módosítások kiválasztása

git diff:
 - git diff --cached -> hozzáadott módosítások átnézése

git commit, egysoros message: 
 - git commit -m "[#1] Rövid commit leírás"

push: 
 - git push origin bugfix/short_name_of_bug-1
 -  - csak első alkalommal kell a branch, utána elég a git push

Merge request:
 - push-t követően terminálban kidob egy linket az MR-hez ahol véglegesíteni lehet azt

Git reset:
 - git reset --soft HEAD~1
 - - lokális branchről visszavonja a legutóbbi commitot
 - git reset --hard HEAD~1
 - - minden nem commitolt változás + az előző commit elveszik

Local branch törlése
 - git branch -d <local-branch>
 - -D megerősíteni

Remote branch törlés
 - git push origin --delete <branch>
