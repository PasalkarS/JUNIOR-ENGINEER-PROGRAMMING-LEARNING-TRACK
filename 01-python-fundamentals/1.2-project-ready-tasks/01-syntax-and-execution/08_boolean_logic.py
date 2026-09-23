# 08 - Boolean Logic
# Evaluates and, or, not expressions.

has_id = True
has_ticket = False
is_vip = True

can_enter = (has_id and has_ticket) or is_vip
print("Can user enter venue?", can_enter)
