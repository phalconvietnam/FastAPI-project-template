import enum


class UserRole(enum.Enum):
    ADMIN_ROLE = 'administrators'
    USER_ROLE = 'users'
    GUEST_ROLE = 'guests'
