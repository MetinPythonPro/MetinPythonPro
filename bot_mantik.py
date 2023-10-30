import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def emoji_olusturucu():
    emoji = [":grinning:", ":smiley:", ":smile:", ":grin:", ":laughing:", ":face_holding_back_tears:", ":sweat_smile:", ":joy:", ":rofl:", ":smiling_face_with_tear: ", ":relaxed:", ":blush:", ":innocent:", ":slight_smile:", ":upside_down:", ":wink:", ":relieved:", ":heart_eyes:", ":smiling_face_with_3_hearts:", ":kissing_heart:", ":kissing:", ":kissing_smiling_eyes:", ":kissing_closed_eyes:", ":yum:", ":stuck_out_tongue:", ":stuck_out_tongue_closed_eyes: ", ":stuck_out_tongue_winking_eye:", ":zany_face:", ":face_with_raised_eyebrow:"]
    return random.choice(emoji)

def yazi_tura():
    para = random.randint(0, 2)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"
