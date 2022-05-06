USER_ROLE_SUPER_USER = 1
USER_ROLE_HOTELIER = 2
USER_ROLE_CUSTOMER = 3
USER_ROLES = (
    (USER_ROLE_SUPER_USER, 'super admin'),
    (USER_ROLE_HOTELIER, 'hotelier'),
    (USER_ROLE_CUSTOMER, 'customer'),
)

star_numbers = (
    (1, "One-Star"),
    (2, "Two-Star"),
    (3, "Three-Star"),
    (4, "Four-Star"),
    (5, "Five-Star")
)
room_type = (
    ("SINGLE", "Single Room"),
    ("K_DOUBLE", "King Double Room"),
    ("Q_DOUBLE", "Queen Double Room"),
    ("SINGLE_DELUXE", "Single Deluxe Room"),
    ("DOUBLE_DELUXE", "Double Deluxe Room"),
    ("TWIN", "Twin Room"),
    ("TWIN_DOUBLE", "Twin Double Room"),
    ("TRIPLE", "Triple Room"),
    ("PRESIDENTIAL", "Presidential Suite")
)
status_choices = (
    (1, "Paid"),
    (0, "Unpaid"),
)
