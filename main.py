from collections import namedtuple

Vaulter = namedtuple('Vaulter', 'i_height s_height i_speed s_speed')


def week_1():
    height = int(input('Please enter the pole vaulter\'s height: \n'))
    max_speed = float(input("Please enter the pole vaulter's maximum running speed: \n"))
    return height, max_speed


def week_2(height, max_speed):
    standard_height = height * 0.0254
    standard_max_speed = max_speed * 0.44704
    return standard_height, standard_max_speed


def week_3(i_height, s_height, i_speed, s_speed):
    vaulter_list = [[i_height, s_height], [i_speed, s_speed]]
    vaulter_dict = {'i_height': i_height, 's_height': s_height, 'i_speed': i_speed, 's_speed': s_speed}
    vaulter_namedtuple = Vaulter(i_height, s_height, i_speed, s_speed)  # might have to multiply standard units values
    return vaulter_list, vaulter_dict, vaulter_namedtuple


def week_4(vaulter):
    if type(vaulter) == list:
        jump_height = 0.5 * ((vaulter[1][1] ** 2) / 9.8) + vaulter[0][1]
    elif type(vaulter) == dict:
        jump_height = 0.5 * ((vaulter['s_speed'] ** 2) / 9.8) + vaulter['s_height']
    else:  # might have to hard code for it being a namedtuple type
        jump_height = 0.5 * ((vaulter.s_speed ** 2) / 9.8) + vaulter.s_height
    return jump_height


def week_5(applicants):
    scores = []
    for n in range(applicants):
        i_height = input()
        i_speed = input()
        applicant_info = [i_height, i_speed]
        scores.append(applicant_info)
    return scores


def week_6(scores):
    vaulters = []
    for indexes in range(len(scores)):
        vaulter_profile = []
        vaulter_list = [[scores[indexes][0], scores[indexes][0] * 0.0254], [scores[indexes][1], scores[indexes][
            1] * 0.44707]]  # might have to only include imperial units and not standard conversions
        vaulter_dict = {'i_height': scores[indexes][0], 's_height': scores[indexes][0] * 0.0254,
                        'i_speed': scores[indexes][1], 's_speed': scores[indexes][1] * 0.44707}
        vaulter_namedtuple = Vaulter(scores[indexes][0], scores[indexes][0] * 0.0254, scores[indexes][1],
                                     scores[indexes][
                                         1] * 0.44707)  # might have to assign variables for standard units and then plug them in
        vaulter_profile = [vaulter1_list, vaulter1_dict, vaulter1_namedtuple]
        vaulters.append(vaulter_profile)
    return vaulters


def week_7(vaulters, cutoff):
    for data in vaulters:
        if type(data) == list:
            jump_height = 0.5 * ((data[1][1] ** 2) / 9.8) + data[0][1]
            if jump_height < cutoff:
                vaulters.remove(data)
        elif type(data) == dict:
            jump_height = 0.5 * ((data['s_speed'] ** 2) / 9.8) + data['s_height']
            if jump_height < cutoff:
                vaulters.remove(data)
        else:
            jump_height = 0.5 * ((vaulter.s_speed ** 2) / 9.8) + vaulter.s_height
            if jump_height < cutoff:
                vaulters.remove(data)
    team_members = vaulters
    return team_members


def week_8(vaulters):
    for data in vaulters:
        print(
            f"Applicant's height {data[i_height]}, applicant's vaulting speed: {data[i_speed]}, applicant's estimated jump_height: {(0.5 * ((data['s_speed'] ** 2) / 9.8) + data['s_height']) / 0.0254}")


def week_9(vaulter_file, cutoff):
    """
    Creates a report list using a text file.

    Arguments:
        vaulter_file -- a file with each line in the format "i_height, i_speed\n"
        cutoff -- the minimum estimated jump_height needed for a vaulter to make the team

    Return values:
        file_report -- a list of strings in the format:
                       "Applicant's height {}, applicant's vaulting speed: {}, applicant's estimated jump_height: {}"
    """
    pass


def week_10(report):
    """
    Given a report, sort it by the jump_height

    Arguments:
        report -- a list of strings reporting candidate statistics

    Return values:
        sorted_report -- a sorted list of strings representing each candidate's jump height (a one line comprehension is fine)
    """
    pass


if __name__ == "__main__":
    # Here is a a suite of print statements to help you test your code
    # I are the two recommended examples for basic testing:
    #     height 1, and speed 10; a patholigical example to test edge cases
    #     height 72, speed 23; a realistic example of an olympic athelete

    ti_height, ti_speed = week_1()
    print("Test week 1 ti_height:", ti_height)
    print("Test week 1 ti_speed:", ti_speed)
    print()

    ts_height, ts_speed = week_2(ti_height, ti_speed)
    print("Test week 2 ts_height:", ts_height)
    print("Test week 2 ts_speed:", ts_speed)
    print()

    tv_list, tv_dict, tv_namedtuple = week_3(ti_height, ts_height, ti_speed, ts_speed)
    print("Test week 3 tv_list:", tv_list)
    print("Test week 3 tv_dict:", tv_dict)
    print("Test week 3 tv_namedtuple:", tv_namedtuple)
    print()

    l_j_height = week_4(tv_list)
    d_j_height = week_4(tv_dict)
    n_j_height = week_4(tv_namedtuple)
    print("Test week 4 l_j_height:", l_j_height)
    print("Test week 4 tv_dict:", tv_dict)
    print("Test week 4 tv_namedtuple:", tv_namedtuple)
    print()

    applicant_num = int(input("Please enter the number of applicants you would like to test: \n"))
    app_list = week_5(applicant_num)
    for i, app in enumerate(app_list):
        print(f"Testing week 5 applicant {i}: {app}")
    print()

    sc_list = week_6(app_list)
    for j, appl in enumerate(sc_list):
        print(f"testing week 6 number {j}: \n\tlist: {appl[0]}\n\tdict: {appl[1]}\n\tamedtuple: {appl[2]}")
    print()

    cutoff_test = int(input("Please enter a value to test cutoff for week 7: \n"))
    test_team_members = week_7([sc[1] for sc in sc_list], cutoff_test)
    print("Test week 7:", test_team_members)
    print()

    test_r = week_8(test_team_members)
    for k, mem in enumerate(test_r):
        print(f"Test week 8 member {k}: {mem}\n")
    print()

    test_f = week_9("vaulter_test_file.txt", cutoff_test)
    print("Testing week 9:")
    for f in test_f:
        print('\t', f)
    print()

    test_s = week_10(test_f)
    print("Test week 10:", test_s)