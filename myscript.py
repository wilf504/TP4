# myscript.py
import os
import sys

bad = sys.argv[1] if len(sys.argv) > 1 else os.getenv("BAD_HASH")
good = sys.argv[2] if len(sys.argv) > 2 else os.getenv("GOOD_HASH")

if not bad or not good:
    print("Erreur")
    sys.exit(2)

print(f"git bisect start {bad} {good}")
os.system(f"git bisect start {bad} {good}")

print("Lancement de git bisect run avec la commande de test Django")
rc = os.system("git bisect run python manage.py test budget.tests")

print("Reset bisect")
os.system("git bisect reset")


if rc == 0:
    sys.exit(0)
else:
    sys.exit(1)
