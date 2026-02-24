from datetime import datetime, timedelta


# =========================
# USER CLASS
# =========================
class User:
    def __init__(self, username, role="standard"):
        self.__username = username
        self.__role = role  # "standard" or "admin"

    def get_username(self):
        return self.__username

    def is_admin(self):
        return self.__role == "admin"


# =========================
# DEVICE CLASS
# =========================
class Device:
    def __init__(self, device_id, device_type, owner):
        self.__device_id = device_id
        self.__device_type = device_type
        self.__owner = owner
        self.__firmware_version = "1.0"
        self.__last_security_scan = None
        self.__is_active = True
        self.__is_quarantined = False

    # ---------------------
    # Security Methods
    # ---------------------
    def run_security_scan(self):
        self.__last_security_scan = datetime.now()
        print(f"[SCAN] Device {self.__device_id} scanned successfully.")

    def check_compliance(self):
        if self.__last_security_scan is None:
            return False

        days_since_scan = (datetime.now() - self.__last_security_scan).days
        return days_since_scan <= 30

    def update_firmware(self, version, user):
        if not user.is_admin():
            print("Access denied: Admins only.")
            return

        self.__firmware_version = version
        print(f"[UPDATE] Firmware updated to {version}")

    def quarantine(self, user):
        if not user.is_admin():
            print("Access denied: Admins only.")
            return

        self.__is_quarantined = True
        self.__is_active = False
        print(f"[QUARANTINE] Device {self.__device_id} quarantined.")

    # ---------------------
    # Access Control
    # ---------------------
    def access_device(self, user):
        if not self.__is_active:
            print("Device inactive.")
            return False

        if self.__is_quarantined:
            print("Device quarantined.")
            return False

        if not self.check_compliance():
            print("Device not compliant.")
            return False

        if user.get_username() != self.__owner and not user.is_admin():
            print("Access denied: Not owner.")
            return False

        print("Access granted.")
        return True

    # ---------------------
    # Info
    # ---------------------
    def get_info(self):
        return {
            "device_id": self.__device_id,
            "type": self.__device_type,
            "firmware": self.__firmware_version,
            "owner": self.__owner,
            "compliant": self.check_compliance(),
            "active": self.__is_active,
        }


# =========================
# DEVICE MANAGER
# =========================
class DeviceManager:
    def __init__(self):
        self.__devices = {}

    def add_device(self, device):
        self.__devices[device.get_info()["device_id"]] = device

    def remove_device(self, device_id, user):
        if not user.is_admin():
            print("Only admin can remove devices.")
            return

        if device_id in self.__devices:
            del self.__devices[device_id]
            print("Device removed.")

    def generate_report(self):
        print("\n=== SECURITY REPORT ===")
        for device in self.__devices.values():
            print(device.get_info())


# =========================
# TESTING
# =========================
if __name__ == "__main__":

    admin = User("kamdem_admin", "admin")
    user1 = User("kamdem", "standard")

    manager = DeviceManager()

    device1 = Device("D001", "Laptop", "kamdem")

    manager.add_device(device1)

    print("\nTrying access before scan:")
    device1.access_device(user1)

    print("\nRunning security scan...")
    device1.run_security_scan()

    print("\nTrying access again:")
    device1.access_device(user1)

    print("\nAdmin updating firmware:")
    device1.update_firmware("2.0", admin)

    print("\nGenerating report:")
    manager.generate_report()