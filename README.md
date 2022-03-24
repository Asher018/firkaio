**Firka.io projekt leírás**


## Basic Git parancsok

### Első alkalommal
```
git config --global user.name "Your Name"
git config --global user.email "youremail@yourdomain.com"
```

Ha nem akarod véletlenül mindenhol a saját neved és hivatalos email címed használni:
```
git config user.name "Mike Ainsel"
git config user.email mike@example.com
```

Pl nem jó ötlet mindenhol a studos emailedet használni, de egyetemi projekteknél pont van értelme. Szóval óvatosan a global kapcsolóval.

### Branch létrehozás, elnevezési konvenció:
 - `git checkout -b bugfix/short_name_of_bug-issueSzám`
 - `git checkout -b feature/short_name_of_feature-1`

### git add
 - `git add .` -> mappából minden fájlt hozzáad
 - `git add -A` -> minden fájlt hozzáad
 - `git add -u` -> csak tracked file-ok hozzáadása
 - `git add -p` -> módosítások kiválasztása

### git diff
 - `git diff --cached` -> hozzáadott módosítások átnézése

### git commit, egysoros message: 
 - `git commit -m "[#1] Rövid commit leírás"`

### előző commit javítása
 - `git commit --amend`: hozzáadott változtatásokat is beleveszi a HEAD commitba, plusz a commit üzenetet átírhatod

### git rebase

Történelem átírására sötét mágia, pár sorban nem lehet összefoglalni, itt olvashattok róla: https://git-rebase.io/

### push: 
 - `git push origin bugfix/short_name_of_bug-1`
 -  - csak első alkalommal kell a branch, utána elég a git push

### Merge request:
 - push-t követően terminálban kidob egy linket az MR-hez ahol véglegesíteni lehet azt

### Git reset:
 - `git reset --soft HEAD~`
 - - lokális branchről visszavonja a legutóbbi commitot
 - `git reset --hard HEAD~1`
 - - minden nem commitolt változás + az előző commit elveszik

### Local branch törlése
 - `git branch -d <local-branch>`
 - `-D` megerősíteni

### Remote branch törlés
 - `git push origin --delete <branch>`
