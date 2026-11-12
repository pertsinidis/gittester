# Git & GitHub Cheatsheet (CMD)

## 1. Αρχική Ρύθμιση (Μία φορά σε κάθε υπολογιστή)
git config --global user.name "Το Όνομά Σου"
git config --global user.email "email@example.com"
git config --global core.editor "notepad"
git config --list

## 2. Ξεκίνημα Έργου (Νέο ή Υπάρχον)
git init                                    # Μετατρέπει τον φάκελο σε τοπικό repository
git clone <URL>                             # Κατεβάζει υπάρχον project από το GitHub
git remote add origin <URL>                 # Συνδέει τον τοπικό φάκελο με νέο repo στο GitHub
git remote set-url origin <URL>             # Αλλάζει το URL του συνδεδεμένου repo
git remote -v                               # Δείχνει σε ποιο URL είναι συνδεδεμένος ο φάκελος

## 3. Καθημερινή Ροή (Αποθήκευση & Ανέβασμα)
git status                                  # Δείχνει ποιες αλλαγές υπάρχουν στον φάκελο
git add <αρχείο>                            # Προσθέτει συγκεκριμένο αρχείο για commit
git add .                                   # Προσθέτει ΟΛΑ τα νέα/τροποποιημένα αρχεία
git commit -m "Μήνυμα αλλαγής"              # Αποθηκεύει μόνιμα τις αλλαγές τοπικά
git push -u origin main                     # Πρώτο ανέβασμα του κλάδου main στο GitHub
git push                                    # Ανεβάζει τα επόμενα commits στο GitHub

## 4. Κατέβασμα Αλλαγών (Ενημέρωση από GitHub)
git pull                                    # Κατεβάζει και ενσωματώνει αλλαγές από το GitHub
git fetch                                   # Ελέγχει αν υπάρχουν αλλαγές online χωρίς να αλλάξει αρχεία

## 5. Κλάδοι (Branches)
git branch                                  # Εμφανίζει τους τοπικούς κλάδους
git branch <όνομα>                          # Δημιουργεί νέο κλάδο
git checkout -b <όνομα>                     # Δημιουργεί νέο κλάδο και μπαίνει σε αυτόν
git checkout main                           # Επιστρέφει στον κύριο κλάδο (main)
git merge <όνομα>                           # Ενσωματώνει τον κλάδο <όνομα> στον τρέχοντα κλάδο

## 6. Ιστορικό & Αναίρεση Λαθών (Undo)
git log --oneline                           # Δείχνει συνοπτικά το ιστορικό των commits
git diff                                    # Δείχνει γραμμή προς γραμμή τις αλλαγές πριν το git add
git checkout -- <αρχείο>                    # Επαναφέρει ένα αρχείο στην κατάσταση του τελευταίου commit
git reset HEAD <αρχείο>                     # Βγάζει ένα αρχείο από την αναμονή (μετά από λάθος git add)
git revert <id-του-commit>                  # Αναιρεί ένα παλαιότερο commit δημιουργώντας νέο

## 7. Έξοδος από Κειμενογράφο Vim (αν ανοίξει κατά λάθος)
# Πάτα Esc, γράψε :wq και πάτα Enter (για αποθήκευση & έξοδο)
# Πάτα Esc, γράψε :q! και πάτα Enter (για έξοδο ΧΩΡΙΣ αποθήκευση)

## 8. Ασφάλεια σε Κοινόχρηστο Υπολογιστή (π.χ. Student)
cmdkey /delete:git:https://github.com       # Διαγράφει τα αποθηκευμένα στοιχεία σύνδεσής σου
