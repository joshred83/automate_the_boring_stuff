

def comma_code(my_list):
    if my_list and len(my_list) > 1:
        return ', '.join(my_list[:-1]) + ', and ' + my_list[-1]
    elif len(my_list) == 1:
        return str(my_list[0])
    else:
        return ''


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
