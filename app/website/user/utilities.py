from wtforms import ValidationError

def Password_complexity(form, field):
    special_chars = '!@#$%^&*()_-+=[]|\/?>.<,|'
    valid = False
    for char in field.data:
        if valid == False:
            for special in special_chars:
                if char == special: valid = True  
    if valid == False:
        raise ValidationError('Password must contain at lease one special character')
