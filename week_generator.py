import os.path

uke_nr = int(input("Hva uke skal genereres? "))

uke_folder = f"uke{uke_nr}"

if os.path.exists(uke_folder):
    print("Denne uken finst allerede.")
    exit(0)

nr_oppg_filer = int(input("Hvor mange oppgaver finst det? "))


os.mkdir(uke_folder)

print(f"Generated folder: {uke_folder}")

for i in range(nr_oppg_filer):
    file_path = f"{uke_folder}/uke_{uke_nr:02d}_oppg_{i+1}.py"

    if not os.path.exists(file_path):
        opened = open(file_path, mode="w")
        opened.close()

        print(f"Generated file: {file_path}")