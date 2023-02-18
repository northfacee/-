def solution(id_list, report, w):
    report_list = {}
    report_name = {}
    for k in report:
        if k.split(' ')[1] not in report_list:
            report_list[k.split(' ')[1]] = 1
        else:
            report_list[k.split(' ')[1]] +=1

        if k.split(' ')[0] not in report_name:
            report_name[k.split(' ')[0]] = [k.split(' ')[1]]
        else:
            report_name[k.split(' ')[0]] += [k.split(' ')[1]]
    for name in id_list:
        if name not in report_list:
            report_list[name] = 0
        if name not in report_name:
            report_name[name] = ['X']
            
    ban_list = []
    report_list = sorted(report_list.items(), reverse=True, key=lambda x : x[1])
    for ban in report_list:
        if ban[1] == w:
            ban_list.append(ban[0])
    
    # ban_list, report_name
        
        
    
    return report_name
