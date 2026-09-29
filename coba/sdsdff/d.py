# main.py

import random
from c import welcome_message


def get_yes_no(prompt):
    """Minta input y/n dan loop sampai valid."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "n"):
            return answer 
        print("Masukkan 'y' atau 'n'.")


def get_choice():
    """Minta pilihan goa 1-4 dan loop sampai valid."""
    while True:
        choice = input("Menurut kamu di goa nomor berapa cuypy berada? [1/2/3/4]: ").strip()
        if choice in ("1", "2", "3", "4"):
            return int(choice)
        print("Pilihan tidak valid. Silakan coba lagi.")


def main():
    welcome_message("Welcome to Cuypy")

    nama_user = input("Masukkan nama kamu: ").strip()
    while not nama_user:
        nama_user = input("Isi nama kamu: ").strip()

    previous_position = None

    while True:
        # Pilih posisi cuypy secara acak, dan pastikan berbeda dari ronde sebelumnya
        if previous_position is None:
            cuypy_position = random.randint(1, 4)
        else:
            possible_positions = [p for p in range(1, 5) if p != previous_position]
            cuypy_position = random.choice(possible_positions)

        previous_position = cuypy_position

        # Siapkan kotak
        empty_boxes = ["|_|"] * 4
        hidden_boxes = empty_boxes.copy()
        hidden_boxes[cuypy_position - 1] = "|i_t|"

        empty_display = " ".join(empty_boxes)
        hidden_display = " ".join(hidden_boxes)

        # Loop tebakan untuk ronde ini
        while True:
            print(f"\nHalo {nama_user}! Coba perhatikan goa di bawah ini:")
            print(empty_display)

            pilihan_user = get_choice()
            confirm_answer = get_yes_no(
                f"Apakah kamu yakin jawabannya adalah {pilihan_user}? [y/n]: "
            )

            if confirm_answer == "n":
                print("Baik, silakan pilih lagi.")
                continue

            # confirm_answer == "y"
            if pilihan_user == cuypy_position:
                print(f"{hidden_display}\nSelamat {nama_user}, kamu menang!")
            else:
                print(
                    f"{hidden_display}\nKamu kalah! "
                    f"Cuypy berada di goa nomor {cuypy_position}."
                )
            break

        # Tanya lanjut atau tidak
        lanjut = get_yes_no("\nApakah ingin melanjutkan? [y/n]: ")
        if lanjut == "n":
            print("Terima kasih sudah bermain. Selesai!")
            break


if __name__ == "__main__":
    main()