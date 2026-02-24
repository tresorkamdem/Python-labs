from datetime import datetime


class User:
    def __init__(self, username, password, privilege_level="standard"):
        self.__username = username
        self.__password_hash = self.__hash_password(password)
        self.__privilege_level = privilege_level
        self.__login_attempts = 0
        self.__account_status = "active"
        self.__activity_log = []

    # -------------------------
    # Private Methods
    # -------------------------

    def __hash_password(self, password):
        # Simple simulated hashing (for lab purpose)
        return f"hashed_{password}"

    def __log_activity(self, message):
        timestamp = datetime.now()
        self.__activity_log.append(f"{timestamp} - {message}")

    # -------------------------
    # Authentication Methods
    # -------------------------

    def authenticate(self, password):
        if self.__account_status == "locked":
            self.__log_activity("Login attempt on locked account")
            return False

        if self.__hash_password(password) == self.__password_hash:
            self.__login_attempts = 0
            self.__log_activity("Successful login")
            return True
        else:
            self.__login_attempts += 1
            self.__log_activity(f"Failed login attempt ({self.__login_attempts})")

            if self.__login_attempts >= 3:
                self.lock_account()

            return False

    def lock_account(self):
        self.__account_status = "locked"
        self.__log_activity("Account locked after 3 failed attempts")

    def reset_login_attempts(self):
        self.__login_attempts = 0
        self.__log_activity("Login attempts reset")

    # -------------------------
    # Privilege Control
    # -------------------------

    def check_privileges(self, required_level):
        hierarchy = {"guest": 0, "standard": 1, "admin": 2}
        return hierarchy.get(self.__privilege_level, 0) >= hierarchy.get(required_level, 0)

    # -------------------------
    # Safe Display Method
    # -------------------------

    def get_user_info(self):
        return {
            "username": self.__username,
            "privilege_level": self.__privilege_level,
            "account_status": self.__account_status
        }

    # -------------------------
    # Getter Methods
    # -------------------------

    def get_username(self):
        return self.__username

    def get_activity_log(self):
        return self.__activity_log


# -------------------------
# Simple Test (Required for Lab)
# -------------------------

if __name__ == "__main__":
    user = User(username="kamdem", password="password1234", privilege_level="standard")

    print("Login 1:", user.authenticate("wrong"))
    print("Login 2:", user.authenticate("wrong"))
    print("Login 3:", user.authenticate("wrong"))  # Should lock account
    print("Login 4:", user.authenticate("password1234"))  # Should fail (locked)

    print("\nUser Info:", user.get_user_info())

    print("\nActivity Log:")
    for entry in user.get_activity_log():
        print(entry)


