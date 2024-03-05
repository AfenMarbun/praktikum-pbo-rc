class Robot:
    def __init__(self, nama, serangan, pertahanan, hp):
        self.nama = nama
        self.serangan = serangan
        self.pertahanan = pertahanan
        self.hp = hp

    def serang_musuh(self, musuh):
        damage = self.serangan

        if musuh.pertahanan > 0 :
            musuh.pertahanan -= damage
        else:
            musuh.hp -= damage
        print(f"{self.nama} menyerang {musuh.nama} dan menghasilkan {damage} kerusakan!")

    def bertahan(self):
        self.pertahanan += 5
        print(f"{self.nama} mengaktifkan pertahanan tambahan!")

    def menyerah(self):
        self.hp -= self.hp
        self.pertahanan -= self.pertahanan
        print(f"{self.nama} menyerah dan mengakhiri pertarungan.")

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.putaran = 0

    def putaran_permainan(self):
        self.putaran += 1
        print(f"\nPutaran {self.putaran}:")
        print(f"{self.robot1.nama} - HP: {self.robot1.hp}, Pertahanan: {self.robot1.pertahanan}")
        print(f"{self.robot2.nama} - HP: {self.robot2.hp}, Pertahanan: {self.robot2.pertahanan}")
        pilihan_robot1 = input(f"Aksi untuk {self.robot1.nama} (serang/bertahan/menyerah): ").lower()
        pilihan_robot2 = input(f"Aksi untuk {self.robot2.nama} (serang/bertahan/menyerah): ").lower()

        if pilihan_robot1 == "serang":
            self.robot1.serang_musuh(self.robot2)
        elif pilihan_robot1 == "bertahan":
            self.robot1.bertahan()
        else:
            self.robot1.menyerah()

        if self.robot2.hp > 0:
            if pilihan_robot2 == "serang":
                self.robot2.serang_musuh(self.robot1)
            elif pilihan_robot2 == "bertahan":
                self.robot2.bertahan()
            else:
                self.robot2.menyerah()

    def mulai_permainan(self):
        print("Permainan dimulai!")
        lanjutkan = "y"
        while lanjutkan.lower() == "y":
            self.putaran_permainan()
            if self.robot1.hp <= 0 or self.robot2.hp <= 0:
                lanjutkan = input("Permainan selesai. Apakah Anda ingin memulai ulang? (y/n): ")
                if lanjutkan.lower() == "y":
                    self.__init__(self.robot1, self.robot2)
                    print("Permainan dimulai kembali!")
                else:
                    print("Terima kasih telah bermain!")
                    break

robot1 = Robot("thanos", 50, 100, 100)
robot2 = Robot("ironman", 60, 100, 100)

permainan = Game(robot1, robot2)
permainan.mulai_permainan()

