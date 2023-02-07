# --------- Intro to Hashing ----------

from werkzeug.security import generate_password_hash, check_password_hash

hardcoded_password_string = "123456789_bad_password"

hashed_password = generate_password_hash(hardcoded_password_string)
print(hashed_password)

password_attempt_one = "abcdefghij_123456789"

hash_match_one = check_password_hash(hashed_password, password_attempt_one)
print(hash_match_one)

password_attempt_two = "123456789_bad_password"

hash_match_two = check_password_hash(hashed_password, password_attempt_two)
print(hash_match_two)
